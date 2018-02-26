formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
#Taking formatter string on line 1, calls its format function, fourmat four arguments which match the four {}
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
        "Try your",
        "Own text here",
        "Maybe a poem",
        "Or a song about fear"
))
