from pytube import YouTube
import os
import wget

url = YouTube(str(input("What Is The URL?"))).thumbnail_url
path = str(os.getcwd()) + "\downloads"

print("Downloading")
wget.download(url, path)