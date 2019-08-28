
text = ""
with open("mess.txt", 'r') as file:
    for sign in file.read():
        if sign.isalpha():
            text += sign

print(text)