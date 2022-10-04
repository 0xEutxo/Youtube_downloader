from pytube import YouTube

#inser url of YT video inside ''
url = ''
video = YouTube(url)

print("video_title: ")

print(video.title)

print("download_video: ")

video = video.streams.get_highest_resolution()

#or video = video.streams.first()

#for stream in video.streams:
    #print(stream)

    #insert file path into () or leave blank for current dir download
video.download()
