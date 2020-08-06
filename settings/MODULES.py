import os

import requests

try:
    import tweepy
except ImportError:
    os.system('python -m pip install tweepy')

import settings.SETTINGS as SETTINGS


def post_text(text: str):
    if SETTINGS.nopost is True:
        return
    auth = tweepy.OAuthHandler(consumer_key=SETTINGS.TWITTER_TOKEN["consumer_key"],
                               consumer_secret=SETTINGS.TWITTER_TOKEN["consumer_secret"])
    auth.set_access_token(key=SETTINGS.TWITTER_TOKEN["access_token_key"],
                          secret=SETTINGS.TWITTER_TOKEN["access_token_secret"])
    client = tweepy.API(auth)
    client.update_status(status=text)
    return


def tweet_image(url, message):
    if SETTINGS.nopost is True:
        return
    auth = tweepy.OAuthHandler(consumer_key=SETTINGS.TWITTER_TOKEN["consumer_key"],
                               consumer_secret=SETTINGS.TWITTER_TOKEN["consumer_secret"])
    auth.set_access_token(key=SETTINGS.TWITTER_TOKEN["access_token_key"],
                          secret=SETTINGS.TWITTER_TOKEN["access_token_secret"])
    api = tweepy.API(auth)
    filename = 'Outpug/image.png'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)
        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")
