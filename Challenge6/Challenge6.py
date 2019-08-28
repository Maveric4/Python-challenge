import pickle
from urllib.request import urlopen

pic = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))
print(pic)

print("Answer is:")
for line in pic:
        print("".join([k * v for k, v in line]))
