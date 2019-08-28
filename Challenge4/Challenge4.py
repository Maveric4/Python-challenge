import re

with open("letters.txt", 'r') as file:
    text = file.read()

matches = re.findall("[a-z]+[A-Z][A-Z][A-Z][(a-z){.+}][A-Z][A-Z][A-Z][a-z]+", text)
word = ''
for match in matches:
    letter = re.match("[a-z]+[A-Z][A-Z][A-Z]([(a-z){.+}])[A-Z][A-Z][A-Z][a-z]+", match).group(1)
    word += letter
print(word)
