from __future__ import unicode_literals
import yt_dlp as youtube_dl
import os


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    print("hook", d["status"])
    if d["status"] == "finished":
        print("Done downloading, now converting ...")


ydl_opts = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
    "logger": MyLogger(),
    "outtmpl": "/tmp/audio",  # Set the output filename directly
    "progress_hooks": [my_hook],
}


def lambda_handler(event, context):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        # Store the current working directory
        original_cwd = os.getcwd()
        # ydl.download(["https://www.youtube.com/watch?v=suwPBof3-DE"])
        try:
            # Change the working directory to /tmp (Lambda only allows writes to /tmp)
            # os.chdir("/tmp")

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(["https://www.youtube.com/watch?v=suwPBof3-DE"])
        finally:
            # Change the working directory back to the original
            # os.chdir(original_cwd)
            pass

    # https://youtu.be/JO5Vc3GcF4s
    # https://youtu.be/suwPBof3-DE


lambda_handler(None, None)
