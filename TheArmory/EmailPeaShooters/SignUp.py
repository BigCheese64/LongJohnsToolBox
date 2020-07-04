#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 16:31:44 2020

@author: alex
"""


from selenium import webdriver
class signUp():
    def __init__(self,email,driver):
        self.email=email
        self.driver=driver
        self.sites=["https://glc.yale.edu/","https://www.potterybarnkids.com/","https://www.catfaeries.com/newsletter.html","https://www.proflowers.com/",'https://secure.marthastewart.com/common/profile/quicksignup.jsp?internalSource=footer&lnkid=signup&referringID=1549813&referringContentType=home_page&regSource=10008','https://www.treehugger.com/news-4846010','https://www.retailmenot.com/holidays/cyber-monday','https://retailcodes.com/offers/cyber-monday','https://couponfollow.com/cybermonday']
        self.xpaths={"https://glc.yale.edu/":['//*[@id="edit-mergevars-email"]','//*[@id="edit-submit--2"]'],"https://www.potterybarnkids.com/":['//*[@id="footer-email-signup"]','/html/body/footer/div[1]/div/ul[4]/li[1]/form/div[2]/input'],"https://www.catfaeries.com/newsletter.html":['/html/body/div/div[4]/div[1]/div/div/div/div[2]/div/div[1]/table/tbody/tr/td/form/input[3]','/html/body/div/div[4]/div[1]/div/div/div/div[2]/div/div[1]/table/tbody/tr/td/form/input[4]'],"https://www.proflowers.com/":['//*[@id="signupEmail"]','/html/body/div[1]/footer/div[1]/div[3]/div[1]/div/div/button'],'https://secure.marthastewart.com/common/profile/quicksignup.jsp?internalSource=footer&lnkid=signup&referringID=1549813&referringContentType=home_page&regSource=10008':['//*[@id="firstName"]','//*[@id="regEmail"]','/html/body/div[1]/div/section/form/section[1]/div/input'],'https://www.treehugger.com/news-4846010':['//*[@id="mntl-newsletter-submit_1-0__input"]','//*[@id="mntl-newsletter-submit__button_1-0"]'],'https://www.retailmenot.com/holidays/cyber-monday':['/html/body/div[1]/div[1]/footer/div[1]/div/div/form/div[2]/input[6]','/html/body/div[1]/div[1]/footer/div[1]/div/div/form/div[2]/button'],'https://retailcodes.com/offers/cyber-monday':['//*[@id="ContactName"]','//*[@id="ContactEmailAddress"]','/html/body/div/div/div/div[3]/div/div[4]/form/button'],'https://couponfollow.com/cybermonday':['/html/body/main/section[2]/div[2]/section[1]/form/input','/html/body/main/section[2]/div[2]/section[1]/form/button']}
    def subscribe(self):
        for i in self.sites:
            self.driver.get(i)
            for j in range(len(self.xpaths[i])-1):
                self.driver.find_element_by_xpath(self.xpaths[i][j]).send_keys(self.email)
            self.driver.find_element_by_xpath(self.xpaths[i][-1]).click()
        

email=input(">Enter target email:\n>")
while True:
    cOrF=input(">Enter C if you have chrome installed or F for firefox:\n>")
    if cOrF.lower()=="c":
        driver=webdriver.Chrome()
        break
    elif cOrF.lower()=="f":
        driver=webdriver.Firefox()
        break
signUp(email,driver).subscribe()