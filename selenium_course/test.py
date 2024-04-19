from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import unittest
import math
import pytest


# link = "https://easysmarthub.ru/contact/"

# def test_1():
#     try:
#         browser = webdriver.Chrome()
#         browser.get(link)
#         input_1 = browser.find_element(By.CSS_SELECTOR, "[name='your-name']")
#         input_1.send_keys()
#         input_2 = browser.find_element(By.CSS_SELECTOR, "[name='your-email']")
#         input_2.send_keys()
#         input_3 = browser.find_element(By.CSS_SELECTOR, "[name='your-subject']")
#         input_3.send_keys()
#         input_4 = browser.find_element(By.CSS_SELECTOR, "[name='your-message']")
#         input_4.send_keys()
#         button_1 = browser.find_element(By.CSS_SELECTOR, "[name='gdpr']")
#         button_1.click()
#         button_2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")    
#         button_2.click()
#     finally:
#         time.sleep(7)
#         browser.quit()

# if __name__ == "__main__":
#     test_1()



# def test_2():
#     try:
#         browser = webdriver.Chrome()
#         browser.get(link)
#         input_1 = browser.find_element(By.CSS_SELECTOR, "[name='your-name']")
#         input_1.send_keys('Yana')
#         input_2 = browser.find_element(By.CSS_SELECTOR, "[name='your-email']")
#         input_2.send_keys()
#         input_3 = browser.find_element(By.CSS_SELECTOR, "[name='your-subject']")
#         input_3.send_keys()
#         input_4 = browser.find_element(By.CSS_SELECTOR, "[name='your-message']")
#         input_4.send_keys()
#         button_1 = browser.find_element(By.CSS_SELECTOR, "[name='gdpr']")
#         button_1.click()
#         button_2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")    
#         button_2.click()
#     finally:
#         time.sleep(7)
#         browser.quit()

# if __name__ == "__main__":
#     test_2()


# def test_3():
#     try:
#         browser = webdriver.Chrome()
#         browser.get(link)
#         input_1 = browser.find_element(By.CSS_SELECTOR, "[name='your-name']")
#         input_1.send_keys('Yana')
#         input_2 = browser.find_element(By.CSS_SELECTOR, "[name='your-email']")
#         input_2.send_keys('Yana')
#         input_3 = browser.find_element(By.CSS_SELECTOR, "[name='your-subject']")
#         input_3.send_keys('Yana')
#         input_4 = browser.find_element(By.CSS_SELECTOR, "[name='your-message']")
#         input_4.send_keys('Yana')
#         button_1 = browser.find_element(By.CSS_SELECTOR, "[name='gdpr']")
#         button_1.click()
#         button_2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")    
#         button_2.click()
#     finally:
#         time.sleep(7)
#         browser.quit()

# if __name__ == "__main__":
#     test_3()


# def test_4():
#     try:
#         browser = webdriver.Chrome()
#         browser.get(link)
#         input_1 = browser.find_element(By.CSS_SELECTOR, "[name='your-name']")
#         input_1.send_keys('Yana')
#         input_2 = browser.find_element(By.CSS_SELECTOR, "[name='your-email']")
#         input_2.send_keys('Yana@yandex.ru')
#         input_3 = browser.find_element(By.CSS_SELECTOR, "[name='your-subject']")
#         input_3.send_keys('Yana')
#         input_4 = browser.find_element(By.CSS_SELECTOR, "[name='your-message']")
#         input_4.send_keys('Yana')
#         button_2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")    
#         button_2.click()
#     finally:
#         time.sleep(7)
#         browser.quit()

# if __name__ == "__main__":
#     test_4()


