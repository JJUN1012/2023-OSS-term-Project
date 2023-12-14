from asciimatics.renderers import FigletText

def aaprint():
    colors = [31, 33, 32, 36, 34, 35]  # Red, Yellow, Green, Cyan, Blue, Magenta
    rainbow_text = ""
    text = str(FigletText("SHOW ME THE HIGHWAY", font='small'))
    for i, char in enumerate(text):
        if char != "\n":
            rainbow_text += "\033[{}m".format(colors[i % len(colors)]) + char
        else:
            rainbow_text += char
    reset = "\033[0m"
    print(rainbow_text + reset)
if __name__ == "__main__":
    aaprint()