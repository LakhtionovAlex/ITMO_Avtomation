from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://demoqa.com/"
driver = webdriver.Chrome()
driver.get(link)



icon = driver.find_element(By.CSS_SELECTOR, 'span')
button = driver.find_element(By.CSS_SELECTOR, 'div.home-body > div > div:nth-child(1)')
footer_text = driver.find_element(By.CSS_SELECTOR, 'span')


if icon is None or button is None or footer_text is None:
    print('Элемент не найден')
else:
    print('Элемент найден')
