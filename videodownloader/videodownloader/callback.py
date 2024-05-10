from pytube import YouTube


# link validator
def validate_link(link):
    try:
        YouTube(link)
        return True
    except Exception as e:
        print(f"{e}")
        return False


# for higher n lower resolution
def get_higher_resolution(video):
    try:
        return video.streams.get_highest_resolution()
    except Exception as e:
        print(f"{e}")
        return False


def get_lower_resolution(video):
    try:
        return video.streams.get_lowest_resolution()
    except Exception as e:
        print(f"{e}")
        return False


# for video download
def download(video):
    try:
        video.download()
        return True
    except Exception as e:
        print(f"{e}")
        return False
