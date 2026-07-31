#!/usr/bin/env python3
"""
Auto-sync this fork with its upstream source(s), validate, and push.

Run once per session (see the throttle below) from the global CLAUDE.md
instruction. Two things are kept in sync, per tools/vendor-manifest.json:

1. The whole repo, against the fork's upstream (coreyhaines31/marketingskills):
   a plain fetch + merge.
2. Any individually vendored skill folders (currently just planning-with-files),
   which live in a different upstream repo and aren't part of the fork
   relationship, so they're synced by diffing a fresh shallow clone of their
   source repo against the local copy.

Safety rules (do not change without good reason):
- Never force-push. A push that isn't a fast-forward is left for manual review.
- Never delete local files during a vendored-skill sync, only add/update --
  avoids surprise deletions if upstream restructures.
- preserveFiles in the manifest are never overwritten (e.g. our own
  LICENSE/NOTICE.md that upstream doesn't have).
- Run validate-skills.sh before pushing. On failure, commit locally (if
  anything changed) but do NOT push, and write .sync-blocked so future runs
  stop and report instead of retrying forever.
- On a merge conflict, abort the merge and stop. Never push a conflicted tree.
"""
import json
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MANIFEST = REPO / "tools" / "vendor-manifest.json"
LAST_SYNC = REPO / "tools" / ".last-sync"
BLOCKED = REPO / "tools" / ".sync-blocked"
THROTTLE_SECONDS = 6 * 3600  # don't check more than once every 6 hours


def run(cmd, cwd=REPO, check=True):
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and result.returncode != 0:
        raise RuntimeError(f"command failed: {cmd}\n{result.stdout}\n{result.stderr}")
    return result


def log(msg):
    print(f"[sync-upstream] {msg}")


def throttled():
    if not LAST_SYNC.exists():
        return False
    try:
        last = float(LAST_SYNC.read_text().strip())
    except ValueError:
        return False
    return (time.time() - last) < THROTTLE_SECONDS


def sync_fork():
    """Fetch + merge the fork's upstream. Returns True if anything changed."""
    manifest = json.loads(MANIFEST.read_text())["fork"]
    remote = manifest["upstreamRemote"]
    branch = manifest["branch"]

    run(["git", "fetch", remote])
    local_sha = run(["git", "rev-parse", branch]).stdout.strip()
    upstream_sha = run(["git", "rev-parse", f"{remote}/{branch}"]).stdout.strip()
    if local_sha == upstream_sha:
        log("fork: already up to date with upstream")
        return False

    merge = run(["git", "merge", f"{remote}/{branch}", "--no-edit"], check=False)
    if merge.returncode != 0:
        run(["git", "merge", "--abort"], check=False)
        raise RuntimeError(f"fork merge conflict against {remote}/{branch}, aborted:\n{merge.stdout}\n{merge.stderr}")
    log(f"fork: merged {remote}/{branch} ({local_sha[:7]} -> {upstream_sha[:7]})")
    return True


def sync_vendored_skill(entry):
    """Diff a fresh shallow clone of entry's source repo against the local
    copy and update it. Returns True if anything changed."""
    skill = entry["skill"]
    src_url = entry["sourceUrl"]
    branch = entry["branch"]
    src_subpath = entry["sourcePathInUpstream"]
    local_path = REPO / entry["localPath"]
    preserve = set(entry.get("preserveFiles", []))

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        clone = run(["git", "clone", "--depth", "1", "--branch", branch, src_url, str(tmp)], check=False)
        if clone.returncode != 0:
            log(f"vendored skill '{skill}': could not clone {src_url}, skipping this run\n{clone.stderr}")
            return False

        src_dir = tmp / src_subpath
        if not src_dir.exists():
            log(f"vendored skill '{skill}': expected path '{src_subpath}' not found upstream, skipping")
            return False

        changed = False
        for item in src_dir.rglob("*"):
            if item.is_dir():
                continue
            rel = item.relative_to(src_dir)
            if str(rel) in preserve or rel.name in preserve:
                continue
            dest = local_path / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            if not dest.exists() or dest.read_bytes() != item.read_bytes():
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, dest)
                changed = True

    if changed:
        log(f"vendored skill '{skill}': updated from {src_url}@{branch}")
    else:
        log(f"vendored skill '{skill}': already up to date")
    return changed


def main():
    if BLOCKED.exists():
        log(f"sync is blocked, see {BLOCKED} -- delete it after manual review to re-enable")
        return

    if throttled():
        log("checked recently, skipping (throttle)")
        return

    LAST_SYNC.write_text(str(time.time()))

    status = run(["git", "status", "--porcelain"]).stdout.strip()
    if status:
        log("working tree not clean, skipping auto-sync this run (avoid touching in-progress local changes)")
        return

    manifest = json.loads(MANIFEST.read_text())
    any_changes = False

    try:
        if sync_fork():
            any_changes = True

        for entry in manifest.get("vendoredSkills", []):
            if sync_vendored_skill(entry):
                any_changes = True
    except RuntimeError as e:
        BLOCKED.write_text(str(e))
        log(f"BLOCKED: {e}")
        return

    if not any_changes:
        log("nothing to sync")
        return

    # Stage any vendored-skill file changes (fork merge is already committed by git merge).
    run(["git", "add", "-A"])
    staged = run(["git", "status", "--porcelain"]).stdout.strip()
    if staged:
        run(["git", "commit", "-m", "chore: sync vendored skill(s) from upstream (auto)"])

    validate = run(["bash", "validate-skills.sh"], check=False)
    if validate.returncode != 0:
        BLOCKED.write_text(f"validate-skills.sh failed after sync:\n{validate.stdout}\n{validate.stderr}")
        log("validation FAILED after sync -- committed locally but NOT pushed, see .sync-blocked")
        return

    push = run(["git", "push", "origin", "main"], check=False)
    if push.returncode != 0:
        BLOCKED.write_text(f"git push failed (likely diverged from origin, needs manual review):\n{push.stdout}\n{push.stderr}")
        log("push FAILED -- see .sync-blocked")
        return

    log("synced and pushed to origin/main")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log(f"unexpected error, not pushing anything: {e}")
        sys.exit(0)  # never fail the session-start hook chain
