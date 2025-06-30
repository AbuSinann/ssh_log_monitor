![SSH Log Monitor + Telegram Alerts](assets/thumbnail.png)

# 🛡️ SSH Log Monitor + Telegram Alerts

**A lightweight Python security tool** that monitors your Linux SSH logs (`/var/log/auth.log`) and instantly sends alerts to your Telegram bot when suspicious login attempts are detected — such as brute-force attacks or repeated failed passwords.

---

## 🚀 Why This Project?

SSH brute force attacks are one of the most common intrusion methods on public Linux servers. This tool helps you:
- Monitor SSH logs in real time
- Get alerts before attackers succeed
- Automate your security workflows
- Practice log parsing, automation, and alerting — all key cybersecurity skills

---

## 🧩 Features

- 🔍 Monitors `auth.log` for failed SSH login attempts
- 📲 Sends real-time Telegram alerts with IP and log details
- 🧠 Designed to be simple, portable, and fast
- 🔐 Optional IP auto-blocking with `iptables`
- ⚙️ Easy to run manually, via cron, or as a systemd service

---

## 📂 Project Structure
```
ssh-log-monitor-telegram/
 ├── monitor.py           # Main scripts 
 ├── config.json          # Telegram bot token + chat ID (template)
 ├── requirements.txt     # Python dependencies
 ├── assets/
 │   └── thumbnail.png    # Project banner image
 └── README.md            # Documentation
```
---

## ⚙️ Setup Guide

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/AbuSinann/ssh-log-monitor.git
cd ssh-log-monitor-telegram
```
### 📦 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 🔑 3. Configure Your Telegram Bot

Create a Telegram bot via @BotFather and get your:

**- Bot token**

**- Chat ID (via @userinfobot or API)**


Then create `config.json`:

```json
{
  "telegram_bot_token": "YOUR_TELEGRAM_BOT_TOKEN",
  "telegram_chat_id": "YOUR_TELEGRAM_CHAT_ID",
  "log_path": "/var/log/auth.log"
}
```

> ✅ Note: This file is ignored by `.gitignore` for security.

---

### ▶️ 4. Run the Monitor

```bash
python3 monitor.py
```

You’ll get a Telegram message if any suspicious login attempts are detected.


---

## ⏱️ Automate with Cron

To check logs every 5 minutes:

```bash
crontab -e
```

Add:
```bash
*/5 * * * * /usr/bin/python3 /full/path/to/monitor.py
```

---

## 🛡️ Optional: Auto-Block IPs

If you want to automatically block suspicious IPs using `iptables`, uncomment the following line in `monitor.py`:

```python
# os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")
```

Use responsibly.

---

## 🖼️ Project Preview

---

## 👨‍💻 Built By

Abu Sinan
Cybersecurity & Automation Expert
🔗 Upwork Profile
🔗 LinkedIn Profile

---

## 🧠 Learning Outcomes

This project showcases skills in:

Python scripting for system log analysis

Regex and pattern matching

Working with the Telegram Bot API

Real-time alert automation

Cronjob setup for continuous monitoring

---

## 📄 License

MIT License — free to use, modify, and share with credit.