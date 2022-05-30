link = "https://ipaudio6.com/wp-content/uploads/BAY/PRIME/Gulag%20Archipelago/{}.mp3"
import time
import requests

i = 1


def pullmp3(link,filename):
    mp3 = requests.get(link)
    if mp3.status_code == 200:
        with open(filename,'wb') as f:
            print("saving mp3")
            f.write(mp3.content)
    else:
        print("link doesn't exist")


while i < 100:
    if i < 10:
        num = "0" + str(i)
    else:
        num = str(i)
    #print(num)
    print(link.format(num))
    pullmp3(link.format(num),str(num) + ".mp3")
    i += 1


