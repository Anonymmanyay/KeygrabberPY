import keyboard
import os

# Ensure that the output file is created in a safe location
output_dir = os.path.expanduser("~/Desktop")
output_file = os.path.join(output_dir, "KeyRecorder.txt")

with open(output_file, "a") as file:
    print(f"Press 'Esc', to stop Recording!")

    while True:
        try:
            # Wait for a key press event
            key_event = keyboard.read_event(timeout=0.1)

            # Check if it is a key press event
            if key_event.event_type == keyboard.KEY_DOWN:
                # Get the name of the pressed key
                pressed_key = key_event.name

                # Special handling for space key
                if pressed_key == "space":
                    pressed_key = " "

                # Write the pressed key to the file
                file.write(pressed_key + "\n")
                file.flush()  # Ensure immediate writing

                # Check if the escape key was pressed
                if pressed_key == "esc":
                    print("Recording stopped.")
                    break

            # Ignore unsupported keys
        except KeyError:
            continue

        # Exit the loop if the user presses Ctrl+C
        except KeyboardInterrupt:
            break
