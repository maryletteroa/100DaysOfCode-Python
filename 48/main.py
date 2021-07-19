from selenium import webdriver
from datetime import datetime


chrome_driver_path="/mnt/d/Programs/Chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
url="http://orteil.dashnet.org/experiments/cookie"
driver.get(url)

game_time = 0
cookie = driver.find_element_by_id("cookie")
items = driver.find_elements_by_css_selector("#store div")
store  = {}
for i, item in enumerate(items):
    store[i] = {
        "name": item.get_attribute("id"),
        "cost": item.find_element_by_css_selector("b").text.split(" ")[-1].replace(",",""),
    }
start_time = datetime.now()

while game_time < 5:
    cookie.click()
    now = datetime.now()
    time_diff = (now - start_time).seconds
    if time_diff != 0 and time_diff % 5 == 0:
        money = driver.find_element_by_id("money").text.replace(",","")
        for item in store:
            cost = store[item]["cost"]
            if cost != "" and int(money) >= int(cost):
                name = store[item]["name"]
        if name != "":
            driver.find_element_by_id(f"{name}").click()
        name = ""
    game_time = (now - start_time).total_seconds() / 60 

money = driver.find_element_by_id("money").text.replace(",","")
cps = driver.find_element_by_id("cps").text
print(f"Total score: {money}")
print(f"Cookies per second: {cps}")
driver.quit()