import re
import json
import requests

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

TOKEN = config["telegram_bot_token"]
CHAT_ID = config["telegram_chat_id"]
LOG_PATH = config["log_path"]

PATTERN = r"Failed password for.*from (\d+\.\d+\.\d+\.\d+)"

def read_last_lines(path, num_lines=100):
    with open(path, "r") as file:
        return file.readlines()[-num_lines:]

def send_alert(ip, line):
    message = f"⚠️ SSH Alert\nIP: {ip}\n\nLog: {line}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

def main():
    lines = read_last_lines(LOG_PATH)
    for line in lines:
        match = re.search(PATTERN, line)
        if match:
            ip = match.group(1)
            print(f"[!] Suspicious IP: {ip}")
            send_alert(ip, line)

if __name__ == "__main__":
    main()