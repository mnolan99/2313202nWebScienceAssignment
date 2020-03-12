# WebScienceAE - 2313202n

import pymongo
from pymongo import Connection
import json
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime

# Connect to MongoDB using the localhost on port 27017
# This creates a database with the name WebScienceAE, and
# a collection name of Football3.
connection = Connection('localhost', 27017)
db = connection.WebScienceAE
db.ClimateChange.ensure_index("id", unique=True, dropDups=True)
collection = db.Football3      

# Track keywords and hashtags from tweets that are coming in live.
keywords = ['VAR', '#VAR', 'Football', '#Football']

# Only crawl tweets that are written in english
language = ['en']

# Twitter developer portal keys (These have been removed and can be replaced with the markers keys).
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Collect tweets from the twitter steam API and store their details in the MongoDB database
class StdOutListener(StreamListener):

    def on_data(self, data):

        # Load each tweet in
        tweets = json.loads(data)

        # Get data from the tweet and store in the database
        tweetID = tweets['id_str']  # Print the Tweet ID
        username = tweets['user']['screen_name']  # Print username of the Tweet author
        followers = tweets['user']['followers_count']  # Print no of people who follow tweet author
        text = tweets['text']  # Print the text of the tweet
        hashtags = tweets['entities']['hashtags']  # Hashtags of the Tweet
        timestamp = tweets['created_at']  # Tweet timestamp
        language = tweets['lang']  # Tweet language

        # Convert timestamp so that it can be read by MongoDB
        created = datetime.datetime.strptime(timestamp, '%a %b %d %H:%M:%S +0000 %Y')

        # Add all tweet information into tweet variable which is stored in the database
        tweet = {'id':tweetID, 'username':username, 'followers':followers, 'text':text, 'hashtags':hashtags, 'language':language, 'created':created}

        # Save the data to MongoDB
        collection.save(tweet)

    # If an error occurs, print to console
    def on_error(self, status):
        print (status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=keywords, languages=language)
