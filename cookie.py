from selenium import webdriver
import time


URL = 'https://orteil.dashnet.org/cookieclicker/'
    
#creating object of webdriver and passing driver location path to it
service = webdriver.firefox.service.Service('/Users/Dhruv/itrackr/geckodriver')
service.start()

#Creating driver object to load url
driver = webdriver.Remote(service.service_url)
driver.get(URL)
driver.implicitly_wait(15)
time.sleep(2)

# Selecting the language in the landing page
driver.find_element_by_id("langSelect-EN").click()
time.sleep(2)
grandma_counter = 0
farm_counter = 0
mine_counter = 0
factory_counter = 0
# Starting the Game Loop
while True:

    # Clicking the Cookie button
    driver.find_element_by_id("bigCookie").click()

    # Getting number of cookies
    num_cookies = int(driver.find_element_by_id("cookies").text.split()[0].replace(',', ''))
    
    # Getting the prices of the diffeent buildings
    try:
        grandma_price = int(driver.find_element_by_id("productPrice1").text.replace(',', ''))
        farm_price = int(driver.find_element_by_id("productPrice2").text.replace(",", ""))
        mine_price = int(driver.find_element_by_id("productPrice3").text.replace(",", ""))
        factory_price = int(driver.find_element_by_id("productPrice4").text.replace(",", ""))
    except:
        grandma_price = 100
        farm_price = 1000
        mine_price = 100000
        factory_price = 1000000
    
    # Clicking the building based on the strategy and number of cookies
    if num_cookies >= grandma_price and grandma_counter < 10:
        time.sleep(0.5)
        driver.find_element_by_id("product1").click()
        grandma_counter = grandma_counter + 1
    elif num_cookies >= farm_price and farm_counter < 10:
        time.sleep(0.5)
        driver.find_element_by_id("product2").click()
        farm_counter = farm_counter + 1
    elif num_cookies >= mine_price and mine_counter < 10:
        time.sleep(0.5)
        driver.find_element_by_id("product3").click()
        mine_counter = mine_counter + 1
    elif num_cookies >= factory_price:
        time.sleep(0.5)
        driver.find_element_by_id("product4").click()
        factory_counter = factory_counter + 1

# Ending the game (this is currently of no use but can employ in the future)
time.sleep(20)
driver.quit()