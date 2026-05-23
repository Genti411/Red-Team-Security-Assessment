"""Minimal command-and-control server for the LAB SIMULATION.

An in-memory task queue: operators POST commands to /add and simulated agents
poll /get. It executes nothing - it only stores strings and hands them back, to
demonstrate the C2 beacon/tasking pattern. Lab / authorized use only.
"""
from __future__ import annotations

from flask import Flask, jsonify, request


def create_app() -> Flask:
    app = Flask(__name__)
    queue: list[str] = []

    @app.get("/health")
    def health():
        return jsonify(status="ok", queued=len(queue))

    @app.post("/add")
    def add_command():
        cmd = (request.get_json(force=True) or {}).get("cmd")
        if not cmd:
            return jsonify(error="missing 'cmd'"), 400
        queue.append(cmd)
        return jsonify(status="queued", queued=len(queue))

    @app.post("/get")
    def get_command():
        return jsonify(cmd=queue.pop(0) if queue else "noop")

    return app


if __name__ == "__main__":
    create_app().run(port=8080)
