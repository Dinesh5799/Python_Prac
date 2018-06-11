from selenium import webdriver
import time
import urllib.parse,urllib.error,urllib.request
import xml.etree.ElementTree as ET
import pyautogui

def coursera_login():
    try:
        course_name = input('Enter Course Name Exactly Shown As In Coursera: ')
        browser = webdriver.Chrome(executable_path=r"C:/Users/dines/Documents/chromedriver.exe")
        # browser = webdriver.Chrome('C:/Users/dines/Documents/chromedriver.exe')
        browser.get('https://www.coursera.org/?authMode=login')
        time.sleep(2)
        print('Successfully opened url')
        user = browser.find_element_by_id('emailInput-input')
        user.send_keys('dineshchunduspecial@gmail.com')
        print('No issue with email')
        password = browser.find_element_by_id('passwordInput-input')
        password.send_keys('Guessit')
        print('No issue with password')
        login = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div/span/div[2]/div/div[3]/div/div/div/div[2]/div/div[1]/form/div[1]/button')
        login.click()
        print('No issue with login')
        serviceurl = 'https://www.coursera.org/courses?languages=en&'
        course_name = course_name.lower()
        url = serviceurl + urllib.parse.urlencode({'query': course_name})
        print('URL = ', url)
        browser.get(url)
        # Introduction to Data Science in Python
        time.sleep(1)
        pyautogui.moveTo(450,450)
        pyautogui.click()
        for i in range(6):
            pyautogui.hotkey('tab')
        pyautogui.click()
        time.sleep(60)
    except Exception as e:
        print("Got into exception ", e)



coursera_login()
