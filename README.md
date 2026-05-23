# Red Team Security Assessment

A modular framework that models the phases of a red-team engagement in Python:
APT kill-chain simulation, a minimal command-and-control channel, an
exploit-launcher pattern, and automated reporting. Built as a portfolio project
to show how the pieces of an offensive workflow fit together.

> **Lab and authorized use only.** Every module here is a **simulation** - it
> executes nothing against real systems. The APT and exploit modules just return
> labelled "simulated" steps, and the C2 server is an in-memory string queue that
> runs no commands. Only ever use this (and any tooling like it) against systems
> you own or are explicitly authorized to test.

## Components

| Module | What it does |
|---|---|
| `apt/simulate_apt.py` | Returns the phases of an APT kill chain (initial access, priv-esc, lateral movement, exfiltration) as simulated steps. |
| `c2/c2_server.py` | Minimal Flask C2 server: `/add` queues a command, `/get` hands the next one to a polling agent, `/health` reports status. Stores strings only. |
| `c2/agent.py` | Simulated agent that beacons to the server and prints tasked commands (never executes them). |
| `exploits/exploit_example.py` | Exploit-launcher template showing the CLI/targeting interface; returns a simulated result. |
| `report/generate_report.py` | Writes a timestamped Markdown engagement report. |

## Install

```bash
pip install -r requirements.txt
```

## Run the simulation

```bash
python apt/simulate_apt.py --target 10.0.0.5
```

```
[+] [10.0.0.5] Initial access (simulated)
[+] [10.0.0.5] Privilege escalation (simulated)
[+] [10.0.0.5] Lateral movement (simulated)
[+] [10.0.0.5] Data exfiltration (simulated)
```

```bash
# C2: start the server, then beacon with the agent (in a second terminal)
python c2/c2_server.py                       # listens on :8080
python c2/agent.py --server http://localhost:8080 --iterations 3

python exploits/exploit_example.py --target 10.0.0.5
python report/generate_report.py             # writes report.md
```

Docker:

```bash
docker compose up --build
```

## Tests

```bash
pytest
```

Covers the APT simulation, the exploit-launcher result, report generation, and a
full C2 round trip (queue a command, beacon, receive it) plus graceful handling
of an unreachable server.

## Roadmap

- Lab-scoped exploit modules behind the launcher interface (isolated lab only).
- Authenticated, encrypted C2 transport and tasking history.
- Structured (JSON) reporting with MITRE ATT&CK technique mapping.
