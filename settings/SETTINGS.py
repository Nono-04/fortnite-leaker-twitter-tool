""" SETTINGS
What the bot should post on Twitter:
If a Type is True than the Bot post it. (If a Type is False than the Bot dont post it)
"""

lang = "en"

# Leaks CONFIG
leaks = True
leaksimagetext = f"Fortnite Leaks"  # Text in the Image
leaksimageurl = ""  # Need to be a URL | The best is a colored background
# Shop CONFIG
shop = True
shopimagetext = f"Fortnite Item Shop"  # Text in the Image
shopimagedate = True # Note: That will disable the Item Shop Text AND Multi Lang is not supported (only EN) but you are able to change the source code (Line: 64)
shopimageurl = ""  # Need to be a URL | The best is a colored background
#### OTHER Features ####
brnews = True
stwnews = True  # Not every News can be posted because of Text length
creativenews = True  # Might be SPAM if Creative and BR news are activated (same shop/other news)
staging = True
blogposts = True
ingamebugmessage = True
playlist = True
compblog = True
tournament = True
progressbar = True # Every Day a new Progressbar
intervall = 30  # Under 20 Seconds is not recommend

""" TWITTER_TOKEN
Enter here you Twitter Tokens from https://developer.twitter.com/en/apps
"""

TWITTER_TOKEN = {
    "consumer_key": "xxxx",
    "consumer_secret": "xxxx",
    "access_token_key": "xxxx",
    "access_token_secret": "xxxx",
}

nopost = True  # A FUNCTION FOR TESTING! Leave it on False or the Bot dont work!!!!
