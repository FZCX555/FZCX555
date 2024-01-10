#import youtube_search_python
from pytube import YouTube
import os

print()

URL = input('url : ')
yt = YouTube(URL)


try:
	print("\nmengdonlot akwokwo..... \n")
	yt = YouTube(URL)
	yt.streams.filter(only_audio=True)[-1].download(filename=yt.title+".mp3")
	#print("success")
	print("\nsukses su! \n")
	os.system("python3 ytmp3.py")

except:
	print("\nerror om.... \n")
	os.system("reboot")
	