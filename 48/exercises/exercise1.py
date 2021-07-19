from selenium import webdriver

chrome_driver_path="/mnt/d/Programs/Chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
url = "https://www.python.org"
driver.get(url)

times = [time.text for time in driver.find_elements_by_css_selector(".event-widget time")]
names = [name.text for name in driver.find_elements_by_css_selector(".event-widget a")]
events_ = zip(times, names)
events = {}
for i, event in enumerate(events_):
    events[i] = {"time": event[0], "name": event[1]}
print(events)

driver.quit() # quits entire program