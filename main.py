import tweepy, random, requests
from pytube import Playlist
from PIL import Image
from io import BytesIO
from config import api_key, api_secret, bearer_token, access_token, access_token_secret

'''
importing libraries
pip install tweepy
pip install pytube requests pillow
'''
def main():
    #initializing API
    client = tweepy.Client(
        bearer_token, 
        api_key, 
        api_secret, 
        access_token, 
        access_token_secret)

    #API initialization for Auth 1 API use
    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
    api = tweepy.API(auth)

    #Creating Playlist variable
    p = Playlist('https://www.youtube.com/playlist?list=PLh6Ws4Fpphfqr7VL72Q6HK5Ole9YI54hv')
    print("Loaded playlist.")
    playlistVideos = p.videos

    #choosing random video
    randomVideo = random.choice(playlistVideos)

    #getting video ID & link
    videoID = randomVideo.video_id
    link = randomVideo.watch_url

    #extracting thumbnail image
    thumbnail = f'https://img.youtube.com/vi/{videoID}/maxresdefault.jpg'
    response = requests.get(thumbnail)
    image = Image.open(BytesIO(response.content))

    #saving to bytesIO object
    image_io = BytesIO()
    image.save(image_io, "PNG")
    image_io.seek(0)
    #uploading thumbnail as media to call as parameter in create_tweet function
    media = api.media_upload(filename="thumbnail.png", file=image_io)

    #Removing text from video title
    ostTitle = randomVideo.title.replace('ブルーアーカイブ Blue Archive ', '')

    #creating tweet
    client.create_tweet(
        text=f'Today\'s OST of the day is: {ostTitle}\nLink: {link}', 
        media_ids=[media.media_id_string])

if __name__ == "__main__":
    main()