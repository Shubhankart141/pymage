import requests
import urllib.parse as urlparse
import os

f = open('images.txt', 'r')

def downloadImage(source):
    with open(source) as file:
        for line in file:
            filename = line.split("/")[-1]
            r = requests.get(line.strip())
            open('images/' + filename.strip(),'wb').write(r.content)


downloadImage('images.txt')

#url = 'https://i.redd.it/mdx71eo604b31.jpg'
#r = requests.get(url)
#filename = url.split("/")[-1]
#open(filename,'wb').write(r.content)


#r = requests.get(url)
#open('images/image.png','wb').write(r.content)
