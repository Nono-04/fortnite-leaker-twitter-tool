from datetime import datetime
import json
import time

import requests

try:
    import tweepy
except Exception as ex:
    raise ImportError("Tweepy is not installed " + str(ex))

from settings import SETTINGS as SETTINGS
from settings import MODULES as MODULES


def get_text(type: str):
    with open('lang.json', mode='r', encoding="ISO-8859-1") as file:
        data = json.load(file)
        try:
            output = str(data[type][SETTINGS.lang])
        except:
            print("Lang is not defind")
            output = str(data[type]["en"])
        return output


def check_leaks():
    try:
        with open('Cache/leaks.json', 'r') as file:
            Cached = json.load(file)
        data = requests.get('https://api.peely.de/v1/leaks')
        new = data.json()
        if data.status_code != 200:
            return
    except Exception as ex:
        print(ex, "leaks")
        return
    if new != Cached:
        url = "https://peely.de/leaks"
        if SETTINGS.leaksimageurl or SETTINGS.leaksimagetext != "":
            lang = "en"
            if SETTINGS.lang:
                lang = SETTINGS.lang
            url = f"https://api.peely.de/v1/leaks/custom?background={SETTINGS.leaksimageurl}&text={SETTINGS.leaksimagetext}&lang={lang}"
        try:
            print("NEW Leaks")
            MODULES.tweet_image(url=url, message=get_text("leaks"))
        except Exception as ex:
            raise tweepy.TweepError(ex)
        with open('Cache/leaks.json', 'w') as file:
            json.dump(new, file, indent=3)


def check_shop():
    try:
        with open('Cache/shop.json', 'r') as file:
            Cached = json.load(file)
        data = requests.get('https://api.peely.de/v1/shop')
        new = data.json()
        if data.status_code != 200:
            return
    except:
        return
    if new != Cached:
        url = new["discordurl"]
        if SETTINGS.shopimagedate is True:
            SETTINGS.shopimagetext = "Item Shop from " + str(datetime.utcnow().__format__('%d.%m.%Y'))
        if SETTINGS.shopimageurl or SETTINGS.shopimagetext != "":
            lang = "en"
            if SETTINGS.lang:
                lang = SETTINGS.lang
            url = f"https://api.peely.de/v1/shop/custom?background={SETTINGS.shopimageurl}&text={SETTINGS.shopimagetext}&lang={lang}"
        try:
            print("NEW Shop")
            print(url)
            MODULES.tweet_image(url=url, message=get_text("shop"))
        except Exception as ex:
            raise tweepy.TweepError(ex)
        with open('Cache/shop.json', 'w') as file:
            json.dump(new, file, indent=3)


def emergencynotice():
    try:
        with open('Cache/notice.json', 'r') as file:
            Cached = json.load(file)
        data = requests.get(
            f'https://api.peely.de/v1/notices?lang={SETTINGS.lang}')
        new = data.json()
        if data.status_code != 200:
            return
    except:
        return
    if new["data"]["messages"] != Cached["data"]["messages"]:
        for i in new["data"]["messages"]:
            if i not in Cached["data"]["messages"]:
                title = i["title"]
                body = i["body"]
                MODULES.post_text(text=f"{title}\n{body}")
        print("NEW Notice")
    with open('Cache/notice.json', 'w') as file:
        json.dump(new, file, indent=3)


def blogpost():
    try:
        with open('Cache/blog.json', 'r', encoding="utf8") as file:
            Cached = json.load(file)
        data = requests.get(
            f'https://api.peely.de/v1/blogposts/normal?lang={SETTINGS.lang}')
        new = data.json()
        if data.status_code != 200:
            return
    except:
        return
    if Cached["data"]["blogposts"] != new["data"]["blogposts"]:
        for i in new["data"]["blogposts"]:
            old = False
            for i2 in Cached["data"]["blogposts"]:
                if i["url"] == i2["url"]:
                    old = True
            if old is True:
                continue
            else:
                print("NEW Blogpost")
                MODULES.tweet_image(url=i["url"], message=get_text(
                    "blogpost") + f'\n\n{i["url"]}')
        with open('Cache/blog.json', 'w', encoding="utf8") as file:
            json.dump(new, file, indent=3)


