class Color:
    black = "black"
    blue = "blue"
    dark_blue = "dark blue"
    yellow = "yellow"
    red = "red"
    green = "green"


tile_color = {
    "d": Color.black,
    "b": Color.blue,
    "g": Color.dark_blue,
    "y": Color.yellow,
    "r": Color.red
}


tile_color_reverse = {
    Color.black: "d",
    Color.blue: "b",
    Color.dark_blue: "g",
    Color.yellow: "y",
    Color.red: "r"
}