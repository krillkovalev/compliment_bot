from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def compliment():
    driver = webdriver.Chrome()
    driver.get('https://castlots.org/generator-komplimentov-devushke/')
    btn_element = driver.find_element(By.ID, 'random-button')
    btn_element.click()
    time.sleep(3)
    title = driver.find_element(By.CLASS_NAME, 'compliment')
    result = title.text
    return result


# if __name__ == '__main__':
#     compliment()
