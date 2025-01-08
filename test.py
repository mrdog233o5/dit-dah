from pynput import keyboard

# The event listener will be running in this block
with keyboard.Events() as events:
    for event in events:
        if type(event) == keyboard.Events.Press:
            print("press")
        else:
            print("release")

print("nigga")