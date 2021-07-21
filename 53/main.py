from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import os

ZILLOW_LISTING_URL = os.environ.get("ZILLOW_LISTING_URL")
GOOGLE_FORM_URL = os.environ.get("GOOGLE_FORM_URL")

# ---- zillow ---- #
chrome_driver_path="/mnt/d/Programs/Chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(ZILLOW_LISTING_URL)
driver.maximize_window()

# click on a clickable element on right pane
# scroll for n seconds (to the bottom of the page to load everything)
# can be replaced with scrolling till element
next = True
scroll_time = 10
wait_time = 10
page_num = 1
listings = {}
records = 0 # total number of parsed records
bef_link = ""
while next:
    
    # driver.implicitly_wait(wait_time)
    sort_button = driver.find_element_by_xpath('//*[@id="sort-popover"]')
    driver.implicitly_wait(wait_time)
    ActionChains(driver).move_to_element(sort_button).click(sort_button).perform()
    ActionChains(driver).move_to_element(sort_button).click(sort_button).perform()
    total_time = 0
    start_time = datetime.now()
    while total_time < scroll_time:
        sort_button.send_keys(Keys.DOWN)
        now = datetime.now()
        total_time = (now - start_time).total_seconds()

    # get information
    addresses = driver.find_elements_by_class_name("list-card-addr")
    prices = driver.find_elements_by_class_name("list-card-price")
    urls = driver.find_elements_by_css_selector(".list-card-info a")

    for i, address in enumerate(addresses):
        n = i + records
        listings[n] = {"address": addresses[i].text,
            "price": prices[i].text,
            "url": urls[i].get_attribute("href"),}

    num_listings_in_page = len(addresses)
    print(f"Page: {page_num}, {num_listings_in_page} listings")
    page_num +=1
    records += num_listings_in_page

    next_button = driver.find_element_by_xpath('//*[@id="grid-search-results"]/div[2]/nav/ul/li[10]/a')
    next_button_link = next_button.get_attribute("href")
    if bef_link != next_button_link:
        next_button.click()
        bef_link = next_button_link
    else:
        next = False

driver.quit()

print(f"Total listings recorded: {records}")


# ---- google sheets ---- #
# driver needs to be reinitialized
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(GOOGLE_FORM_URL)
driver.maximize_window()

for listing in listings:
    print(f"Listing {listing + 1} / {records} ...", end="\r")
    address_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(listings[listing]["address"])
    price_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(listings[listing]["price"])
    url_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    url_input.send_keys(listings[listing]["url"])
    submit_btn = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit_btn.click()
    another_response = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()

driver.quit()


