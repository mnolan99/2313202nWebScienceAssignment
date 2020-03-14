# WebScienceAE - 2313202n

from TwitterSearch import *

try:
    t = TwitterSearchOrder() # create an object of TwitterSearch
    t.set_keywords(['Football', 'VAR']) # Search for keywords of football and VAR
    t.set_language('en') # Only search for English tweets

    # Add Twitter Developer keys to authenticate access
    keys = TwitterSearch(
        consumer_key = '',
        consumer_secret = '',
        access_token = '',
        access_token_secret = ''
     )

    # For each tweet, print out the tweet data
    for tweet in keys.search_tweets_iterable(t):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

# Handle any errors that may occur
except TwitterSearchException as e:
    print(e)
