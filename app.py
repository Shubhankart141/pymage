import praw
import json

reddit = praw.Reddit(client_id='j0bm-shNQLoL7w',
                     client_secret='TT1Byd0ErUS9AsTT6PQXOG_Q4VY',
                     user_agent='my-user-agent')

my_sub = reddit.subreddit('indiansgonewild+HappyEmbarrassedGirls')
imagesList = []
badContent = ["comments","gfycat","youtu.be"]

myfile = open('images.txt', 'w')
for i in my_sub.new():
    if 'imgur' in i.url or 'redd' in i.url:
        imagesList.append(i.url)
        myfile.write(i.url + " \n")
        print(i.url)
myfile.close()

myfile = open('images.txt', 'a')
for i in my_sub.stream.submissions(skip_existing=True):
    if 'imgur' in i.url or 'redd' in i.url:
        imagesList.append(i.url)
        myfile.write(i.url + " \n")
        print(i.url)
myfile.close()

#print(imagesList)
#print("Updated images.txt")

# To-do
# download the images
