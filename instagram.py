import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By


INSTA_USERNAME = "devmarvis"
INSTA_PASS = "e1506441*"
SEARCH_QUERY = "spotify"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

INSTA_URL = "http://instagram.com"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(INSTA_URL)

        time.sleep(5)

        username_input = self.driver.find_element(By.NAME, value="username")
        username_input.send_keys(INSTA_USERNAME)

        password_input = self.driver.find_element(By.NAME, value="password")
        password_input.send_keys(INSTA_PASS)

        login_btn = self.driver.find_element(By.CSS_SELECTOR, value="button[type='submit']")
        login_btn.click()

        # time.sleep(5)

    def find_followers(self):
        search_btn = self.driver.find_elements(By.CSS_SELECTOR, value='div.x1iyjqo2.xh8yej3 > div')
        search_btn[1].click()
        time.sleep(2)

        search_input = self.driver.find_element(By.CSS_SELECTOR, value='input[aria-label="Search input"]')
        search_input.send_keys(SEARCH_QUERY)
        time.sleep(3)
        # x78zum5 xdt5ytf x5yr21d
        top_results = self.driver.find_elements(By.CSS_SELECTOR, value='div.x78zum5.xdt5ytf.x5yr21d a')
        top_results[0].click()

        # time.sleep(4)

    def follow(self):
        followers_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, value="followers")
        followers_link.click()

        time.sleep(5)

        follow_btns = self.driver.find_elements(By.CSS_SELECTOR, value="button._acan._acap._acas._aj1-._ap30")
        # print(follow_btns)

        time.sleep(3)

        for follow_btn in follow_btns[1:11]:
            try:
                follow_btn.click()
            except ElementClickInterceptedException:
                time.sleep(1)
                follow_btn.click()
            finally:
                time.sleep(1.5)

        close_pop = self.driver.find_element(By.CSS_SELECTOR, "button._abl-")
        close_pop.click()