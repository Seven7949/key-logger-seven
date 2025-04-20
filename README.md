# key-logger-seven

# 🕵️‍♂️ Basic Keylogger (Educational Use Only)

A Python-based keylogger that logs keystrokes into a hidden log file. Intended **only** for ethical testing, awareness, and educational demonstrations.

---

## ⚠️ WARNING

This tool is **NOT** to be used for malicious purposes.
Use only on systems you own or have explicit permission to test.

---

## 🚀 Features

- Logs every keystroke to a time-stamped hidden log file
- Captures both printable and special keys (Shift, Enter, etc.)
- Can be extended to email or alert logs

---

## 🧠 How It Works

- Uses `pynput` to listen to global keypress events
- Writes keys into a timestamped log file under `.logs/` directory

---

## 🛠️ Requirements

```bash
pip install pynput