def staging():
    try:
        with open('Cache/staging.json', 'r', encoding="utf8") as file:
            Cached = json.load(file)
        data = requests.get(
            'https://api.peely.de/v1/staging')
        new = data.json()
        if data.status_code != 200:
            return
    except:
        return
    if Cached["data"]["staging"] != new["data"]["staging"]:
        print("NEW Staging Server")
        MODULES.post_text(text=new["data"]["staging"] + f" " + get_text("staging"))
        with open('Cache/staging.json', 'w', encoding="utf8") as file:
            json.dump(new, file, indent=3)


def brnews():
    with open('Cache/brnews.json', 'r', encoding="utf8") as file:
        old = json.load(file)
    try:
        req = requests.get(
            f"https://api.peely.de/v1/br/news?lang={SETTINGS.lang}")
        if req.status_code != 200:
            return
        new = req.json()
    except:
        return
    if old != new:
        try:
            for i in new["data"]["motds"]:
                if not i in old["data"]["motds"]:
                    print("NEW BR news feed")
                    MODULES.tweet_image(url=i["image"], message=get_text(
                        "brnews") + f"\n\n{i['title']}\n\n{i['body']}")
        except:
            pass
        with open('Cache/brnews.json', 'w', encoding="utf8") as file:
            json.dump(new, file, indent=3)


def playlist():
    try:
        with open('Cache/playlist.json', 'r') as file:
            Cached = json.load(file)
        data = requests.get(
            f'https://api.peely.de/v1/playlists?lang={SETTINGS.lang}')
        new = data.json()
        if data.status_code != 200:
            return
    except:
        return
    if new["data"]["playlists"] != Cached["data"]["playlists"]:
        for i in new["data"]["playlists"]:
            if i not in Cached["data"]["playlists"]:
                print("NEW Playlist")
                try:
                    playlist_id = i["playlist_id"]
                    _type = i["_type"]
                    image = i["image"]
                    MODULES.tweet_image(
                        url=i["image"],
                        message=get_text(
                            "playlist") + f"\n\nName:\n{playlist_id}\n\nLink:\n{image}")
                except:
                    MODULES.post_text(text=get_text(
                        "playlist") + f"\n\nName:\n{i['playlist_id']}")
    with open('Cache/playlist.json', 'w') as file:
        json.dump(new, file)


def stwnews():
    with open('Cache/stwnews.json', 'r', encoding="utf8") as file:
        old = json.load(file)
    try:
        req = requests.get(
            f"https://api.peely.de/v1/stw/news?lang={SETTINGS.lang}")
        if req.status_code != 200:
            return
        new = req.json()
    except:
        return
    if old != new:
        try:
            for i in new["data"]["messages"]:
                if not i in old["data"]["messages"]:
                    print("NEW STW news feed")
                    MODULES.tweet_image(url=i["image"], message=get_text(
                        "stwnews") + f"\n\n{i['title']}\n{i['body']}")
        except:
            pass
        with open('Cache/stwnews.json', 'w', encoding="utf8") as file:
            json.dump(new, file, indent=3)


def creativenews():
    with open('Cache/creativenews.json', 'r', encoding="utf8") as file:
        old = json.load(file)
    try:
        req = requests.get(
            f"https://api.peely.de/v1/creative/news?lang={SETTINGS.lang}")
        if req.status_code != 200:
            return
        new = req.json()
    except:
        return
    if old != new:
        try:
            for i in new["data"]["motds"]:
                if not i in old["data"]["motds"]:
                    print("NEW Creative news feed")
                    MODULES.tweet_image(url=i["image"], message=get_text(
                        "creativenews") + f"\n\n{i['title']}\n{i['body']}")
        except:
            pass
        with open('Cache/creativenews.json', 'w', encoding="utf8") as file:
            json.dump(new, file, indent=3)


