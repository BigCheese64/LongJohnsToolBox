#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:49:33 2020

@author: root
"""
import time
#import urllib.request #not sure if this is a native lib so if it no work try installing
from urllib.request import Request, urlopen
from BGparent import browserSelect
import os
import configparser as cp
from fpdf import FPDF
from PIL import Image

class linkTableInfo():
    def __init__(self,webTable):
        self.table=webTable
    def get_row_count(self):
        return len(self.table.find_elements_by_tag_name("h3")) - 11 #returns the number of chapter links

    def row_data(self,rowcount):
        text=[]
        for row_number in range(rowcount+1):
            try:
                row_number = row_number+2
                #/html/body/div[2]/div[5]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/h3/a
                
                row = self.table.find_elements_by_xpath("/html/body/div[2]/div[5]/div[2]/div[3]/div[2]/div[2]/div[2]/div["+str(row_number)+"]/div[1]/h3/a") #gets all of the links as elements
                rData = []
                print(len(row))
                for webElement in row :
                    try:
                        rData.append(webElement.get_attribute('href'))
                    except:
                        failed=True
                text.append(rData)
            except:
                failed=True
        print(text)
        return(text)

def saveImages(driver,mangaName,pgnum):
    images=driver.find_elements_by_tag_name('img')
    #print(len(images))
    for i in range(len(images)):
        i+=1
        #print(i)
        image=[]
        #/html/body/div[2]/div[5]/div[2]/div/div/div[1]/div[4]/img[1]
        #/html/body/div[2]/div[5]/div[2]/div/div/div[1]/div[4]/img[4]
        #/html/body/div[2]/div[5]/div[2]/div/div/div[1]/div[4]/img[8]
        image=driver.find_elements_by_xpath('/html/body/div[2]/div[5]/div[2]/div/div/div[1]/div[4]/img['+str(i)+']')
        #print(len(image))
        if image==[]:
            break
        src=image[0].get_attribute('src')
        #print(src)
        pgnum+=1
        if src!="":

            req = Request(src, headers={'User-Agent': 'Mozilla/5.0'})
            image = urlopen(req)
            output = open(mangaName+"/page"+str(pgnum)+'.jpg',"wb")
            output.write(image.read())
            output.close()
        
    return(pgnum)


def makePdf(pdfFileName, listPages,mangaName, dir = ''):

    dir += ""+mangaName+"/"
    cover = Image.open(dir + str(listPages[0]))
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])

    for page in listPages:
        pdf.add_page()
        pdf.image(dir + str(page) , 0, 0)

    pdf.output(pdfFileName + ".pdf", "F")



config = cp.ConfigParser()
config.read("mangaRipper.ini")
startpage=str(config['SETTINGS']['kissmangaurl'])
mangaName=str(config['SETTINGS']['manganame'])
b=input("If the program crashed please enter the last number printed otherwise press enter.")
if b!="":
    try:
        b=int(b)
    except:
        print("Start page must be a number!")
        b=-1
else:
    b=0
bselect=browserSelect()
driver=bselect.returnDriver()
driver=None
if driver != None:
    driver.get(startpage)
    linklist=[]
    loaded=0
    i=0
    os.system('mkdir '+'"'+mangaName+'"')
    pgnum=0
    
    while loaded==0:
        time.sleep(1)
        loaded=(linkTableInfo(driver).get_row_count())
    time.sleep(1)
    #print(loaded)
    while linklist==[]:    
        i+=1
        linklist=linkTableInfo(driver).row_data(loaded)
        time.sleep(1)
    linklist.reverse()
    for i in linklist:
        b+=1        
        if b>=0:
            if i!=[]:
                #print(b)
                driver.get(i[0])
                while True:
                    #try:
                    pgnum=saveImages(driver,mangaName,pgnum)
                    break
                    #except:
                        #loop=True
                print(pgnum)
    driver.close()
imageList=[]
#DELEATE THIS LINE q!!@!!!!!!!
pgnum=2301
for i in range(pgnum):
    i+=1
    imageList.append("page"+str(i)+'.jpg')
print(len(imageList))
makePdf(mangaName,imageList, mangaName)
        
    
