import io

import requests

try:
    import tweepy
except ImportError:
    raise ImportError("Tweepy is not installed")

try:
    from PIL import Image
except ImportError:
    raise ImportError("PIP is not installed")

import settings.SETTINGS as SETTINGS


def post_text(text: str):
    if SETTINGS.nopost is True:
        return
    auth = tweepy.OAuthHandler(consumer_key=SETTINGS.TWITTER_TOKEN["consumer_key"],
                               consumer_secret=SETTINGS.TWITTER_TOKEN["consumer_secret"])
    auth.set_access_token(key=SETTINGS.TWITTER_TOKEN["access_token_key"],
                          secret=SETTINGS.TWITTER_TOKEN["access_token_secret"])
    client = tweepy.API(auth)
    try:
        auth.get_username()
    except:
        raise KeyError("INVALID TWITTER KEYS")
    client.update_status(status=text)
    return


def tweet_image(url, message):
    if SETTINGS.nopost is True:
        return
    auth = tweepy.OAuthHandler(consumer_key=SETTINGS.TWITTER_TOKEN["consumer_key"],
                               consumer_secret=SETTINGS.TWITTER_TOKEN["consumer_secret"])
    auth.set_access_token(key=SETTINGS.TWITTER_TOKEN["access_token_key"],
                          secret=SETTINGS.TWITTER_TOKEN["access_token_secret"])
    client = tweepy.API(auth)
    try:
        auth.get_username()
    except:
        raise KeyError("INVALID TWITTER KEYS")
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
        else:
            # pass
            raise tweepy.TweepError("!!!SIMULATION!!!")
    except tweepy.TweepError as ex:
        print(ex)
        for tint in range(2, 10):
            try:
                temp = Image.open("image.png")
            except Exception as ex:
                return print(ex)
            x = int(round(temp.size[0] / tint))
            if x <= 0:
                x = 1900
            y = int(round(temp.size[1] / tint))
            if y <= 0:
                y = 1080
            temp = temp.resize((x, y), Image.ANTIALIAS)
            temp.save("image.png", optimize=True, quality=int(round(100 / tint)))
            temp.save(io.BytesIO(), format="PNG")
            try:
                client.update_with_media("image.png", status=message)
                break
            except tweepy.TweepError as ex:
                print(ex)
