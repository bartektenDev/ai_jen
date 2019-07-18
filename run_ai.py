# -*- coding: utf-8 -*-
# Import libraries
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pyautogui import press, typewrite, hotkey

import subprocess as sp
import requests
import time
import re

#DEFINE
targetDatabaseURL = 'https://www.amazon.com'


def initializeJEN():
    global userSearchItemName, userSearchIntensity
    #Run AI
    print('BOOTING JEN...')

    time.sleep(3)
    # WINDOWS tmp = sp.call('cls',shell=True)
    # LINUX tmp = sp.call('clear',shell=True)
    tmp = sp.call('cls',shell=True)
    print("Jen is ready.")

    #Ask user for target item to look for
    userSearchItemName = input("Please enter the item you would like to search: ")
    pickItem()


def pickItem():
    global userSearchItemName, userSearchIntensity
    #Select AI search intensity
    print("Please enter intensity of search on scale 1 - 3")
    print("1 - Quick Light Scan")
    print("2 - Sherlock Holmes Scan")
    print("3 - ENDOME SCAN (Intelligence beyound human knowledge)")

    userSearchIntensity = input("Selection: ")

    #Validate Entered Selection to be an Int and a valid option

    if userSearchIntensity.startswith('1'):
        print("You chose Quick Light Scan")
        time.sleep(2)
        #We passed the checkpoints to lets start searching
        executeJENSCAN1()
    elif userSearchIntensity.startswith('2'):
        print("You chose Sherlock Holmes Scan")
    elif userSearchIntensity.startswith('3'):
        print("You chose ENDOME SCAN (Intelligence beyound human knowledge)")
    else:
        print("You idiot.")
        shutdown()


def executeJENSCAN1():
    global userSearchItemName, userSearchIntensity, numofitems, numofgucciprice
    tmp = sp.call('cls',shell=True)
    print("Running...")

    #Execute Scan
    driver = webdriver.Chrome()
    #Load page
    driver.get(targetDatabaseURL)
    #Page Loaded, click on  the search box
    element = driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
    element.click()

    time.sleep(2)

    #Enter item to search using fake paste
    typewrite(userSearchItemName)
    time.sleep(2)

    numofitems = 0
    numofgucciprice = 0

    #Enter search box
    element = driver.find_element_by_xpath("//input[@value='Go']")
    element.click()

    time.sleep(1)

    #Run through FIRST PAGE (important because this is a loop) ever price and find the best option based on lowest legit price and good ratio reviews
    howManyRuns = 5
    pageNum = 0
    for pageNum in range(howManyRuns):
        pageNum += 1
        itemName = driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
        for everyItem in itemName:
            numofitems += 1

            vare = everyItem.get_attribute('innerHTML')

            time.sleep(0.01)
            #newvare = vare.replace(".", "")
            print("Product:", vare)

        itemPrice = driver.find_elements_by_xpath("//span[@class='a-offscreen']")
        for everyItem2 in itemPrice:

            scannedItemName = everyItem2.get_attribute('innerHTML')

            time.sleep(0.01)
            #newvare = vare.replace(".", "")
            print("Cost: ", scannedItemName)

        itemLink = driver.find_elements_by_xpath("//span[@class='a-offscreen']")
        for everyItem2 in itemPrice:

            scannedItemName = everyItem2.get_attribute('innerHTML')

            time.sleep(0.01)
            #newvare = vare.replace(".", "")
            print("Cost: ", scannedItemName)

        time.sleep(3)
        
        #next page and loop
        driver.get(driver.current_url+"&page="+str(pageNum))


    # listOfItemsStars = driver.find_elements_by_class_name('a-icon-alt')
    # for everyRating in listOfItemsStars:
    #     vare = everyRating.get_attribute('innerHTML')
    #     time.sleep(0.2)
    #     #newvare = vare.replace("", "")
    #     print("Rating: " + vare + "")


    time.sleep(2)
    print("Jen has finished scanning!")
    time.sleep(2)
    print("Scanned", numofitems,"products. Found ",numofgucciprice,"with a great price. Check log file `dropLIST.txt`")
    print("Shutting down in 3 seconds..")
    time.sleep(3)
    #Close browser. We are done searching.
    driver.quit()

def shutdown():
    exit()


initializeJEN()
