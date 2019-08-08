import json

urls = ["https://imgur.com/image.jpg", "https://imgur.com/anotherimage.jpg"]

data = json.loads(urls)
print(data)
