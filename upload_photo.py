#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password


import time
from timeloop import Timeloop
from datetime import timedelta

# Do the import
# import InstagramAPI

import os
from InstagramAPI.InstagramAPI import InstagramAPI

tl = Timeloop()

# username = os.environ['instagram_username']
# password = os.environ['instagram_password']
# instagramAPI = InstagramAPI(username, password)
# instagramAPI.login()  # login
# photoId = 1
# caption = "#dog #dogsofinstagram #dogs #puppy #instadog #dogstagram  #doglover #dogoftheday " \
#           "#doglovers #puppies #doggo #puppylove #ilovemydog #puppiesofinstagram #doglife " \
#           "#doggy #dogsofinsta #Husky #Huskies #HuskiesOfInstagram " \
#           "#HuskyPuppy #SiberianHusky #HuskyGram #HuskyLove #HuskyNation #HuskyOfInstagram #HuskyWorld #HuskyDog " \
#           "#InstaHusky #HuskyPuppies "


def rewriteImageName():
    path_name = './photos/'
    arr = os.listdir('./photos/')
    index = arr.__len__()
    i =1
    for file in arr:
        os.rename("{}/{}".format(path_name, file), "{}/{}".format(path_name, "{}.JPEG".format(i)))
        print(file)
        i += 1
        # break

@tl.job(interval=timedelta(seconds=600))
def uploadPhoto():
    global photoId
    global instagramAPI
    global caption

    photo_path = 'photos/{}.JPEG'.format(photoId)
    print("Uploading photo {}".format(photo_path))
    instagramAPI.uploadPhoto(photo_path, caption=caption)
    photoId += 1
    print("Uploaded photo {}".format(photo_path))


# uploadPhoto()
# tl.start(block=True)

rewriteImageName()
