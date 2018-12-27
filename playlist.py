# Import modules
from pytube import YouTube
from bs4 import BeautifulSoup
import requests
import io

def download_list(url_list):
    # Download videos in url playlist received 
    for url in url_list:
        # Url being downloaded
        print( url )
        download_video( url, path)
    
def download_video(url, path):
    # Download 
    try:
        yt = YouTube(url)
        try:
            # Download best resolution of youtube video
            yt.streams.filter(progressive=True).order_by('resolution').desc().first().download(path)
        except:
            print("Error in downloading")
    except:
        print("Unable to start download")
    
# Gets the urls of videos in html link
def get_urls(link):
    # List variable
    mlist = []
    # Get html as response
    url_doc = requests.get(link).text
    # Create soup
    soup = BeautifulSoup(url_doc, 'html.parser')
    # Get all video rows
    trs = soup.select('tr.pl-video')

    print("Parsing urls:")
    # Get link from each row
    for row in trs:
        url = 'https://www.youtube.com' + row.a['href']
        mlist.append(url)
        print( url )
        # Print line of 80 dashes
        print('-' * 80)
    
    print('-' *80 +'\nEnd')
    return mlist


# Path to save
#path = input( "Gimme path to save in: " )

# List or video
download_type = input( "1 for single :: 2 for playlist")

if( download_type== "1" ):
    # Single link download
    url = input("Gimme video url:")
    download_video( url, path )
else:
    # Playlist link
    link = input( "Gimme playlist link: " )
    # Set up soup
    url_list = get_urls( link )
    # Bulk Download
    download_list( url_list )




