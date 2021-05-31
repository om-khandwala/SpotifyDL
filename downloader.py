import time
from pytube import YouTube
import os


def download(link, song_name):
    try:
        yt = YouTube(link)
        try:
            audio = yt.streams.filter(only_audio=True).first()
            audio.download(filename=song_name, output_path='./audio')
            time.sleep(1)
            os.rename(f'./audio/{song_name}.mp4', f'./audio/{song_name}.mp3')

            return yt.streams.filter(only_audio=True).first(), 'downloaded'
        except:

            return None, 'download failed'
    except:
        print("no internet")
