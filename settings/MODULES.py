import io
import os

import requests

try:
    import tweepy
except ImportError:
    os.system('python -m pip install tweepy')
try:
    from PIL import Image
except ImportError:
    os.system('python -m pip install pillow')

import settings.SETTINGS as SETTINGS


def post_text(text: str):
    auth = tweepy.OAuthHandler(consumer_key=SETTINGS.TWITTER_TOKEN["consumer_key"],
                               consumer_secret=SETTINGS.TWITTER_TOKEN["consumer_secret"])
    auth.set_access_token(key=SETTINGS.TWITTER_TOKEN["access_token_key"],
                          secret=SETTINGS.TWITTER_TOKEN["access_token_secret"])
    client = tweepy.API(auth)
    if SETTINGS.nopost is False:
        client.update_status(status=text)
    return


def tweet_image(url, message):
    auth = tweepy.OAuthHandler(consumer_key=SETTINGS.TWITTER_TOKEN["consumer_key"],
                               consumer_secret=SETTINGS.TWITTER_TOKEN["consumer_secret"])
    auth.set_access_token(key=SETTINGS.TWITTER_TOKEN["access_token_key"],
                          secret=SETTINGS.TWITTER_TOKEN["access_token_secret"])
    client = tweepy.API(auth)
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open("image.png", 'wb') as image:
            for chunk in request:
                image.write(chunk)
    else:
        return print("Unable to download image")
    try:
        if SETTINGS.nopost is False:
            client.update_with_media("image.png", status=message)
    except tweepy.TweepError as ex:
        print(ex)
        for tint in range(2, 11):
            temp = Image.open("image.png")
            x = int(round(temp.size[0] / tint))
            y = int(round(temp.size[1] / tint))
            temp = temp.resize((x, y), Image.ANTIALIAS)
            temp.save("image.png", optimize=True, quality=int(round(100 / tint)))
            temp.save(io.BytesIO(), format="PNG")
            try:
                if SETTINGS.nopost is False:
                    client.update_with_media("image.png", status=message)
                break
            except tweepy.TweepError as ex:
                print(ex)