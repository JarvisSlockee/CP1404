COLOURS = {"aliceblue": "#f0f8ff", "aquamarine1": "#7fffd4", "cyan1": "#00ffff", "DarkOliveGreen1": "	#caff70",
           "darkgoldnrod1": "#ffb90f", "darkorchid1": "#bf3eff", "dodgerblue2": "#1c86ee", "firebrick1": "#ff3030",
           "lightblue1": "#bfefff", "plum": "#dda0dd"}

for i, j in COLOURS.items():
    print("Colour options are: {}".format(i))

colour = input("Enter colour name: ").lower()
while colour != "":
    if colour in COLOURS:
        print(colour, "hex code is", COLOURS[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour name: ").lower()
