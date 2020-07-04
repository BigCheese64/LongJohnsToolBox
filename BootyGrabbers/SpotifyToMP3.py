from selenium import webdriver
import time
import os
import configparser as cp

class spotifyToYoutube():
    def __init__(self,d,conf):
        self.driver=d
        self.directory=conf['SETTINGS']['Download Directory']
        self.playlist=conf['SETTINGS']['Playlist']
        self.driver.get(self.playlist)

    def getStuff(self):
        self.names=[]
        self.artists=[]
        counter=1
        Nelements=[]
        Aelements=[]
        while True:
            try:
                Nelements.append(self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[4]/div[1]/div/div[2]/div/div/div[2]/section[1]/div[4]/section/ol/div['+str(counter)+']/div/li/div[2]/div/div[1]'))
                try:
                    Aelements.append(self.driver.find_element_by_css_selector("section.tracklist-container:nth-child(1) > ol:nth-child(1) > div:nth-child("+str(counter)+") > div:nth-child(1) > li:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1) > span:nth-child(1) > span:nth-child(1) > a:nth-child(1)"))
                except:
                    Aelements.append(self.driver.find_element_by_css_selector("section.tracklist-container:nth-child(1) > ol:nth-child(1) > div:nth-child("+str(counter)+") > div:nth-child(1) > li:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(2) > span:nth-child(1) > span:nth-child(1) > a:nth-child(1)"))
                    
                counter+=1
                print(len(Aelements))
            except:
                break
        for i in range(len(Nelements)):

            self.names.append(Nelements[i].text)
            self.artists.append(Aelements[i].text)
    def getLinks(self):
        self.links=[]
        for i in range(len(self.names)):
            self.driver.get("https://www.youtube.com/results?search_query="+self.names[i]+' by '+self.artists[i])
            self.links.append(self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a').get_attribute("href"))  
            
    def downloadLinks(self):
        self.driver.get('https://ytmp3.cc/en13/')
        for i in self.links:
            
            self.driver.find_element_by_id('input').send_keys(i)
            self.driver.find_element_by_id('submit').click()
            while len(self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/a[1]').get_attribute("href"))<1:
                time.sleep(.5)
            self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/a[1]').click()
            self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/a[3]').click()

config = cp.ConfigParser()
config.read("SpotifyToMP3.ini")
try:
    if bool(config['SETTINGS']['firefox']):
	STY=spotifyToYoutube(webdriver.Firefox(),config)
    elif bool(config['SETTINGS']['chrome']):
	STY=spotifyToYoutube(webdriver.Chrome(),config)
    else:
	print("Please change your .ini file and set either chrome or firefox to true")
    STY.getStuff()
    STY.getLinks()
    STY.downloadLinks()
except:
    print("Please change your .ini file and set either chrome or firefox to true")



