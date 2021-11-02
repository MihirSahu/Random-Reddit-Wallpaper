#!/bin/python3

import os
import urllib.request
import praw
import random

# Create Reddit instance
reddit = praw.Reddit(
    user_agent="Comment Extraction (by u/USERNAME)",
    client_id="in2HuqFUZl3aGRhZoJQz3Q",
    client_secret="Dl9iHhXbipTIyQjnydqtwqtirErOhw",
    username="uncomprehensivebelt",
    password="uW7P2]sqe8D&!sjJ",
)

# Specify subreddit to target
subreddit = reddit.subreddit("wallpapers")

# Generate random number
randomNum = random.randrange(0, 51)

# Get 50 hot submissions from subreddit, add urls to a list, and select the nth one depending on randomNum. Save the url of the image to a variable
urlList = []
for submission in subreddit.hot(limit=50):
    urlList.append(submission.url)
imgUrl = urlList[randomNum]

# Detect name of image from url and save to variable
imgName = ""
temp = list(imgUrl)
temp.reverse()
for idx, i in enumerate(temp):
    if i == '/':
        temp = temp[:idx]
        temp.reverse()
        imgName = "".join(temp)

# Download image from url
urllib.request.urlretrieve(imgUrl, f"/home/theonlyonzz/Pictures/reddit_wallpapers/{imgName}")

# Set wallpaper using feh utility on linux
os.system(f"feh --bg-fill ~/Pictures/reddit_wallpapers/{imgName}")
