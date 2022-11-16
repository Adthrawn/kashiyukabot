This is a quick-ish bot I wrote for twitter that loops through a provided directory of images and mp4s (in place of .gif files, due to twitter upload limitations) and posts them to twitter

Most of the config is done via the credConfig.cfg file

You will need the following details for the Twitter API

 - consumerKey
 - consumerSecret
 - accessToken
 - accessTokenSecret

There are two other configs
 - image_dir - path to where the images are stored
 - hastags - the hashtags to include with the post

At the moment, you should only need the following python libraries

 - oauthlib
 - requests
 - requests-oauthlib
 - configparser
 - python3-magic

You run the script by executing the main.py file
