from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("https://www.amazon.com")
time.sleep(10)
# assert "Python" in driver.title
elem = driver.find_element_by_name("field-keywords")
elem.clear()
elem.send_keys("playstation")
elem.send_keys(Keys.RETURN)
time.sleep(10)
elems = driver.find_elements_by_class_name("sg-col-inner")
print(elems)
# assert "No results found." not in driver.page_source
# driver.close()

for elements in elems:
    title_data = elements.find_elements_by_class_name("a-size-medium a-color-base a-text-normal")
    print((elements.text).split("\n"))
