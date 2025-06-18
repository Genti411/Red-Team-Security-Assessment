import datetime

def generate():
    with open("report.md", "w") as f:
        f.write("# Red Team Report\n")
        f.write(f"Generated: {datetime.datetime.now()}\n")
        f.write("\n## Activities Performed\n- APT Simulated\n- Exploits Tested\n- C2 Established\n")
    print("[+] Report generated: report.md")

if __name__ == "__main__":
    generate()
