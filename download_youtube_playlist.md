**Step1:** Try this first
```python
from pytube import Playlist

link = input("Enter YouTube Playlist URL: ")

yt_playlist = Playlist(link)
path = "D:\VS_Code\Coding Playground\YT_video_downloader\singger"

i = 1
for video in yt_playlist.videos:
    # Download Normally
    # video.streams.get_lowest_resolution().download(output_path=path)
    # Download videos in series
    video.streams.get_lowest_resolution().download(output_path=path, filename=str(i)+" "+video.title+".mp4")
    print("Video Downloaded: ", video.title)
    i=i+1

print("\nAll videos are downloaded.")
```

**If Step1 fails** 

**a:** Go to *https://playlist.downloader.is/*. Paste youtube playlist link. It will create a downloadable link for files. Save them in text file.

**b:** Put these in wget using below python script
```python
import re
import numpy as np
import wget
import os,sys
urlist=sys.argv[1]
Lines = open(urlist, 'r').readlines()

for line in Lines:
    url,name=line.strip().split("=Lecture")[0]+"=Lecture",str(line.strip().split("=Lecture")[1:]).replace(" ","")[1:-2]
    wget.download(url,out=name)
```
**c** Find Missed url in **Step a**
```python

#These url you have to donwload yourself....since there url is not there in file containing downloadable_urls


import re
import numpy as np
file1 = open('download_url.txt', 'r')
Lines = file1.readlines()

def sort_list(list1, list2):
    zipped_pairs = zip(list2, list1)
    z = [x for _, x in sorted(zipped_pairs)]
    return z


name_dict=[]
for line in Lines:
    name=float(str(line.strip().split("=Lecture")[1:]).replace(" ","")[1:-2].split("—")[0][1:])
    name_dict.append(name)
Lines=sort_list(Lines,name_dict)

count = 0
missing=0
missing_list=[]
probable_missing_list=[]
prev_vno=1.0
for line in Lines:
    count += 1
    url,name=line.strip().split("=Lecture")[0],str(line.strip().split("=Lecture")[1:]).replace(" ","")[1:-2]
    vno=float(name.split("—")[0][1:])
    #print(count,vno)
    if (np.abs((vno-prev_vno)-0.1)<0.01):
        pass
    elif (((vno-prev_vno)-0.2)<0.05):
        missing+=1
        missing_list.append(float("%0.1f"%(vno/2.+prev_vno/2.)))
    else:
        probable_missing_list.append(prev_vno)
        pass
    prev_vno=vno
print("Missing elements: ",missing_list)
print("Check these are last videos of chapter: ", probable_missing_list)
```
