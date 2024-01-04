from pytube import YouTube


def runner():
    link = input("Enter Link ")
    yt = YouTube(link)
    vid = yt.streams.get_highest_resolution()
    vid.download()
    print("done")

runner()