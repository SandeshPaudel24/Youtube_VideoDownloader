from django.shortcuts import render
from pytube import *
from pytube import YouTube

# can use callback also frm callback.py


def download_youtube_video(url):
    try:
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download()
        return "Video downloaded successfully!"
    except Exception as e:
        return f"Error: {e}"


def downloader(request):
    if request.method == "POST":
        link = request.POST["link"]
        message = download_youtube_video(link)
        return render(request, "view.html", {"message": message})
    else:
        return render(request, "view.html")
