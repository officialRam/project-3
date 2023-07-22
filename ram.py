from pytube import YouTube
yt=YouTube("https://www.youtube.com/watch?v=Qwm6BSGrOq0&list=RDQwm6BSGrOq0&start_radio=1")
print(yt.title)
stream=yt.streams.first()
stream.download()