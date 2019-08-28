
cnt = 0
with open("90052.txt", 'r') as file:
    file_content = file.read()
    code = int(file_content.split(" ")[-1])

while True:
    with open(str(code) + ".txt", 'r') as file:
        cnt += 1
        file_content = file.read()
        try:
            code = int(file_content.split(" ")[-1])
        except Exception as e:
            print("Answer is: ")
            print(file_content)
            break
        print(str(cnt) + ": " + file_content)


import zipfile
import re
comments = []
f = zipfile.ZipFile("channel.zip")
num = '90052'
while True:
    content = f.read(num + ".txt").decode("utf-8")
    comments.append(f.getinfo(num + ".txt").comment.decode("utf-8"))
    match = re.search("Next nothing is (\d+)", content)
    if match == None:
        break
    num = match.group(1)

print("".join(comments))