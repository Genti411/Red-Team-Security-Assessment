import time, requests

while True:
    try:
        r = requests.post('http://localhost:8080/get')
        cmd = r.json()['cmd']
        if cmd != "noop":
            print(f"[Agent] Executing: {cmd}")
    except:
        print("[Agent] Failed to connect")
    time.sleep(5)
