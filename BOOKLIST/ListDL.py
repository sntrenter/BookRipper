link = "https://ipaudio6.com/wp-content/uploads/BOOKAUDIO/Big%20Short/{}.mp3"
import time
import requests
from Booklist import Booklist 
import re
from bs4 import BeautifulSoup
i = 1


def pullmp3(link,filename):
    mp3 = requests.get(link)
    if mp3.status_code == 200:
        with open(filename,'wb') as f:
            print("saving mp3")
            f.write(mp3.content)
    else:
        print("link doesn't exist")


#while i < 100:
#    if i < 10:
#        num = "0" + str(i)
#    else:
#        num = str(i)
#    #print(num)
#    print(link.format(num))
#    pullmp3(link.format(num),str(num) + ".mp3")
#    i += 1


def main():
    print("start")
    #mp3re = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)(.mp3)"
    for i in Booklist[:1]:
        print("============================")
        print(i)
        page = requests.get(i)
        soup = BeautifulSoup(page.text, 'html.parser')
        print(soup.title)
        links = soup.findAll('a', href=True)
        mp3s = [l for l in links if l['href'].endswith('.mp3')]
        mp3 = mp3s[0]#.split("\"")
        print(mp3.next)
        print()
        newlink = str(mp3.next)[:-6]
        print(newlink)
        j = 1
        while j < 100:
            if j < 10:
                num = "0" + str(j)
            else:
                num = str(j)
            #print(num)
            print(newlink+str(num)+".mp3")
            #pullmp3(link.format(num),str(num) + ".mp3")
            j += 1
        
main()