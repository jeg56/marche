
import re

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui 
from bs4 import BeautifulSoup
import time

import codecs


def main():
    url='http://annuaire.marchesdefrance.fr/liste-des-marches/'

    # create a new Firefox session


    options = Options()
    options.headless = True
 
    browser = webdriver.Firefox(options=options,executable_path="/home/jeg/Programmes/Selenium/geckodriver-v0.26.0-linux64/geckodriver")

    browser.get("http://www.google.com")
    # Navigate to the application home page
    reponse=browser.get("http://www.google.com")
    print(reponse.context)
main()