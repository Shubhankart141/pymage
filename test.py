import urllib.parse as urlparse
import os

f = open('images.txt', 'r')

for x in f:
    url = x
    print(url.split("/")[-1])
