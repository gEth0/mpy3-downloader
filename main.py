try:
    from pytubefix import YouTube
    import json
    import music_tag
    import urllib.request
    from termcolor import colored
    import os
except:
    print("Make sure you have installed all the dependences needed ----> pip install -r requirements.txt")
with open("links.json","r") as f:
    links = json.load(f)["links"]

def downloadAudio(url):
    yt = YouTube(url)
    ys = yt.streams.get_audio_only()
    path = f"./songs/{yt.author}"
    ys.download(output_path=path,mp3=True)
    print(colored(f"\n{yt.title} : DOWNLOADED\n","green"))
    return yt

def setSongTag(song):
    try:
        with open(coverPath, 'rb') as img_in:
                song['artwork'] = img_in.read()
        with open(coverPath, 'rb') as img_in:
            song.append_tag('artwork', img_in.read())

            song["title"] = yt.title
            song["artist"] = yt.author
            
            song.save()
        print(colored("done\n","green"))
    except:
        print(colored(f"some errors occured while setting metadata","red"))

print(colored("\nStarting mpy3-downloader\n-----------------INFO-----------------\nThis script will download mp3 audio from the links given in the link.json file,then it will add author, title and the cover as well to the metadata","blue"))

for link in links:
    try:
        yt = downloadAudio(link)

        completePath = f"./songs/{yt.author}/{yt.title}.mp3"

        print(colored("start adding metadata","green"))

        thUrl = yt.thumbnail_url
        coverPath = urllib.request.urlretrieve(thUrl)[0]
        
        song = music_tag.load_file(completePath)
        setSongTag(song)

        os.remove(coverPath)

        if(links[len(links)-1] != link):
            print("------------------NEXT------------------")
    except :
        print(colored(f"some errors occured ---> skipping to the next link","red"))