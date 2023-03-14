from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def open_link():
    link = 'https://www.saucedemo.com/'
    driver = webdriver.Chrome()
    driver.get(link)

    try:
        driver.find_element(By.ID, 'user-name')
        driver.find_element(By.ID, 'password')
        driver.find_element(By.ID, 'login-button')
    except NoSuchElementException:
        return False
    return 'Элементы найдены'

    # if username is None or password is None or submit is None:
    #     print('Элементы не найдены')
    # else:
    #     print('Элементы найдены')


print(open_link())
