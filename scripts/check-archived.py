#!/usr/bin/env python3
"""Flag GitHub repositories that are archived but still listed in the main list.

Unmaintained and archived projects belong in `archived.md`, not in `README.md`
(the Awesome guidelines ask that such items be kept out of the main list). Any
archived repo found in `README.md` is reported as an error (with a GitHub Actions
annotation) and makes the job fail; entries in `archived.md` are not checked, as
they are expected to be archived or dormant.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request

README = "README.md"
LINK_RE = re.compile(r"https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")

token = os.environ.get("GITHUB_TOKEN")


def api_archived(slug):
    """Return (archived_bool, error_str)."""
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "awesome-swarm-ci"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(f"https://api.github.com/repos/{slug}", headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp).get("archived", False), None
    except urllib.error.HTTPError as exc:
        return None, f"HTTP {exc.code}"
    except Exception as exc:  # noqa: BLE001 - report and continue
        return None, str(exc)


def collect_live_repos():
    """Map 'owner/repo' -> line number, for every repo linked in README.md."""
    live = {}
    with open(README, encoding="utf-8") as handle:
        for lineno, line in enumerate(handle, 1):
            for owner, repo in LINK_RE.findall(line):
                slug = f"{owner}/{repo.rstrip('/')}"
                live.setdefault(slug, lineno)
    return live


def main():
    live = collect_live_repos()
    problems = []
    for slug, lineno in sorted(live.items()):
        archived, err = api_archived(slug)
        if err:
            print(f"::warning file={README},line={lineno}::could not check {slug}: {err}")
        elif archived:
            problems.append(slug)
            print(
                f"::error file={README},line={lineno}::{slug} is archived on GitHub "
                f"but listed in README.md — move it to archived.md"
            )
        else:
            print(f"ok: {slug}")

    if problems:
        print(f"\n{len(problems)} archived repo(s) found in README.md.")
        return 1
    print("\nNo archived repos in README.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
