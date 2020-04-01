import urllib.request
from datetime import datetime
import cv2
from pyagender import PyAgender
import names
import random


def GetPhoto():
    url = 'https://www.thispersondoesnotexist.com/image'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    request = urllib.request.Request(url, headers={'User-Agent': user_agent})
    response = urllib.request.urlopen(request)
    html = response.read()
    f = open('img.jpg', 'wb')
    f.write(html)
    f.close()

GetPhoto()
agender = PyAgender()
faces = agender.detect_genders_ages(cv2.imread('img.jpg'))
age = int(faces[0]['age'])
print("age: ", age)
print("date of birth: " + str(int(str(datetime.now())[:4]) - age) + '.' + str(random.randint(1,12)) + '.' + str(random.randint(1,31)))
if faces[0]['gender'] <0.5:
    print('gender: male')
    gender = 'male'
elif faces[0]['gender']>0.5:
    print('gender: female')
    gender = 'female'
else:
    print('gender: idk')
    if random.randint(0,1):
        gender = 'male'
    else:
        gender = 'female'
name=names.get_full_name(gender=gender)
print("name: ", name)
print("relatives: ", *[names.get_first_name() + ' ' + name.split()[1] for i in range(0,random.randint(1,7))])
