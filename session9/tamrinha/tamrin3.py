

def caps_and_smalls(text):
    up = 0
    low = 0
    for ch in text:
        if ch.isupper():
            up += 1
        elif ch.islower():
            low += 1
    return up, low


string = input("Enter your text: ")
up, low = caps_and_smalls(string)
print("Your text contains {} upper(s) and {} lower(s).".format(up, low))
