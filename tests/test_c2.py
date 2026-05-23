import importlib.util
import os
import threading

import pytest
import requests
from werkzeug.serving import make_server

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load(rel_path, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, rel_path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


c2_server = _load("c2/c2_server.py", "c2_server")
agent = _load("c2/agent.py", "c2_agent")


@pytest.fixture(scope="module")
def server():
    srv = make_server("127.0.0.1", 0, c2_server.create_app())
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{srv.server_port}"
    srv.shutdown()


def test_queue_roundtrip_via_agent(server):
    requests.post(f"{server}/add", json={"cmd": "whoami"})
    assert agent.poll_once(server) == "whoami"


def test_empty_queue_returns_noop(server):
    while agent.poll_once(server) != "noop":  # drain anything queued
        pass
    assert agent.poll_once(server) == "noop"


def test_add_without_cmd_returns_400(server):
    assert requests.post(f"{server}/add", json={}).status_code == 400


def test_agent_handles_unreachable_server():
    # Nothing listening; run one iteration and confirm it doesn't raise.
    agent.run("http://127.0.0.1:1", iterations=1, interval=0)
