import os
from glob import glob
import re
from pydub import AudioSegment

pathToFolder = "murikami\Haruki Murakami - Norwegian Wood/*/"


def SubDirPath (d):
    return filter(os.path.isdir, [os.path.join(d,f) for f in os.listdir(d)])

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


def main():
    print("start")

    #get folders or "discs"
    subdir = natural_sort(glob(pathToFolder,recursive=True))
    #get mp3s
    discnum = 1
    for i in subdir:
        print(i)
        mp3s = natural_sort(glob(i + "*.mp3",recursive=True))
        mp3s = [os.path.abspath(e) for e in mp3s]
        #combine mp3s https://stackoverflow.com/questions/2952309/python-library-to-split-and-join-mp3-files
        mp3List = []
        for j in mp3s:
            print(j)
            #print(os.path.exists(j))
            mp3List.append(AudioSegment.from_mp3(j))
        #print(mp3List)
        full = sum(mp3List)
        full.export("Disc_"+ str(discnum) +".mp3",format="mp3")
        discnum += 1
        #break;


    print("end")


main()