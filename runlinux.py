# -*- coding: utf-8 -*-
# Import libraries
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pyautogui import press, typewrite, hotkey
from xlwt import Workbook
from selenium.webdriver.common.keys import Keys

import os
import subprocess as sp
import requests
import time
import re
import xlsxwriter
import xlwt


def initializeJEN():
    global userSearchItemName, userSelectScanType
    #Run AI
    print('BOOTING JEN...')

    time.sleep(1)
    # WINDOWS tmp = sp.call('cls',shell=True)
    # LINUX tmp = sp.call('clear',shell=True)
    tmp = sp.call('clear',shell=True)
    print("Jen is ready.")

    #Ask user for target item to look for
    userSearchItemName = input("Please enter the item you would like to search: ")
    pickItem()


def pickItem():
    global userSearchItemName, userSelectScanType, userAliExpressLoginEmail, userAliExpressLoginPassword, userEbayLoginEmail, userEbayLoginPassword
    #Select AI search intensity
    print("Please select type of scan (1-4): ")
    print("1 - Amazon (Best and Cheapest Item Scan)")
    print("2 - AliExpress -> Ebay Listing (Find item at good price, list it immediately on eBay)")

    userSelectScanType = input("Selection: ")

    #Validate Entered Selection to be an Int and a valid option

    if userSelectScanType.startswith('1'):
        print("You chose Amazon item Scan.")
        time.sleep(1)
        tmp = sp.call('clear',shell=True)
        print("INITIALIZING SCAN.")
        time.sleep(1)
        tmp = sp.call('clear',shell=True)
        print("INITIALIZING SCAN..")
        time.sleep(1)
        tmp = sp.call('clear',shell=True)
        print("INITIALIZING SCAN...")
        time.sleep(1)
        tmp = sp.call('clear',shell=True)
        print("INITIALIZING SCAN.")
        time.sleep(1)
        #We passed the checkpoints to lets start searching
        amazonWebBestandCheapItemScan()
    elif userSelectScanType.startswith('2'):
        print("You chose AliExpress -> Ebay Listing [Auto]")
        time.sleep(1)
        tmp = sp.call('clear',shell=True)
        # userAliExpressLoginEmail = input("Enter AliExpress Login Email: ")
        # userAliExpressLoginPassword = input("Enter AliExpress Login Password: ")
        # userEbayLoginEmail = input("Enter Ebay Login Email: ")
        # userEbayLoginPassword = input("Enter Ebay Login Password: ")

        userAliExpressLoginEmail = "bartek8991@live.com"
        userAliExpressLoginPassword = "Password1234"
        userEbayLoginEmail = ""
        userEbayLoginPassword = ""
        print("INITIALIZING SCAN.")
        time.sleep(1)
        tmp = sp.call('clear',shell=True)
        time.sleep(0.1)
        print("INITIALIZING SCAN..")
        time.sleep(1)
        tmp = sp.call('clear',shell=True)
        time.sleep(0.1)
        print("INITIALIZING SCAN...")
        time.sleep(1)
        tmp = sp.call('clear',shell=True)
        time.sleep(0.1)

        #We passed the checkpoints to lets start searching
        aliExpressToEbayAutomation()
    elif userSelectScanType.startswith('3'):
        print("You chose ENDOME SCAN (Intelligence beyound human knowledge)")
    else:
        print("You idiot.")
        time.sleep(1)
        shutdown()


def amazonWebBestandCheapItemScan():
    global userSearchItemName, userSelectScanType, userAliExpressLoginEmail, userAliExpressLoginPassword, userEbayLoginEmail, userEbayLoginPassword, numofitems, numofprices, numofgucciprice, numofratings, sheet1, wb, scannedItemPrice, scannedItemRating
    tmp = sp.call('clear',shell=True)
    print("Running...")

    targetDatabaseURL = 'https://www.amazon.com'

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
    numofprices = 0
    numofratings = 0
    numofgucciprice = 0

    #Enter search box
    element = driver.find_element_by_xpath("//input[@value='Go']")
    element.click()

    time.sleep(1)

    #Run through FIRST PAGE (important because this is a loop) ever price and find the best option based on lowest legit price and good ratio reviews
    howManyRuns = 1
    pageNum = 1

    # Workbook is created
    wb = Workbook()

    # add_sheet is used to create sheet.
    sheet1 = wb.add_sheet('Sheet 1')

    for pageNum in range(howManyRuns):
        pageNum += 1

        #Item Name of the Product
        itemName = driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
        for everyItem in itemName:
            numofitems += 1

            vare = everyItem.get_attribute('innerHTML')

            time.sleep(0.01)

            sheet1.write(numofitems, 0, vare)

            #newvare = vare.replace(".", "")
            print("Product:", vare)

        #Item Price of the Product
        itemPrice = driver.find_elements_by_xpath("//span[@class='a-offscreen']")
        for everyItem2 in itemPrice:
            numofprices += 1

            scannedItemPrice = everyItem2.get_attribute('innerHTML')
            #sheet1.write(1, 0, 'ISBT DEHRADUN')

            time.sleep(0.01)

            #sheet1.write(numofprices, 1, scannedItemPrice)

            #newvare = vare.replace(".", "")
            print("Cost: ", scannedItemPrice)

        #Item Rating of the Product
        itemRating = driver.find_elements_by_xpath("//span[@class='a-icon-alt']")
        for everyItem3 in itemRating:
            numofratings += 1

            scannedItemRating = everyItem3.get_attribute('innerHTML')

            time.sleep(0.01)

            #sheet1.write(numofprices, 3, scannedItemRating)

            #newvare = vare.replace(".", "")
            print("Rating: ", scannedItemRating)

        time.sleep(3)

        #next page and loop
        driver.get(driver.current_url+"&page="+str(pageNum))

    #Write the file with collected data
    wb.save(str(userSearchItemName)+'_LIST.xlsx')

    time.sleep(2)
    print("Jen has finished scanning!")
    time.sleep(2)
    print("Scanned", numofitems,"products. Found", numofgucciprice, "with a great price. Check log file `dropLIST.txt`")
    print("Shutting down..")
    time.sleep(3)
    #Close browser. We are done searching.
    driver.quit()


