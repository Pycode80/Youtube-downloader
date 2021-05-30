from art import *
from pytube import YouTube
from pytube import Playlist
import os



os.chdir("C:/Users/Illiès/Desktop")

Art = text2art("Youtube   Downloader")
print(Art)

choix = input("""
1. Download A Video
2. Download A Playlist

Make a choice : """)

if choix == "1":
    genre = input("""\n1. Download the Video and the audio
2. Download only the audio\n
Make a choice :  """)
    if genre == "1":
        url = input("Enter your url : ")
        print("Loading ...")
        YouTube(url).streams.first().download()
        print("Download complete")
        quit


    if genre == "2":
        url = input("\nEnter your url : ")
        print("Loading ...")
        yt=YouTube(url)
        t = yt.streams.filter(only_audio=True)
        out_file = t[0].download()
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print("Download complete")
        quit
    else:
        print("You are crazy, you asked for an option that does not exist.")


if choix =="2":
    genre = input("""\n1. Download the Video and the audio
2. Download only the audio\n
Make a choice :  """)
    if genre == "1":
        url = input("Enter your url : ")
        print("Loading ...")
        playlist = Playlist(url)
        os.mkdir("Playlist")
        os.chdir("C:/Users/Illiès/Desktop/Playlist")
        print('Number of videos in playlist: %s' % len(playlist.video_urls))
        playlist.download_all()
        print("Download complete")
        quit


    if genre == "2":
        url = input("\nEnter your url : ")
        print("Loading ...")
        pl = Playlist(url)
        os.mkdir("Playlist")
        os.chdir("C:/Users/Illiès/Desktop/Playlist")
        for yt in pl.videos:
            out_file = yt.streams.filter(only_audio=True).first().download()
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
        print("Download complete")
        quit
    else:
        print("You are crazy, you asked for an option that does not exist.")
        quit

else:
    print("You are crazy, you asked for an option that does not exist.")
    quit


