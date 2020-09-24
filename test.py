#=================================================

#================================================

import requests as res
import bs4
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
 
import time
# import requests



def function():


    options = Options()
    options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    #options=webdriver.ChromeOptions()
    #options.add_argument('--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    #options.add_argument('--profile-directory=Default')
    print("reached Here")
    driver = webdriver.Chrome( "C:\\Users\\Administrator\\Downloads\\chromedriver_win32\\chromedriver",chrome_options = options)
    while True:
        try:
            driver.get('https://stackoverflow.com/')
            break
        except:
            pass
    while True:
        try:
            loginButton=driver.find_element_by_xpath("/html/body/header/div/ol[2]/li[2]/a[1]")
            loginButton.click()
            break
        except:
            pass
    while True:
        try:
            googleSignInButton=driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/button[1]")
            googleSignInButton.click()
            break
        except:
            pass
    time.sleep(4)
    while True:
        try :
            mailId = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
            mailId.send_keys('vishnudk179@gmail.com',Keys.ENTER)
            break
        except:
            pass
    
    # passwrdButton=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/button")
    # passwrdButton.click()
    # time.sleep(4)
    # passwrdButton2=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[2]/div")
    # passwrdButton2.click()
    time.sleep(4)
    while True:
        try:
            passwrdBar=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
            passwrdBar.send_keys("Bs1@3^$1fDg%&Sds'",Keys.ENTER)
            break
        except:
            pass
    time.sleep(4)
    while True:
            while True:
                try:
                    driver.get('https://youtu.be/aSMjYwCkCUw')
                    break
                except:
                    pass
            while True:
                try:

                    currentNoVeiws = driver.find_element_by_xpath(" //*[@id='count']/yt-view-count-renderer/span[1]")  #("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[5]/div[2]/ytd-video-primary-info-renderer/div/div/div[1]/div[1]/yt-view-count-renderer/span[1]")
                
                    # //*[@id="count"]/yt-view-count-renderer/span[1]
                                                                #    /html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[1]/div[1]/yt-view-count-renderer/span[2]
                                                                #    /html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[5]/div[2]/ytd-video-primary-info-renderer/div/div/div[1]/div[1]/yt-view-count-renderer/span[1]
                    break
                except:
                    pass
            cv = currentNoVeiws.text
            print(cv)
            # /html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/ytcp-video-row[7]/div/div[6]

            # print(currentNoVeiws.text)
            # checkButton = driver.find_element_by_xpath("/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/ytcp-video-row[7]/div/div[1]/ytcp-checkbox-lit/div")
            # checkButton.click()
            # editButton = driver.find_element_by_xpath("/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/div[1]/div/ytcp-video-bulk-actions/ytcp-bulk-actions/div[1]/span/ytcp-select/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger/div/div[3]/iron-icon")
            # editButton.click()
            # titleButton = driver.find_element_by_xpath("/html/body/ytcp-text-menu/paper-dialog/paper-listbox/paper-item[1]/ytcp-ve/div")
            # titleButton.click()
            while True:
                try:
                    driver.get("https://studio.youtube.com/video/aSMjYwCkCUw/edit/basic?c=UCXJXRZSGnb5UQYm3kXcTRFw")
                    break
                except:
                    pass
            while True:
                try:        
                    titleBar = driver.find_element_by_xpath("/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-metadata-editor-section/ytcp-video-metadata-editor-old/div/ytcp-animatable/ytcp-video-metadata-basics-old/div/div[1]/div[1]/ytcp-mention-textbox/ytcp-form-input-container/div[1]/div[2]/ytcp-mention-input/div")
                    break
                except:
                    pass

            noOfviews="The no of views of this video is "+str(cv)
            titleBar.send_keys(Keys.CONTROL, 'a')
            titleBar.send_keys(noOfviews)
            try:
                updateButton = driver.find_element_by_xpath("/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-metadata-editor-section/ytcp-video-metadata-editor-old/div/ytcp-sticky-header/ytcp-primary-action-bar/div/div[2]/ytcp-button[2]")
                updateButton.click()
            except:
                pass
            # confirmationCheckBox = driver.find_element_by_xpath("/html/body/ytcp-confirmation-dialog/ytcp-dialog/paper-dialog/div[2]/div/div[2]/div/label/ytcp-checkbox-lit/div")
            # confirmationCheckBox.click()
            # confirmationButton = driver.find_element_by_xpath("/html/body/ytcp-confirmation-dialog/ytcp-dialog/paper-dialog/div[3]/div[2]/ytcp-button[2]")
            # confirmationButton.click()
            time.sleep(5)

if __name__ == "__main__":
    function()