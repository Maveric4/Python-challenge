
from PIL import Image
import re
img = Image.open("oxygen.png")
row = [img.getpixel((x, img.height / 2)) for x in range(img.width)]
# print(row)

row = row[::7]
# print(row)
ords = [r for r, g, b, a in row]
txt = "".join(map(chr, ords))
print(txt)

nums = re.findall("\d+", txt)
print("Answer is: " + "".join(map(chr, map(int, nums))))