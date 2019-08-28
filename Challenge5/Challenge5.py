from urllib import request

# site_obj = request.urlopen(url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")
site_obj = request.urlopen(url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022")
cnt = 0
while True:
    cnt += 1
    web_content = site_obj.read().decode()
    try:
        code = int(web_content.split(" ")[-1])
    except Exception as e:
        print("Answer is: ")
        print(web_content)
        break
    print(str(cnt) + ": " + web_content)
    site_obj = request.urlopen(url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(code))



