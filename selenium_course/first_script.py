import time

# Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver

#импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

#инициализация драйвера браузера
# driver = webdriver.Chrome()

# #установили паузу на 15 секунд. Если все сделали верно при запуке откроется хром
# time.sleep(1)

# # С помощью метода GET мы скажем браузеру, что надо открыть
# driver.get('https://suninjuly.github.io/text_input_task.html')
# time.sleep(1)

# # Метод find_element позволяет найти нужный элемент на сайте
# textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

# # Питон за нас напишет текст get() в поле textarea
# textarea.send_keys("get()")
# time.sleep(5)

# # Найдем кнопку как в предыдущем случае
# submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# # выполним действие нажатия на кнопку
# submit_button.click()
# time.sleep(5)

# # после выполнения всех действий мы закрываем окно брауузера
# driver.quit()




# driver.get('https://google.com')
# textarea = driver.find_element(By.CSS_SELECTOR, ".gLFyf")
# textarea.send_keys("get()")
# time.sleep(5)
# submit_button = driver.find_element(By.CSS_SELECTOR, ".gNO89b")
# submit_button.click()
# time.sleep(15)
# driver.quit()



# /////

# link = "http://suninjuly.github.io/simple_form_find_task.html"


# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     input_1 = browser.find_element(By.NAME, "first_name")
#     input_1.send_keys("Yana")
#     input_2 = browser.find_element(By.NAME, "last_name")
#     input_2.send_keys('Yana')
#     input_3 = browser.find_element(By.NAME, "firstname")
#     input_3.send_keys('Yana')
#     input_4 = browser.find_element(By.ID, "country")
#     input_4.send_keys('Yana')
#     button = browser.find_element(By.ID, "submit_button")
#     button.click()
#     time.sleep(5)
# finally:
#     browser.quit()



# /////

# link = "https://www.degreesymbol.net/"
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     link = browser.find_element(By.LINK_TEXT, "Degree Symbol in Math")
#     link.click()
# finally:
#     time.sleep(10)
#     browser.quit()
   


# /////

# import math

# a = str(math.ceil(math.pow(math.pi, math.e)*10000))
# print(a)

# link = "http://suninjuly.github.io/find_link_text"
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     link = browser.find_element(By.LINK_TEXT, "224592")
#     link.click()
#     input_1 = browser.find_element(By.NAME, "first_name")
#     input_1.send_keys("Yana")
#     input_2 = browser.find_element(By.NAME, "last_name")
#     input_2.send_keys('Yana')
#     input_3 = browser.find_element(By.NAME, "firstname")
#     input_3.send_keys('Yana')
#     input_4 = browser.find_element(By.ID, "country")
#     input_4.send_keys('Yana')
#     button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
#     button.click()
# finally:
#     time.sleep(10)
#     browser.quit()


# /////

# link = "https://easysmarthub.ru/contact/"
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     input_1 = browser.find_element(By.CSS_SELECTOR, "[name='your-name']")
#     input_1.send_keys("Yana")
#     input_2 = browser.find_element(By.CSS_SELECTOR, "[name='your-email']")
#     input_2.send_keys('Yana@yandex.ru')
#     input_3 = browser.find_element(By.CSS_SELECTOR, "[name='your-subject']")
#     input_3.send_keys('Yana')
#     input_4 = browser.find_element(By.CSS_SELECTOR, "[name='your-message']")
#     input_4.send_keys('link = "https://easysmarthub.ru/contact/"'
# 'try:'
#     'browser = webdriver.Chrome()'
#     'browser.get(link)'
#     'input_1 = browser.find_element(By.CSS_SELECTOR, "[name="your-name"]")'
#     'input_1.send_keys("Yana")'
#     'input_2 = browser.find_element(By.CSS_SELECTOR, "[name="your-email"]")'
#     'input_2.send_keys("Yana@yandex.ru")'
#     'input_3 = browser.find_element(By.CSS_SELECTOR, "[name="your-subject"]")'
#     'input_3.send_keys("Yana")'
#     'input_4 = browser.find_element(By.CSS_SELECTOR, "[name="your-message"]")'
#     'input_4.send_keys('   ')'
#     'button_1 = browser.find_element(By.CSS_SELECTOR, "[name="gdpr"]")'
#     'button_1.click()'
#     'button_2 = browser.find_element(By.CSS_SELECTOR, "[button type="submit"]")'  
#     'button_2.click()'
# 'finally:'
#     'time.sleep(10)'
#    ' browser.quit()'
#   )
#     button_1 = browser.find_element(By.CSS_SELECTOR, "[name='gdpr']")
#     button_1.click()
#     button_2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")    
#     button_2.click()
# finally:
#     time.sleep(10)
#     browser.quit()



# /////

from selenium.webdriver.support.ui import Select

# link = "https://suninjuly.github.io/selects2.html"
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     input_1 = browser.find_element(By.ID, 'num1')
#     input_2 = browser.find_element(By.ID, 'num2')
#     a = input_1.text
#     b = input_2.text
#     a1 = int(a)
#     b1 = int(b)
#     my_sum = a1+b1
#     select = Select(browser.find_element(By.TAG_NAME,'select'))
#     select.select_by_value(str(my_sum))
# finally:
#     time.sleep(5)
#     browser.quit()



# /////

import os

