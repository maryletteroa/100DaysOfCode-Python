from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
import time


url = "https://www.linkedin.com"
chrome_driver_path="/mnt/d/Programs/Chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

# sign-in
email = os.environ.get("email")
password = os.environ.get("password")
driver.find_element_by_xpath("/html/body/nav/div/a[2]").click()
driver.find_element_by_xpath('//*[@id="username"]').send_keys(email)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()
try:
    # do not remember
    driver.find_element_by_xpath('//*[@id="remember-me-prompt__form-secondary"]/button').click()
except NoSuchElementException:
    pass
try:
    # skip phone
    driver.find_element_by_xpath('//*[@id="ember455"]/button').click()
except NoSuchElementException:
    pass


# search
search_term = '"python developer"' + Keys.ENTER
driver.find_element_by_xpath('//*[@id="global-nav-typeahead"]/input').send_keys(search_term)
sleep_n = 5
# select jobs, remote, easy apply
# sleep every filter to allow the page to load
# use full xpath as the button ids tend to change with every reload
time.sleep(sleep_n)
driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div[2]/section/div/nav/div/ul/li[2]/button").click()
time.sleep(sleep_n)
driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[3]/section/div/div/div/ul/li[7]/div/button").click()
time.sleep(sleep_n)
driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[3]/section/div/div/div/ul/li[8]/div/button").click()

# loop through results
time.sleep(sleep_n)
results = driver.find_elements_by_class_name("jobs-search-results__list-item")
for result in results:
    result.click()
    try:
        # easy apply button is present
        driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[3]/div/div/section[2]/div/div/div[1]/div/div[1]/div/div[2]/div[3]/div/div/div/button").click()
        try:
            # there is no Next button
            # submit the application
            driver.find_element_by_link_text("Submit application").click()
            driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/form/footer/div[1]/input").click()
        except NoSuchElementException:
            pass
        # close
        driver.find_element_by_xpath("/html/body/div[3]/div/div/button").click()
        try:
            # and discard
            driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[3]/button[1]").click()
        except NoSuchElementException:
            pass
    except NoSuchElementException:
        pass

