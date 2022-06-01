from selenium import webdriver
import time

NUMBER_OF_COOKIES = 1000000
URL = 'https://orteil.dashnet.org/cookieclicker/'
    
#creating object of webdriver and passing driver location path to it
service = webdriver.firefox.service.Service('/Users/Dhruv/itrackr/geckodriver')
service.start()

#Creating driver object to load url
driver = webdriver.Remote(service.service_url)
driver.get(URL)
driver.implicitly_wait(15)
time.sleep(2)
driver.find_element_by_id("langSelect-EN").click()
time.sleep(2)
grandma_counter = 0
farm_counter = 0
i = 0
while True:
    i = i + 1
    driver.find_element_by_id("bigCookie").click()
    num_cookies = int(driver.find_element_by_id("cookies").text.split()[0].replace(',', ''))
    grandma_price = int(driver.find_element_by_id("productPrice1").text.replace(',', ''))
    try:
        farm_price = int(driver.find_element_by_id("productPrice2").text.replace(",", ""))
        #print("reached")
        if i == 1050:
            print(farm_price)
    except:
        farm_price = 1000
    
    if num_cookies >= grandma_price and grandma_counter < 5:
        time.sleep(0.5)
        driver.find_element_by_id("product1").click()
        grandma_counter = grandma_counter + 1
    elif num_cookies >= farm_price:
        time.sleep(0.5)
        driver.find_element_by_id("product2").click()
        farm_counter = farm_counter + 1
    if farm_counter > 2:
        grandma_counter = 0
        farm_counter = 0


time.sleep(20)
driver.quit()