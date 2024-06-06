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
    client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

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
    media = client.upload_media(media=image_io, media_category="tweet_image")

    #Removing text from video title
    ostTitle = randomVideo.title.replace('ブルーアーカイブ Blue Archive ', '')

    #creating tweet
    client.create_tweet(text=f'Today\'s OST is: {ostTitle}\n{link}', media_ids=[media.media_id])

if __name__ == "__main__":
    main()