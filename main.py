import json
import os
import time

import requests

try:
    import tweepy
except ImportError:
    os.system('python -m pip install tweepy')
    try:
        import tweepy
    except ImportError:
        print("Please install the Python Package: tweepy\nOpen CMD and enter this:\n\npython -m pip install tweepy")

import settings.SETTINGS as SETTINGS
import settings.MODULES as MODULES


def get_text(type: str):
    with open("lang.json") as lang:
        data = json.loads(lang.read())

        try:
            output = str(data[type][SETTINGS.lang])
        except:
            output = str(data[type]["en"])
        return output


def check_leaks():
    try:
        with open('Cache/leaks.json', 'r') as file:
            Cached = json.load(file)
        data = requests.get('https://peely.de/api/leaks/lastupdate')
        new = data.json()
        if data.status_code != 200:
            return
    except Exception as ex:
        print(ex, "leaks")
        return
    if new != Cached:
        url = "https://peely.de/leaks"
        if SETTINGS.leaksimageurl or SETTINGS.leaksimagetext != "":
            url = f"https://peely.de/api/leaks/custom?background={SETTINGS.leaksimageurl}&text={SETTINGS.leaksimagetext}"
        MODULES.tweet_image(url=url, message=get_text("shop"))
        with open('Cache/leaks.json', 'w') as file:
            json.dump(new, file, indent=3)
        print("Leaks posted")


def check_shop():
    try:
        with open('Cache/shop.json', 'r') as file:
            Cached = json.load(file)
        data = requests.get('https://peely.de/api/shop/lastupdate')
        new = data.json()
        if data.status_code != 200:
            return
    except:
        return
    if new != Cached:
        url = new["discordurl"]
        if SETTINGS.shopimageurl or SETTINGS.shopimagetext != "":
            url = f"https://peely.de/api/shop/custom?background={SETTINGS.shopimageurl}&text={SETTINGS.shopimagetext}"
        print(url)
        MODULES.tweet_image(url=url, message=get_text("shop"))
        with open('Cache/shop.json', 'w') as file:
            json.dump(new, file, indent=3)
        print("Item Shop posted")


def emergencynotice():
    try:
        with open('Cache/content.json', 'r') as file:
            Cached = json.load(file)
        data = requests.get(
            f'https://fortnitecontent-website-prod07.ol.epicgames.com/content/api/pages/fortnite-game?lang={SETTINGS.lang}')
        new = data.json()
        if data.status_code != 200:
            return
    except:
        return
    if new["emergencynotice"]["news"]["messages"] != Cached["emergencynotice"]["news"]["messages"]:
        for i in new["emergencynotice"]["news"]["messages"]:
            if i not in Cached["emergencynotice"]["news"]["messages"]:
                title = i["title"]
                body = i["body"]
                MODULES.post_text(text=f"{title}\n{body}")
        print("emergencynotice posted")
    with open('Cache/content.json', 'w') as file:
        json.dump(new, file, indent=3)


def blogpost():
    try:
        with open('Cache/blog.json', 'r', encoding="utf8") as file:
            Cached = json.load(file)
        data = requests.get(
            f'https://www.epicgames.com/fortnite/api/blog/getPosts?category=&postsPerPage=6&offset=0&locale={SETTINGS.lang}')
        new = data.json()
        if data.status_code != 200:
            return
    except:
        return
    if Cached["blogList"] != new["blogList"]:
        print("Blog Update")
        for i in new["blogList"]:
            old = False
            for i2 in Cached["blogList"]:
                if i["title"] == i2["title"]:
                    old = True
            if old is True:
                continue
            else:
                MODULES.tweet_image(url=i["image"], message=f'https://www.epicgames.com/fortnite/{i["urlPattern"]}')
        with open('Cache/blog.json', 'w', encoding="utf8") as file:
            json.dump(new, file, indent=3)


def staging():
    try:
        with open('Cache/staging.json', 'r', encoding="utf8") as file:
            Cached = json.load(file)
        data = requests.get(
            'https://fortnite-public-service-stage.ol.epicgames.com/fortnite/api/version')
        new = data.json()
        if data.status_code != 200:
            return
    except:
        return
    if Cached["version"] != new["version"]:
        print("Staging Server Updated")
        MODULES.post_text(text=new["version"] + get_text("staging"))
        with open('Cache/staging.json', 'w', encoding="utf8") as file:
            json.dump(new, file, indent=3)


def news():
    with open('Cache/news.json', 'r', encoding="utf8") as file:
        old = json.load(file)
    try:
        req = requests.get(f"https://fortnite-api.com/v2/news/br?lang={SETTINGS.lang}")
        if req.status_code != 200:
            return
        new = req.json()
    except:
        return
    if old != new:
        for i in new["data"]["motds"]:
            if not i in old["data"]["motds"]:
                print("NEW news feed")
                MODULES.tweet_image(url=i["image"], message=get_text("news") + f"\n{i['title']}\n{i['body']}")
                with open('Cache/news.json', 'w', encoding="utf8") as file:
                    json.dump(new, file, indent=3)


def featuredislands():
    with open('Cache/featuredislands.json', 'r', encoding="utf8") as file:
        old = json.load(file)
    try:
        req = requests.get("https://peely.de/api/featured_islands")
        if req.status_code != 200:
            return
        new = req.json()
    except:
        return
    if old != new:
        for i in new["featured_islands"]:
            if not i in old["featured_islands"]:
                MODULES.tweet_image(url=i["image"],
                                    message=get_text("featuredislands") + f"\n{i['title']}\n{i['code']}")
    with open('Cache/featuredislands.json', 'w', encoding="utf8") as file:
        json.dump(new, file, indent=3)


def playlist():
    try:
        with open('Cache/playlist.json', 'r') as file:
            Cached = json.load(file)
        data = requests.get(
            f'https://fortnitecontent-website-prod07.ol.epicgames.com/content/api/pages/fortnite-game?lang={SETTINGS.lang}')
        new = data.json()
        if data.status_code != 200:
            return
    except:
        return
    if new["playlistinformation"]["playlist_info"]["playlists"] != Cached["playlistinformation"]["playlist_info"][
        "playlists"]:
        for i in new["playlistinformation"]["playlist_info"]["playlists"]:
            if i not in Cached["playlistinformation"]["playlist_info"]["playlists"]:
                try:
                    playlist_name = i["playlist_name"]
                    _type = i["_type"]
                    image = i["image"]
                    MODULES.tweet_image(
                        url=i["image"],
                        message=get_text(
                            "playlist") + f"\n\nName:\n{playlist_name}\n\nType:\n {_type}\n\nLink:\n{image}")
                except:
                    MODULES.post_text(text=get_text("playlist") + f"\n\nName:\n{i['playlist_name']}")
        print("Playlist gepostet")
    with open('Cache/playlist.json', 'w') as file:
        json.dump(new, file)


if __name__ == "__main__":
    print("Twitter Bot Ready")
    while True:
        print("Checking...")
        if SETTINGS.leaks is True:
            check_leaks()
        if SETTINGS.ingamebugmessage is True:
            emergencynotice()
        if SETTINGS.shop is True:
            check_shop()
        if SETTINGS.staging is True:
            staging()
        if SETTINGS.blogposts is True:
            blogpost()
        if SETTINGS.newsfeed is True:
            news()
        if SETTINGS.featuredislands is True:
            featuredislands()
        if SETTINGS.playlist is True:
            playlist()
        if SETTINGS.intervall < 20:
            time.sleep(20)
        else:
            time.sleep(SETTINGS.intervall)
