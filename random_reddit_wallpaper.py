#!/bin/python3

import os
import urllib.request
import praw
import random
import imagesize

# Function to check connection with reddit
def connect(host='https://www.reddit.com'):
    try:
        urllib.request.urlopen(host, timeout=6) #Python 3.x
        return True
    except:
        return False

if (connect()):
    # Create Reddit instance
    reddit = praw.Reddit(
        user_agent="Comment Extraction (by u/USERNAME)",
        client_id="in2HuqFUZl3aGRhZoJQz3Q",
        client_secret="Dl9iHhXbipTIyQjnydqtwqtirErOhw",
        username="uncomprehensivebelt",
        password="uW7P2]sqe8D&!sjJ",
    )

    # List of subreddits you want to get wallpapers from
    subList = ["wallpapers", "wallpaper", "animewallpaper"]

    randomNum = random.randrange(0, len(subList))

    # Specify subreddit
    sub = subList[randomNum]

    # Create instance of subreddit with specified sub
    subreddit = reddit.subreddit(sub)

    # Get 50 hot submissions from subreddit and add urls to a list
    urlList = []
    for submission in subreddit.hot(limit=50):
        urlList.append(submission.url)

    # Detect name of file from url and save to variable. If file name does not end with .png or .jpg, choose another random number and repeat process until an image comes up
    imgName = ""
    while ((imgName[-4:] != ".png") and (imgName[-4:] != ".jpg")):

        # Generate random number
        randomNum = random.randrange(0, 50)

        imgUrl = urlList[randomNum]

        temp = list(imgUrl)
        temp.reverse()
        for idx, i in enumerate(temp):
            if i == '/':
                temp = temp[:idx]
                temp.reverse()
                imgName = "".join(temp)


    # Download image from url
    urllib.request.urlretrieve(imgUrl, f"/home/theonlyonzz/Pictures/reddit_wallpapers/{imgName}")

    # Compare image width and height to determine whether it's a vertical or horizontal wallpaper, and then set the wallpaper using feh utility on linux
    # Find width and height
    width, height = imagesize.get(f"/home/theonlyonzz/Pictures/reddit_wallpapers/{imgName}")
    # Set wallpaper
    if height > width:
        os.system(f"feh --bg-max /home/theonlyonzz/Pictures/reddit_wallpapers/{imgName}")
    else:
        os.system(f"feh --bg-fill /home/theonlyonzz/Pictures/reddit_wallpapers/{imgName}")

else:
    # Change directory to wallpaper folder
    os.chdir("/home/theonlyonzz/Pictures/reddit_wallpapers/")

    # Make list of files in directory
    imgList = [name for name in os.listdir('.') if os.path.isfile(name)]

    # Choose a random number from the number of files in the directory
    randomNum = random.randrange(0, len(imgList))

    # Find width and height
    width, height = imagesize.get(f"/home/theonlyonzz/Pictures/reddit_wallpapers/{imgList[randomNum]}")

    if height > width:
        os.system(f"feh --bg-max /home/theonlyonzz/Pictures/reddit_wallpapers/{imgList[randomNum]}")
    else:
        os.system(f"feh --bg-fill /home/theonlyonzz/Pictures/reddit_wallpapers/{imgList[randomNum]}")
