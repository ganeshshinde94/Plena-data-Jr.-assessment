string = input("Enter your string here:")

def first_not_repeated_char(string):

    if not string:
        return

    frequency = [0] * 256

    for char in string:
        frequency[ord(char.lower())] += 1

    for char in string:
        if frequency[ord(char.lower())] == 1:
            return (char, frequency)


not_repeated_char, frequency = (first_not_repeated_char(string))
print(not_repeated_char)

not_repeated_chars = ""
repeated_chars = ""

for char in string:
    if frequency[ord(char.lower())]==1:
        not_repeated_chars+=char
    else:
        repeated_chars+=char
print(not_repeated_chars+repeated_chars)

