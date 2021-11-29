link = "https://ipaudio3.club/wp-content/uploads/HHD/Dune/01.mp3"
import time
import requests

i = 1


def pullmp3(link,filename):
    doc = requests.get(link)
    with open(filename,'wb') as f:
        f.write(doc.content)



while i < 24: 
    if i < 10:
        num = "0" + str(i)
    else:
        num = str(i)
    print(num)
    print("https://ipaudio3.club/wp-content/uploads/HHD/Dune/{}.mp3".format(num))
    pullmp3("https://ipaudio3.club/wp-content/uploads/HHD/Dune/{}.mp3".format(num),str(num) + ".mp3")
    i += 1


