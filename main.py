import tweepy, random, requests
from pytube import Playlist
from PIL import Image
from io import BytesIO
from config import api_key, api_secret, bearer_token, access_token, access_token_secret

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

#Creating Playlist variable
p = Playlist('https://www.youtube.com/playlist?list=PLh6Ws4Fpphfqr7VL72Q6HK5Ole9YI54hv')
print("Loaded playlist.")
PlaylistVideos = p.videos

#choosing random video
randomVideo = random.choice(PlaylistVideos)

#getting url
link = randomVideo.watch_url

#saving thumbnail image
thumbnail = randomVideo.thumbnail_url
response = requests.get(thumbnail)
image = Image.open(BytesIO(response.content))
image.show()

#Removing text from video title
ostTitle = randomVideo.title.replace('ブルーアーカイブ Blue Archive ', '')

print(f'The OST chosen is: {ostTitle}')
print(f'The URL is: {link}')