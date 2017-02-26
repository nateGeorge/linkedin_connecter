# designed for Python 2
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup as bs
import os

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
    return driver

if __name__ == "__main__":
    if None in [UNAME, PASS]:
        UNAME = raw_input('enter linkedin username:\n')
        PASS = raw_input('enter linkedin password:\n')

    driver = setup_driver()
    driver.get(URL)
    res = driver.page_source
    soup = bs(res)
    button_class = 'mn-person-card__person-btn-ext'
    soup.find_all({'class':button_class})