# designed for Python 2
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import os
import time

MAIN_URL = 'https://www.linkedin.com/'
URL = 'https://www.linkedin.com/mynetwork/'
UNAME = os.environ.get('linkedin_uname')
PASS = os.environ.get('linkedin_pass')

def setup_driver():
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
        "(KHTML, like Gecko) Chrome/15.0.87"
    )
    driver = webdriver.PhantomJS(desired_capabilities=dcap)
    driver.set_window_size(1920, 1080)
    driver.set_page_load_timeout(15)
    return driver

if __name__ == "__main__":
    if None in [UNAME, PASS]:
        UNAME = raw_input('enter linkedin username:\n')
        PASS = raw_input('enter linkedin password:\n')

    # first, login
    driver = setup_driver()
    driver.get(MAIN_URL)
    ## save page for inspection
    with open('test.html', 'w') as f:
         f.write(driver.page_source.encode('ascii', 'ignore'))

    login_id = driver.find_element_by_id('login-email')
    login_id.send_keys(UNAME)
    login_pass = driver.find_element_by_id('login-password')
    login_pass.send_keys(PASS)
    login_pass.send_keys(Keys.ENTER) #submits form
    time.sleep(3)
    driver.get(URL)
    soup = bs(driver.page_source, 'lxml')
    button_class = 'mn-person-card__person-btn-ext'
    soup.find_all({'class':button_class})
