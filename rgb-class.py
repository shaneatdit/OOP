"""
Creates a class that represents an RGB color.

Calculates luminance using the following formula:
Y = 0.2126 R + 0.7152 G + 0.0722 B
"""


class RGB:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def luminance(self):
        self.luminance = 0.2126 * self.red + 0.7152 * self.green + 0.0722 * self.blue
        return self.luminance

    def __str__(self):
        lum = self.luminance()
        description = "Red: " + str(self.red) \
                      + ", green: " + str(self.green) \
                      + ", blue: " + str(self.blue) \
                      + "\nLuminance: " + str(lum)
        return description


def main():
    black = RGB(0, 0, 0)
    print(black)
    
    white = RGB(255, 255, 255)
    print(white)

main()