def compblog():
    try:
        with open('Cache/compblog.json', 'r', encoding="utf8") as file:
            Cached = json.load(file)
        data = requests.get(
            f'api.peely.de/v1/blogposts/competitive?lang={SETTINGS.lang}')
        new = data.json()
        if data.status_code != 200:
            return
    except:
        return
    if Cached["data"]["blogposts"] != new["data"]["blogposts"]:
        for i in new["data"]["blogposts"]:
            old = False
            for i2 in Cached["data"]["blogposts"]:
                if i["url"] == i2["url"]:
                    old = True
            if old is True:
                continue
            else:
                print("NEW Competitive Blogpost")
                MODULES.tweet_image(url=i["url"], message=get_text(
                    "compblogpost") + f'\n\n{i["url"]}')

        with open('Cache/compblog.json', 'w', encoding="utf8") as file:
            json.dump(new, file, indent=3)


def tournament():
    try:
        with open('Cache/tournament.json', 'r') as file:
            Cached = json.load(file)
        data = requests.get(
            f'https://api.peely.de/v1/tournaments?lang={SETTINGS.lang}')
        new = data.json()
        if data.status_code != 200:
            return
    except:
        return
    if new["data"]["tournaments"] != Cached["data"]["tournaments"]:
        for i in new["data"]["tournaments"]:
            if i not in Cached["data"]["tournaments"]:
                name = i["name"]
                short_description = i["short_description"]
                try:
                    MODULES.tweet_image(
                        url=i["image"],
                        message=get_text(
                            "tournament") + f"\n\nName:\n{name}\n\nDesc:\n{short_description}")
                except:
                    MODULES.post_text(text=get_text(
                        "tournament") + f"\n\nName:\n{name}\n\nDesc:\n{short_description}")
        print("NEW Tournament")
    with open('Cache/tournament.json', 'w') as file:
        json.dump(new, file, indent=3)


def progressbar():
    try:
        with open('Cache/progress.json', 'r') as file:
            Cached = json.load(file)
        data = requests.get(
            f'https://api.peely.de/v1/br/progress/data')
        new = data.json()
        if data.status_code != 200:
            return
    except:
        return
    if new["data"]['DaysLeft'] != Cached["data"]['DaysLeft']:
        try:
            MODULES.tweet_image(
                url=f"https://api.peely.de/v1/br/progress?lang={SETTINGS.lang}",
                message=f"{new['data']['DaysLeft']} " + get_text(
                    "progress") + f". ({round((new['data']['SeasonLength'] / 100) * new['data']['DaysGone'], 2)}%)")
        except:
            return
        print("NEW Progressbar")
    with open('Cache/progress.json', 'w') as file:
        json.dump(new, file, indent=3)


if __name__ == "__main__":
    print("Twitter Bot Ready")
    while True:
        print("Checking...")
        if SETTINGS.leaks is True:
            check_leaks()
        if SETTINGS.shop is True:
            check_shop()
        if SETTINGS.brnews is True:
            brnews()
        if SETTINGS.creativenews is True:
            creativenews()
        if SETTINGS.stwnews is True:
            stwnews()
        if SETTINGS.blogposts is True:
            blogpost()
        if SETTINGS.compblog is True:
            compblog()
        if SETTINGS.ingamebugmessage is True:
            emergencynotice()
        if SETTINGS.staging is True:
            staging()
        if SETTINGS.playlist is True:
            playlist()
        if SETTINGS.tournament is True:
            tournament()
        if SETTINGS.progressbar is True:
            progressbar()
        # --------------------------------- #
        if SETTINGS.intervall <= 20:
            time.sleep(20)
        else:
            time.sleep(SETTINGS.intervall)
