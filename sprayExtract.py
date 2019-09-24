# coding: utf-8

from io import BytesIO

import os
import time
import requests

from PIL import Image
from bs4 import BeautifulSoup


OWCharacters = ['Ana', 'Ashe', 'Bastion', 'D.Va', 'Genji', 'Hanzo', 'Junkrat', 'Lúcio', 'McCree', 'Mei', 'Mercy', 'Orisa', 'Pharah', 'Reaper',
                'Reinhardt', 'Roadhog', 'Soldier 76', 'Sombra', 'Symmetra', 'Torbjörn', 'Tracer', 'Widowmaker', 'Winston',
                'Zarya', 'Zenyatta', 'General']

extractDirectory = 'extract_output/'

def createDir(name):
    if not os.path.exists(extractDirectory + name):
        print ('# - Create Directory: ' + extractDirectory + name)
        os.makedirs(extractDirectory + name)


def downloadPicture(dir, pictName, pictUrl):
    loc = extractDirectory+dir+'/'+pictName
    if pictUrl is not " ":
        o = requests.get(pictUrl)
        i = Image.open(BytesIO(o.content))
        i.save(loc)
        print ('# - Save picture: ' + loc)


def newUrlFormat(url):
    s = url.replace("/thumb", "")
    f = s.split('/100')
    print ('# - URL edited: ' + f[0])
    return f[0]


def selectSprayImgInWebsite(urlSpray):
    r = requests.get(urlSpray)
    print ('# - GET')
    r_html = r.text
    soup = BeautifulSoup(r_html, 'html.parser')
    for q in OWCharacters:
        createDir(q)
    data = {}
    for image in soup.findAll('img'):
        if "Spray" in image.get('alt', ''):
            data[image.get('alt', '')] = newUrlFormat(image.get(('src'), ''))
    return data


def sortSprayForEachOWCharacters(characterList, sortedDict):
    for x, y in sortedDict.items():
        for z in characterList:
            if z in x:
                downloadPicture(z, x, y)
                sortedDict[x] = " "
                print (x + ': ' + y)
    return sortedDict


def getUnsortSprayInGeneralDir(unsortedDict):
    for x, y in unsortedDict.items():
        if y is not " ":
            downloadPicture('General', x, y)


def main(url):
    filtredDataCrawledFromWebsite = selectSprayImgInWebsite(url)
    leftDict = sortSprayForEachOWCharacters(OWCharacters, filtredDataCrawledFromWebsite)
    getUnsortSprayInGeneralDir(leftDict)


if __name__ == '__main__':
    main("http://overwatch.gamepedia.com/Sprays")
