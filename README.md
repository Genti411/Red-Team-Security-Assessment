# Red Team Security Assessment

A modular, lab-only framework that models the phases of a red-team engagement in Python: APT simulation, a minimal command-and-control channel, an exploit-launcher pattern, and automated reporting. Built as a portfolio project to demonstrate how the pieces of an offensive workflow fit together. The modules are intentionally simple and meant for an isolated lab, not real-world use.

## Components

| Module | What it does |
|---|---|
| `apt/simulate_apt.py` | Scripted walkthrough of APT phases (privilege escalation, lateral movement, exfiltration), printed as simulated steps against a target you pass in. |
| `c2/c2_server.py` | Minimal HTTP command-and-control server (Flask) exposing `/add` to queue a command and `/get` for agents to poll. |
| `c2/agent.py` | Polling agent that beacons to the C2 server every few seconds and prints any queued command. Demonstrates the beacon pattern. |
| `exploits/exploit_example.py` | Exploit-launcher template showing the CLI/targeting pattern for adding real modules. |
| `report/generate_report.py` | Writes a timestamped Markdown engagement report (`report.md`). |

## Layout

```
Red-Team-Security-Assessment/
├── apt/simulate_apt.py
├── c2/c2_server.py
├── c2/agent.py
├── exploits/exploit_example.py
├── report/generate_report.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Run it

```bash
cd Red-Team-Security-Assessment
pip install -r requirements.txt

# C2: start the server, then run the agent in a second terminal
python c2/c2_server.py            # listens on :8080
python c2/agent.py

# Simulations and reporting
python apt/simulate_apt.py --target 10.0.0.5
python exploits/exploit_example.py --target 10.0.0.5
python report/generate_report.py
```

Docker:

```bash
cd Red-Team-Security-Assessment
docker compose up --build
```

## Requirements

Python 3, `flask`, `requests`.

## Roadmap

- Real (lab-scoped) exploit modules behind the launcher interface.
- Authenticated, encrypted C2 transport and tasking history.
- Structured (JSON) reporting with MITRE ATT&CK technique mapping.
