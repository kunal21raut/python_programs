from pytube import *
url="https://www.youtube.com/watch?v=o4cOy3GeRGc"
path_to_save_vid= 'C:\\Users\\my\\Desktop'

obj=YouTube(url)
strms=obj.streams.all()
for s in strms:
    print(s)
