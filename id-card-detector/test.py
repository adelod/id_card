import requests
import urllib.request
from PIL import Image
f = open('updated.txt', 'r')
links = f.readlines()
i = 0
for link in links:

    # print(link)
    # response = requests.get(link)
    # print (response)
    if link.endswith('jpeg\n'):
        print('a')
        file = open('images/'+str(i)+'.jpeg', "wb")
    else:
        print('b')
        file = open('images/' + str(i) + '.jpg', "wb")
    file.write(urllib.request.urlopen(urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})).read())
    file.close()
    if link.endswith('jpg\n'):
        print('c')
        im1 = Image.open('images/'+ str(i) +'.jpg')
        im1.save(r'PngImages/'+ str(i)+r'.png')
        im1.close()
    if link.endswith('jpeg\n'):
        print('d')
        im1 = Image.open('images/' + str(i) + '.jpeg')
        im1.save('PngImages/' + str(i) + '.png')
        im1.close()
    i+=1
    if i > 5:
        break
