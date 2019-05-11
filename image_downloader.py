import urllib.request
import os

img_url = "https://betanews.com/wp-content/uploads/2017/09/firefox-logo.jpg"
img_name = os.path.basename(img_url)
print (img_name)
urllib.request.urlretrieve(img_url,img_name)
