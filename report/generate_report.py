"""Generate a Markdown engagement report from recorded activities."""
from __future__ import annotations

import argparse
import datetime

DEFAULT_ACTIVITIES = [
    "APT kill chain simulated",
    "Exploit module tested (simulated)",
    "C2 channel established (lab)",
]


def build_report(activities: list[str], when: str | None = None) -> str:
    when = when or datetime.datetime.now().isoformat(timespec="seconds")
    lines = ["# Red Team Engagement Report", "", f"Generated: {when}", "", "## Activities", ""]
    lines += [f"- {a}" for a in activities]
    return "\n".join(lines) + "\n"


def generate(path: str = "report.md", activities: list[str] | None = None) -> str:
    with open(path, "w") as f:
        f.write(build_report(activities or DEFAULT_ACTIVITIES))
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="report.md")
    args = parser.parse_args()
    print(f"[+] Report written to {generate(args.out)}")


if __name__ == "__main__":
    main()
