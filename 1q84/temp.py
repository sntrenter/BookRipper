link = "https://ipaudio6.com/wp-content/uploads/BOOKAUDIO/1Q84/01.mp3?_=1"
import time

import requests

i = 1


def pullmp3(link,filename):
    doc = requests.get(link)
    with open(filename,'wb') as f:
        f.write(doc.content)



while i < 49: 
    if i < 10:
        num = "0" + str(i)
    else:
        num = i
    mod = int(num)%7
    if mod == 0:
        mod = 7
    
    print(num,mod)
    pullmp3("https://ipaudio6.com/wp-content/uploads/BOOKAUDIO/1Q84/{}.mp3?_={}".format(num,mod),str(num) + ".mp3")
    i += 1
    #time.sleep(1)




