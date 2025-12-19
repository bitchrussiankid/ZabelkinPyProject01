colors = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF",
    "yellow": "FFFF00",
    "black": "#000000"  
    }

yellowColor = colors.pop("yellow")
del colors["black"]

print(colors)
print(yellowColor)