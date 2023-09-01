from pytube import YouTube
print("PRESS 1 FOR VIDEO")
print("PRESS 2 FOR AUDIO")
choice=int(input("Enter you choice:- "))
if choice==1:
    link = input("Enter the youtube link:-")
    ytube = YouTube(link)
    print("We are downloading your video " + ytube.title)
    video = ytube.streams.filter(progressive=True)
    vid = enumerate(video)
    for i in vid:
        print(i)
    ind = int(input("Enter the index of resolution in which you want to download video :-  "))
    video[ind].download()
elif choice==2:
    audio_link = input("Enter the youtube link whose audio you want to download :-")
    youtube = YouTube(audio_link)
    print("We are downloading your audio of  " + youtube.title)
    audio = youtube.streams.filter(only_audio=True)
    vid2 = enumerate(audio)
    for i in vid2:
        print(i)
    ind = int(input("Enter the index of resolution in which you want to download audio :-  "))
    audio[ind].download()
else:
    print("Invalid Choice :(")

print("Successfully Downloaded :)")