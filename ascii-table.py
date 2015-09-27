__author__ = 'Shane'
# displays an ASCII table for the characters with codes between 32 and 126


print("ASCII Code    Character")
for i in range(32, 127):
    if i % 4 == 0:
        print(" ")
    if i < 100:
        print("   ", i, "          ", chr(i))
    else:
        print("  ", i, "          ", chr(i))
