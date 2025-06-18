# Red Team Security Assessment Framework

A modular Python-based red teaming framework to simulate advanced persistent threats, conduct exploit testing, establish command and control, and automate post-exploitation reporting.

## Key Features
- APT simulation tools
- Custom exploit launcher
- Command and Control (C2) server & agent
- Social engineering payloads
- Auto-generated reports
- Dockerized lab-ready setup

## Quick Start

### Run APT Simulation
```bash
python apt/simulate_apt.py --target <target_ip>
```

### Launch C2 Server
```bash
python c2/c2_server.py
```

### Run Exploit (sample)
```bash
python exploits/exploit_example.py --target <target_ip>
```

### Generate Report
```bash
python report/generate_report.py
```

### Docker Setup
```bash
docker-compose up --build
```

