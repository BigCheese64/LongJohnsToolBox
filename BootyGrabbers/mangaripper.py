#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:49:33 2020

@author: root
"""
import time
import urllib.request
from selenium import webdriver
import os
#from selenium import webTable 
class linkTableInfo(object):
    def __init__(self,webTable):
        self.table=webTable
    def get_row_count(self):
        return len(self.table.find_elements_by_tag_name("tr")) - 1

    def row_data(self,rowcount):
        text=[]
        for row_number in range(rowcount):
            #/html/body/div[1]/div[5]/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[1]/a
            #/html/body/div[1]/div[5]/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[1]/a
            #/html/body/div[1]/div[5]/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[1]/a
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
    #/html/body/div[1]/div[4]/div[9]/p[1]/img
    #/html/body/div[1]/div[4]/div[9]/p[2]/img
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
startpage=input("Please paste the url of the kissmanga chapter selection page:")
mangaName=input('What is the name of the manga you are downloading:')

driver=webdriver.Firefox()
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
    print(i)
    time.sleep(1)
linklist.reverse()
print(linklist)
b=0
for i in linklist:
    b+=1        
    if b>=82:
        print(i)
        if i!=[]:
            print(i[0])
            driver.get(i[0])
            while True:
                try:
                    pgnum=saveImages(driver,mangaName,pgnum)
                    break
                except:
                    loop=True

driver.close()
    