# link = "https://suninjuly.github.io/file_input.html"

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     input_1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
#     input_1.send_keys('asd')
#     input_2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"')
#     input_2.send_keys('asd')
#     input_3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
#     input_3.send_keys('asd')

#     #Получяем путь к директории текущего исполняемого файла
#     cur_dir = os.path.abspath(os.path.dirname(__file__))
#     file_path = os.path.join(cur_dir, '1.txt')
#     # file_path = r'C:\Users\AuroraPC\Desktop\Silenium\selenium_course\1.txt'
#     element = browser.find_element(By.CSS_SELECTOR,'[type="file"]')
#     element.send_keys(file_path)
#     button = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
#     button.click()
# finally:
#     time.sleep(5)
#     browser.quit()



# /////
# 15_04_2024

import math
# link = 'https://suninjuly.github.io/alert_accept.html'

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
#     button.click()
#     promt = browser.switch_to.alert
#     promt.accept()

#     def calc(x):
#         return math.log(abs(12*math.sin(int(x))))
    
#     x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
#     el_x = x.text
#     x1 = int(el_x)
#     rez = browser.find_element(By.CSS_SELECTOR, '[class="form-control"]')
#     rez.send_keys(calc(x1))
#     button = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
#     button.click()

# finally:
#     time.sleep(5)
#     browser.quit()    
    

# /////
# 16_04_2024

# link = 'http://suninjuly.github.io/redirect_accept.html'

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
#     button.click()
#     # new_window = browser.window_handles[1]
#     # browser.switch_to.window(new_window)
#     browser.switch_to.window(browser.window_handles[1])     # второй вариант

#     def calc(x):
#         return math.log(abs(12*math.sin(int(x))))
    
#     form = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
#     x = int(form.text)
#     rez = browser.find_element(By.CSS_SELECTOR, '[class="form-control"]')
#     rez.send_keys(calc(x))
#     button = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
#     button.click()

# finally:
#     time.sleep(5)
#     browser.quit()    


# /////

# try:
#     browser = webdriver.Chrome()
#     browser.get('http://suninjuly.github.io/wait1.html')

#     #говорим webdriver искать каждый элемент в течени 5 секунд
#     browser.implicitly_wait(5)

#     # time.sleep(5)       # второй вариант, непредпочтительный

#     button = browser.find_element(By.ID, 'verify')
#     button.click()
#     message = browser.find_element(By.ID, 'verify_message')
#     assert 'successful' in message.text

# finally:
#     time.sleep(3)
#     browser.quit() 



# /////

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# try:
#     browser = webdriver.Chrome()
#     browser.get('http://suninjuly.github.io/explicit_wait2.html')

#     element = WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID,'price'),'100'))
#     btn = browser.find_element(By.ID, 'book')
#     btn.click()

#     def calc(x):
#         return math.log(abs(12*math.sin(int(x))))
    
#     form = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
#     x = int(form.text)
#     rez = browser.find_element(By.CSS_SELECTOR, '[class="form-control"]')
#     rez.send_keys(calc(x))
#     button = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
#     button.click()

# finally:
#     time.sleep(3)
#     browser.quit() 



# /////
# 17_04_2024


# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.TAG_NAME, 'input')
#     for i in elements:
#         i.send_keys("Привет")
#     buton = browser.find_element(By.TAG_NAME,'button')
#     buton.click()
# finally:
#     time.sleep(30)
#     browser.quit()



# /////

import unittest


# class TestAbs(unittest.TestCase):
#     def test_abs1(self):
#         self.assertEqual(abs(-42),42, "should be number")
#     def test_abs2(self):
#        self.assertEqual(abs(-42),42, "should be number")
       


# if __name__ == "__main__":
#     unittest.main()


# /////

# class RegTestForm(unittest.TestCase):
#     def test_reg(self):
#         try:
#             browser = webdriver.Chrome()
#             browser.get("http://suninjuly.github.io/registration1.html")
#             input_1 = browser.find_element(By.CSS_SELECTOR, "[class='form-control first']")
#             input_1.send_keys("Yana")
#             input_2 = browser.find_element(By.CSS_SELECTOR, "[class='form-control second']")
#             input_2.send_keys('Yana')
#             input_3 = browser.find_element(By.CSS_SELECTOR, "[class='form-control third']")
#             input_3.send_keys('Yana')
#             input_4 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone:']")
#             input_4.send_keys('Yana')
#             input_5 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your address:']")
#             input_5.send_keys('Yana')
#             button = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-default']")
#             button.click()
#             a = browser.find_element(By.TAG_NAME, "h1").text
#             self.assertEqual(a,"Congratulations! You have successfully registered!")
#             print("Yes")
#         finally:
#             time.sleep(2)
#             browser.quit()
#     # def test_assert(self):     # некорректный вариант
#     #     self.assertEqual("Congratulations! You have successfully registered!","Congratulations! You have successfully registered!")
#     #     print("Yes")


# if __name__ == "__main__":
#     unittest.main()
        

# /////
# 18_04_2024

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import pytest

# def test_ecept():
#     try:
#         browser = webdriver.Chrome()
#         browser.get('https://easysmarthub.ru/kak-ustanovit-selenium-webdriver-na-windows-i-zapustit-lokalnoe-okruzhenie-python-v-vs-code/')
#         with pytest.raises(NoSuchElementException):
#             browser.find_element(By.CSS_SELECTOR,"[id='molodec']")
#             pytest.fail('Не должна отображаться кнопка')
#     finally:
#         browser.quit()







