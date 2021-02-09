from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get('https://yandex.ru/')
driver.find_element_by_xpath("//input[@class = 'input__control "
                             "input__input mini-suggest__input']").send_keys('ViPNet Coordinator HW5000')
driver.find_element_by_xpath("//button[@class = 'button mini-suggest"
                             "__button button_theme_websearch button_size_ws-head i-bem button_js_inited']").click()
target = 'infotecs.ru›upload…db0/ViPNet_Coordinator_HW_5000…'
WebDriverWait(driver, 10).until(lambda d: d.find_element_by_xpath("//div[@class = 'path organic__path']/a"))
websites = driver.find_elements_by_xpath("//div[@class = 'path organic__path']/a")
for link in websites:
    if link.text == target:
        link.click()
        break