i = 0
#placeholder list
notes = ["G3", "A3", "B3", "C3", "B3", "C3"]
frequencies = {
    "C3":130.81,
    "D3":146.00,
    "E3":164.00,
    "F3":174.00,
    "G3":196.00,
    "A3":220.00,
    "B3":246.00,
}

for note in notes:
    print(frequencies[note])
 