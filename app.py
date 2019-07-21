import praw
import requests
import urllib.parse as urlparse
import os

reddit = praw.Reddit(client_id='j0bm-shNQLoL7w',
                     client_secret='TT1Byd0ErUS9AsTT6PQXOG_Q4VY',
                     user_agent='my-user-agent')

my_sub = reddit.subreddit('earthporn+linuxporn')
imagesList = []
badContent = ["comments","gfycat","youtu.be"]

def downloadImage(source):
    with open(source) as file:
        for line in file:
            filename = line.split("/")[-1]
            r = requests.get(line.strip())
            open('images/' + filename.strip(),'wb').write(r.content)

for i in my_sub.stream.submissions():
    if 'imgur' in i.url or 'redd' in i.url:
        myfile = open('images.txt', 'a')
        imagesList.append(i.url)
        myfile.write(i.url + "\n")
        downloadImage('images.txt')
        print(i.url)
myfile.close()


#myfile = open('images.txt', 'w')
#for i in my_sub.new():
    #if 'imgur' in i.url or 'redd' in i.url:
        #imagesList.append(i.url)
        #myfile.write(i.url + " \n")
        #imageURL = requests.get(i.url)
        #filename = imageURL.split("/")[-1]
        #print(type(filename))
        #with open(filename, 'wb') as f:
            #f.write(r.content)
        #print(i.url)
#myfile.close()



#print(imagesList)
#print("Updated images.txt")

# To-do
# download the images
