from TwitterSearch import *


def tweets(resturant):
    try:
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords([resturant]) # let's define all words we would like to have a look for
        tso.set_language('en') # we want to see German tweets only
        tso.set_include_entities(False) # and don't give us all those entity information

        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch(
            consumer_key = 'YfeOV881N5IJRpq5dBtw',
            consumer_secret = '6ZCATdC9rk7tBHuumlVNKjyawrY3b2rEyaT5vX4bMI',
            access_token = '98964433-5EdRrCuuNWGSUJs1UIIVTFTCc58t9EJ8ujwESaRhj',
            access_token_secret = 'j6PX0HjjYxdWYbgUXbMvV2hdYoR8hUTiCcX6Ag4NaVkgz'
         )

         # this is where the fun actually starts :)
        x=0
        tweets=[]
        for tweet in ts.search_tweets_iterable(tso):
            x = x + 1
            tweets.append('@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ))

            if x==3: break
        return tweets
    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)

print(tweets("mcd"))