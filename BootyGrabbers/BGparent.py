from selenium import webdriver
import configparser as cp
class browserSelect():
    def __init__(self):
        config = cp.ConfigParser()
        config.read("BGsettingsMain.ini")
        try:
            if bool(config['SETTINGS']['firefox']):
                	self.driver=webdriver.Firefox()
            elif bool(config['SETTINGS']['chrome']):
                	self.driver=webdriver.Chrome()
            else:
                print("Please change your BGsettingsMain.ini file and set either chrome or firefox to true")
                self.driver=None
        except:
            print("Please change your BGsettingsMain.ini file and set either chrome or firefox to true")
            self.driver=None
    def returnDriver(self):
        return(self.driver)