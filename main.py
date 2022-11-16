#!/usr/bin/env python3
import mediaUpload
import os
import time
import configparser
import os.path
from os import path

#startup configs/variables
creds = 'credConfig.cfg'
config = configparser.ConfigParser()
config.read(creds)
imageDir = config['misc']['image_dir']
hastags = config['misc']['hastags']
#time limit between posts, in seconds
timer = 2100.0

starttime = time.time()
#read the last iteration from the file
counterFile = 'counter.txt'
file = open(counterFile, 'r')
file_value = file.read()
file.close()
counter = int(file_value)

def imageList():
    #get an array of the files in the directory
    imageArray = os.listdir(imageDir)
    return imageArray
    
def newImage(img_counter,imageArray):
    #iterate counter
    img_counter = img_counter+1

    #check if the counter is at the end of the array
    if img_counter > len(imageArray)-1:
        #build image array again
        imageArray = imageList()
        #check if the new array length is the same as the old array length
        if img_counter == len(imageArray):
            #if so, set back to zero
            img_counter = 0

    #set the global counter and set the next image
    global counter
    counter = img_counter
    try:
        next_image = imageArray[counter]
    except:
        #if there is some exception with the array, just set it back to 0 so we can all get on with our lives
        next_image = imageArray[0]

    #check if the chosen image exists
    if path.exists(imageDir+next_image):
        #if it exists, write to log and continue
        print(str(next_image)+" exists")
    else:
        #if it does not exist, go through this method again until it returns and image that does
        next_image = newImage(img_counter,imageArray)
        print(str(next_image)+" does not exist")
    
    return next_image
    
    
def main(int_counter):
    #create the array of images in the folder
    imageArray = imageList()
    print(int_counter)
    message = 'image: ' + str(imageArray[int_counter]) + ' ' + hastags
    #upload first image
    status = str(mediaUpload.MediaTweet.media_main(imageDir+imageArray[int_counter],message))
    if status == 'failed':
        print('file: '+imageArray[int_counter]+' has failed going to next file')
    else:
        #wait for whatever time you specified in the config file
        time.sleep(2100.0 - ((time.time() - starttime) % 2100.0))
    while True:
        #get the next image
        next_image = newImage(counter,imageArray)
        imageArray = imageList()
        #construct the test of the tweet
        message = 'image: ' + str(imageArray[counter]) + ' ' + hastags
        #upload the file
        status = mediaUpload.MediaTweet.media_main(imageDir+next_image,message)
        #write the current iteration to a file
        file1 = open(counterFile, 'w')
        file1.write(str(counter))
        file1.close()
        if status == 'failed':
            print('file:'+next_image+' failed, going to next file')
        else:
            #wait for whatever time you specified in the config file
            time.sleep(2100.0 - ((time.time() - starttime) % 2100.0))

    
if __name__ == '__main__':
    main(counter)