#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:49:33 2020

@author: root
"""
import time
import urllib.request
from BGparent import browserSelect
import os
import configparser as cp

class linkTableInfo(object):
    def __init__(self,webTable):
        self.table=webTable
    def get_row_count(self):
        return len(self.table.find_elements_by_tag_name("tr")) - 1

    def row_data(self,rowcount):
        text=[]
        for row_number in range(rowcount):
            try:
                row_number = row_number+2
                row = self.table.find_elements_by_xpath("//tr["+str(row_number)+"]/td[1]/a")
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
        return(text)

def saveImages(driver,mangaName,pgnum):
    images=driver.find_elements_by_tag_name('p')
    print(len(images))
    for i in range(len(images)-2):
        i=i+1
        print(i)
        image=[]

        image=driver.find_elements_by_xpath('//p['+str(i)+']/img')
        if image==[]:
            break
        src=image[0].get_attribute('src')
        pgnum+=1
        if src!="":
            urllib.request.urlretrieve(src,mangaName+"/page"+str(pgnum))
        
    return(pgnum)
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
if driver != None:
    driver.get(startpage)
    linklist=[]
    loaded=0
    i=0
    os.system('mkdir '+mangaName)
    pgnum=1831
    
    while loaded==0:
        time.sleep(1)
        loaded=(linkTableInfo(driver).get_row_count())
    time.sleep(1)
    while linklist==[]:    
        i+=1
        linklist=linkTableInfo(driver).row_data(loaded)
        time.sleep(1)
    linklist.reverse()
    for i in linklist:
        b+=1        
        if b>=0:
            if i!=[]:
                print(b)
                driver.get(i[0])
                while True:
                    try:
                        pgnum=saveImages(driver,mangaName,pgnum)
                        break
                    except:
                        loop=True
    driver.close()
    
