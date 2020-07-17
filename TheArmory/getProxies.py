#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 13:55:07 2020

@author: alex
"""


from selenium import webdriver

class getProxies():
    def __init__(self):
        site="https://free-proxy-list.net/"
        driver=webdriver.Firefox()    
        driver.get(site)
        self.ips=[]
        self.ports=[]
        for j in range(15):
            for i in range(20):
                i=i+1
                e=driver.find_element_by_xpath('/html/body/section[1]/div/div[2]/div/div[2]/div/table/tbody/tr['+str(i)+']/td[1]')
                self.ips.append(e.text)
                e=driver.find_element_by_xpath('/html/body/section[1]/div/div[2]/div/div[2]/div/table/tbody/tr['+str(i)+']/td[2]')
                self.ports.append(e.text)
            driver.find_element_by_xpath("/html/body/section[1]/div/div[2]/div/div[3]/div[2]/div/ul/li[10]/a").click()
        driver.close()
    def returnIPs(self):
        return(self.ips)
    def returnPorts(self):
        return(self.ports)
