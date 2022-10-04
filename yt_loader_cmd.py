from pytube import YouTube
from sys import argv

url = argv[1]
video = YouTube(url)

print("video_title: ")

print(video.title)

print("download_video: ")

video = video.streams.get_highest_resolution()

#or video = video.streams.first()

#for stream in video.streams:
    #print(stream)

    #insert file path into () or leave blank for current dir download
video.download('P:\Car Crash Footage')
