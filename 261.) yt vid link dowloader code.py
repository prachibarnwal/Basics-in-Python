from pytube import YouTube
def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("AN ERROR OCCURED")
    print("DOWNLOAD COMPLETED SUCCESSFULLY")
link = input("Enter the YouTube Video URL : ")
Download(link)

