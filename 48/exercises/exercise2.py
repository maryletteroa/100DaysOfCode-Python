from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path="/mnt/d/Programs/Chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# url = "https://en.wikipedia.org/wiki/Main_Page"
url="http://secure-retreat-92358.herokuapp.com"
driver.get(url)

# article_count = driver.find_element_by_css_selector("#articlecount a")
# print(article_count.text)
# article_count.click()


# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

fname = driver.find_element_by_name("fName")
fname.send_keys("test")
lname = driver.find_element_by_name("lName")
lname.send_keys("test")
email = driver.find_element_by_name("email")
email.send_keys("test@email.com")
submit = driver.find_element_by_css_selector("form button")
submit.click()
# driver.quit()