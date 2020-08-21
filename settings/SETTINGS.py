""" SETTINGS
What the bot should post on Twitter:
If a Type is True than the Bot post it. (If a Type is False than the Bot dont post it)
"""

# Leaks CONFIG
leaks =             True
leaksimagetext =    f"Fortnite Leaks" # Text in the Image
leakstext =         f"Fortnite Leaks" # Text in the Tweet
leaksimageurl =     "" # Need to be a URL | The best is a colored background
# Shop CONFIG
shop =              True
shopimagetext =     f"Fortnite Item Shop" # Text in the Image
shoptext =          f"Fortnite Item Shop" # Text in the Tweet
shopimageurl =      "" # Need to be a URL | The best is a colored background
#### OTHER Features ####
newsfeed =          True
staging =           True
blogposts =         True
ingamebugmessage =  True
featuredislands =   True
playlist =          True
intervall = 30 # Under 20 Seconds is not allowed.


""" TWITTER_TOKEN
Enter here you Twitter Tokens from https://developer.twitter.com/en/apps
"""
TWITTER_TOKEN = {
                "consumer_key": "xxxxxxxxxxxxxxxxxxxxxx",
                "consumer_secret": "xxxxxxxxxxxxxxxxxxxxxx",
                "access_token_key": "xxxxxxxxxxxxxxxxxxxxxx",
                "access_token_secret": "xxxxxxxxxxxxxxxxxxxxxx",
            }

nopost = True  # A FUNCTION FOR TESTING! Leave it on False or the Bot dont work!!!!
