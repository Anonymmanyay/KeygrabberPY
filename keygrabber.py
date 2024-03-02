import keyboard

output_file = "tastenprotokoll.txt"

with open(output_file, "a") as file:
print("Drücke 'Esc', um die Aufnahme zu beenden.")

while True:
try:
# Warte auf einen Tastendruck
key_event = keyboard.read_event()

# Überprüfe, ob es ein Tasten-Druck-Ereignis ist
if key_event.event_type == keyboard.KEY_DOWN:
pressed_key = key_event.name

# Spezielle Behandlung für Leertaste
if pressed_key == "space":
pressed_key = " "

# Schreibe den gedrückten Schlüssel in die Datei
file.write(pressed_key + "\n")
file.flush() # Sofortiges Schreiben sicherstellen

# Überprüfe, ob die Escape-Taste gedrückt wurde
if pressed_key == "esc":
print("Aufnahme beendet.")
break

except KeyboardInterrupt:
# Breche die Schleife ab, wenn der Benutzer Strg+C drückt
break
