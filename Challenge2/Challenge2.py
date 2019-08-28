import string

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
diff = ord('q') - ord('o')
print(diff)
new_text = ""
for letter in text:
    if letter == " ":
        new_letter = " "
    elif letter == 'y':
        new_letter = 'a'
    elif letter == 'z':
        new_letter = 'b'
    elif letter in string.punctuation:
        new_letter = letter
    else:
        new_letter = chr(ord(letter) + diff)
    new_text += new_letter

print(new_text)

# Solving puzzle
intab = string.ascii_lowercase
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = "".maketrans(intab, outtab)
print("map".translate(trantab))



