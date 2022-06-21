import os
import time
import webbrowser
import urllib.request
import selenium
from selenium import webdriver

#download necessary chromedriver.exe
urllib.request.urlretrieve("https://monke.academy/WorkAssets/chromedriver.exe", "chromedriver.exe")

#constants
YOUTUBE_URL = "https://www.youtube.com/"
SEARCH_URL = YOUTUBE_URL + "results?search_query="

#initialize driver
driver = webdriver.Chrome()

#prompt user for input
search_term = input("What would you like to search for on YouTube?\n")

#search youtube
driver.get(SEARCH_URL + search_term)

#wait for page to load
time.sleep(2)

#find top video
first_video = driver.find_element_by_id("video-title")

#extract link to video
video_link = first_video.get_attribute("href")

#open link in new window
webbrowser.open_new_tab(video_link)

#close driver
driver.quit()
