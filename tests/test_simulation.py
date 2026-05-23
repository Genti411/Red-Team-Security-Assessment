import importlib.util
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load(rel_path, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, rel_path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


apt = _load("apt/simulate_apt.py", "simulate_apt")
exploit = _load("exploits/exploit_example.py", "exploit_example")
report = _load("report/generate_report.py", "generate_report")


def test_simulate_returns_all_phases():
    steps = apt.simulate("10.0.0.5")
    assert len(steps) == len(apt.PHASES)
    assert all("10.0.0.5" in step for step in steps)


def test_launch_is_simulated_only():
    result = exploit.launch("10.0.0.5")
    assert result["status"] == "simulated"
    assert result["target"] == "10.0.0.5"


def test_report_contains_activities(tmp_path):
    path = tmp_path / "report.md"
    report.generate(str(path), ["did a thing", "did another thing"])
    text = path.read_text()
    assert "Red Team Engagement Report" in text
    assert "did a thing" in text and "did another thing" in text
