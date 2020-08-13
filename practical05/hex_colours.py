COLOUR_DIR = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "chocolate": "#d2691e", "DarkOrange": "#ff8c00",
              "DarkSalmon": "#e9967a", "firebrick": "#b22222", "goldenrod": "#daa520", "HotPink": "#ff69b4",
              "violet": "#ee82ee", "tan": "#d2b48c"}
print(COLOUR_DIR)

color = input("Enter Colour: ")
while color != "":
    if color in COLOUR_DIR:
        print(color, "is", COLOUR_DIR[color])
    else:
        print("Invalid color")
    color = input("Enter Colour: ")
