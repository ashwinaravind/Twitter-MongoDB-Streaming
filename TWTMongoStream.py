import json
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pymongo import MongoClient
import datetime
from tweepy.error import TweepError, RateLimitError
class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        post = json.loads(data)
        posts = db.posts
        post_id = posts.insert_one(post).inserted_id
        db.collection_names(include_system_collections=False)
        print posts.find_one()
        return True
    def on_error(self, status):
        print(status)
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRECT'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.me()
print('CONNECTING  USER : ' + user.name)
l = StdOutListener()
client = MongoClient("YOUR_MONGODB_URL")
db = client["YOUR_MONGO_DB_USERNAME"]
stream = Stream(auth, l)
stream.filter(track=["SEARCH CRITERIA"])