def aliExpressToEbayAutomation():
    global userSearchItemName, userSelectScanType, userAliExpressLoginEmail, userAliExpressLoginPassword, userEbayLoginEmail, userEbayLoginPassword, numofitems, numofprices, numofgucciprice, numofratings, sheet1, wb, scannedItemPrice, scannedItemRating
    tmp = sp.call('clear',shell=True)
    print("Running...")

    targetDatabaseURL = 'https://www.aliexpress.com/'

    #Execute Scan
    driver = webdriver.Chrome()
    #Load page
    driver.get(targetDatabaseURL)
    time.sleep(3)
    #Page Loaded, check if popup is in the way. delete if so
    element = driver.find_element_by_xpath("//a[@class='close-layer']")
    element.click()

    time.sleep(0.5)

    #Sign in so we can search
    element = driver.find_element_by_xpath("//a[@data-role='myaliexpress-link']")
    element.click()
    time.sleep(1)
    element = driver.find_element_by_xpath("//a[@data-role='sign-link']")
    element.click()
    time.sleep(2)

    for x in range(0, 2):
        time.sleep(0.2)
        driver.switch_to_active_element().send_keys(Keys.TAB)

    time.sleep(1)
    typewrite(userAliExpressLoginEmail)
    time.sleep(2)

    for x in range(0, 1):
        time.sleep(0.2)
        driver.switch_to_active_element().send_keys(Keys.TAB)

    typewrite(userAliExpressLoginPassword)
    time.sleep(2)

    for x in range(0, 1):
        time.sleep(0.2)
        driver.switch_to_active_element().send_keys(Keys.ENTER)

    time.sleep(5)

    element = driver.find_element_by_xpath("//a[@class='close-layer']")
    element.click()
    time.sleep(2)
    element = driver.find_element_by_xpath("//input[@class='search-key']")
    element.click()
    time.sleep(2)
    typewrite(userSearchItemName)
    time.sleep(2)
    element = driver.find_element_by_xpath("//input[@class='search-button']")
    element.click()

    os.system("pause")
    time.sleep(0.5)

    element = driver.find_element_by_xpath("//input[@id='search-key']")
    element.click()

    time.sleep(2)

    #Enter item to search using fake paste
    typewrite(userSearchItemName)
    time.sleep(2)

    numofitems = 0
    numofprices = 0
    numofratings = 0
    numofgucciprice = 0

    #Enter search box
    element = driver.find_element_by_xpath("//input[@class='search-button']")
    element.click()

    time.sleep(1)

    #Run through FIRST PAGE (important because this is a loop) ever price and find the best option based on lowest legit price and good ratio reviews
    howManyRuns = 1
    pageNum = 1

    # Workbook is created
    wb = Workbook()

    # add_sheet is used to create sheet.
    sheet1 = wb.add_sheet('Sheet 1')

    for pageNum in range(howManyRuns):
        pageNum += 1

        #Item Name of the Product
        itemName = driver.find_elements_by_xpath("//a[@class='item-title']")
        for everyItem in itemName:
            numofitems += 1

            vare = everyItem.get_attribute('innerHTML')

            time.sleep(0.01)

            sheet1.write(numofitems, 0, vare)

            #newvare = vare.replace(".", "")
            print("Product:", vare)

        #Item Price of the Product
        itemPrice = driver.find_elements_by_xpath("//span[@class='price-current']")
        for everyItem2 in itemPrice:
            numofprices += 1

            scannedItemPrice = everyItem2.get_attribute('innerHTML')
            #sheet1.write(1, 0, 'ISBT DEHRADUN')

            time.sleep(0.01)

            #sheet1.write(numofprices, 1, scannedItemPrice)

            #newvare = vare.replace(".", "")
            print("Cost: ", scannedItemPrice)

        #Item Rating of the Product
        itemRating = driver.find_elements_by_xpath("//span[@class='rating-value']")
        for everyItem3 in itemRating:
            numofratings += 1

            scannedItemRating = everyItem3.get_attribute('innerHTML')

            time.sleep(0.01)

            #sheet1.write(numofprices, 3, scannedItemRating)

            #newvare = vare.replace(".", "")
            print("Rating: ", scannedItemRating)

        time.sleep(3)

        #next page and loop
        driver.get(driver.current_url+"&page="+str(pageNum))

    #Write the file with collected data
    wb.save(str(userSearchItemName)+'_LIST.xlsx')

    time.sleep(2)
    print("Jen has finished scanning!")
    time.sleep(2)
    print("Scanned", numofitems,"products. Found", numofgucciprice, "with a great price. Check log file `dropLIST.txt`")
    print("Shutting down..")
    time.sleep(3)
    #Close browser. We are done searching.
    driver.quit()


def shutdown():
    exit()


initializeJEN()
