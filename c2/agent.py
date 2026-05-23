"""Simulated C2 agent (lab only): polls the server and prints tasked commands.

It does NOT execute anything - commands received from the server are only
printed, to demonstrate the beacon/polling pattern. Lab / authorized use only.
"""
from __future__ import annotations

import argparse
import time

import requests


def poll_once(server_url: str, timeout: float = 5.0) -> str:
    """Poll the C2 server once and return the tasked command (or 'noop')."""
    resp = requests.post(f"{server_url.rstrip('/')}/get", timeout=timeout)
    return resp.json().get("cmd", "noop")


def run(server_url: str, iterations: int | None = None, interval: float = 5.0) -> None:
    count = 0
    while iterations is None or count < iterations:
        try:
            cmd = poll_once(server_url)
            if cmd != "noop":
                print(f"[agent] tasked: {cmd} (not executed - simulation)")
        except requests.RequestException:
            print("[agent] server unreachable")
        count += 1
        if iterations is None or count < iterations:
            time.sleep(interval)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--server", default="http://localhost:8080")
    parser.add_argument("--iterations", type=int, default=None, help="stop after N polls")
    args = parser.parse_args()
    run(args.server, args.iterations)


if __name__ == "__main__":
    main()
