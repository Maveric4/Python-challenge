
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

diff = ord('q') - ord('o')
print(diff)
new_text = ""
for letter in text:
    if letter is " ":
        new_letter = " "
    elif letter is 'y':
        new_letter = 'a'
    elif letter is 'z':
        new_letter = 'b'
    elif letter == '.' or letter == '\'' or letter == '(' or letter == ')':
        new_letter = letter
    else:
        new_letter = chr(ord(letter) + diff)
    new_text += new_letter

print(new_text)


# print(text.maketrans())
intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = "".maketrans(intab, outtab)

print("map".translate(trantab))


