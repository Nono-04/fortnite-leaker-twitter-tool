""" SETTINGS
What the bot should post on Twitter:
If a Type is True than the Bot post it. (If a Type is False than the Bot dont post it)
"""

lang = "en"

# Leaks CONFIG
leaks =             True
leaksimagetext =    f"Fortnite Leaks" # Text in the Image
leaksimageurl =     "" # Need to be a URL | The best is a colored background
# Shop CONFIG
shop =              True
shopimagetext =     f"Fortnite Item Shop" # Text in the Image
shopimageurl =      "" # Need to be a URL | The best is a colored background
#### OTHER Features ####
brnews =            True
stwnews =           True
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
    "consumer_key": "5dwJkyLLOnGvmjCBSD7fmHR8M",
    "consumer_secret": "DSIanSeBn6e0GIPbjO6XHBgimLz6R4xsyQQsSYwfucSMTsvAwG",
    "access_token_key": "1074046337673506816-khQ4rj7hohB3b89ZiKEvfzFp5MXDSu",
    "access_token_secret": "flS3jeBsl5C2mJj5QkFE3gWB3ZHpKv7DhZLH78vzJrOym",
}

nopost = False  # A FUNCTION FOR TESTING! Leave it on False or the Bot dont work!!!!