# def test_5():
#     try:
#         browser = webdriver.Chrome()
#         browser.get(link)
#         input_1 = browser.find_element(By.CSS_SELECTOR, "[name='your-name']")
#         input_1.send_keys('Yana')
#         input_2 = browser.find_element(By.CSS_SELECTOR, "[name='your-email']")
#         input_2.send_keys('Yana@yandex.ru')
#         input_3 = browser.find_element(By.CSS_SELECTOR, "[name='your-subject']")
#         input_3.send_keys('Yana')
#         input_4 = browser.find_element(By.CSS_SELECTOR, "[name='your-message']")
#         input_4.send_keys('Yana')
#         button_1 = browser.find_element(By.CSS_SELECTOR, "[name='gdpr']")
#         button_1.click()
#         button_2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")    
#         button_2.click()
#         message = browser.find_element(By.CSS_SELECTOR, "[class='wpcf7-response-output']")
#         time.sleep(5)
#         assert 'Спасибо! Ваше сообщение успешно отправлено!' == message.text
#         print(message.text)
#     finally:
#         time.sleep(2)
#         browser.quit()

# if __name__ == "__main__":
#     test_5()


link = "https://easysmarthub.ru/contact/"

# def test_1():
#     try:
#         browser = webdriver.Chrome()
#         browser.get(link)
        
#         button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")    
#         button.click()
#     finally:
#         time.sleep(3)
#         browser.quit()

# if __name__ == "__main__":
#     test_1()



# def test_2():
#     try:
#         browser = webdriver.Chrome()
#         browser.get(link)
#         input_1 = browser.find_element(By.CSS_SELECTOR, "[name='your-name']")
#         input_1.send_keys()
#         input_2 = browser.find_element(By.CSS_SELECTOR, "[name='your-email']")
#         input_2.send_keys()
#         input_3 = browser.find_element(By.CSS_SELECTOR, "[name='your-subject']")
#         input_3.send_keys()
        
#         input_5 = browser.find_element(By.CSS_SELECTOR, "[name='your-message']")
#         input_5.send_keys()
#         
#         button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")    
#         button.click()
#     finally:
#         time.sleep(3)
#         browser.quit() 

# if __name__ == "__main__":
#     test_2()


# def test_3():
#     try:
#         browser = webdriver.Chrome()
#         browser.get(link)
#         input_1 = browser.find_element(By.CSS_SELECTOR, "[name='your-name']")
#         input_1.send_keys()
        
#         input_3 = browser.find_element(By.CSS_SELECTOR, "[name='your-subject']")
#         input_3.send_keys()

#         file_path = r'C:\Users\AuroraPC\Desktop\Silenium\selenium_course\2.jpg'
#         input_4 = browser.find_element(By.CSS_SELECTOR, "[.wpcf7-form-control wpcf7-file wpcf7-validates-as-required pozdravlyau-pochti-vse]")
#         input_4.send_keys(file_path)

#         input_5 = browser.find_element(By.CSS_SELECTOR, "[name='your-message']")
#         input_5.send_keys()
#         
#         button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")    
#         button.click()
#     finally:
#         time.sleep(3)
#         browser.quit() 

# if __name__ == "__main__":
#     test_3()


def test_4():
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)

        input_1 = browser.find_element(By.CSS_SELECTOR, "[name='your-name']")
        input_1.send_keys('Yana')

        input_2 = browser.find_element(By.CSS_SELECTOR, "[name='your-email']")
        input_2.send_keys('Yana@ya.ru')
        
        input_3 = browser.find_element(By.CSS_SELECTOR, "[name='your-subject']")
        input_3.send_keys('Yana')

        cur_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(cur_dir, '2.jpg')

        # file_path = r'C:\Users\AuroraPC\Desktop\Silenium\selenium_course\2.jpg'
        input_4 = browser.find_element(By.CSS_SELECTOR, "[class='wpcf7-form-control wpcf7-file wpcf7-validates-as-required pozdravlyau-pochti-vse']")
        input_4.send_keys(file_path)

        input_5 = browser.find_element(By.CSS_SELECTOR, "[name='your-message']")
        input_5.send_keys('Yana')

        

        button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")    
        button.click()
    finally:
        time.sleep(3)
        browser.quit() 

if __name__ == "__main__":
    test_4()





