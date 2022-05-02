
# Implementati o clasa Login care sa mosteneasca unittest.TestCase


# https://the-internet.herokuapp.com/

'''
setUp()
Driver
https://the-internet.herokuapp.com/
Click pe Form Authentication

tearDown()
Quit browser

'''

#1 Verificati ca noul url e corect

#importam libariile necesare
from time import sleep

import self as self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service = s)
#
# # maximizam fereastra
# chrome.maximize_window()
#
# # navigam catre un url
#
# chrome.get('https://the-internet.herokuapp.com')
# sleep(2)
# chrome.find_element(By.LINK_TEXT, "A/B Testing").click()
# sleep(2)
# link = chrome.current_url
# print(link)
#
# assert link == 'the-internet.herokuapp.com/abtest'
# sleep(3)
# chrome.quit()



#2 Verificati ca page title e corect

#initializam chrome
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service = s)
#
# # maximizam fereastra
# chrome.maximize_window()
#
# chrome.get('https://the-internet.herokuapp.com')
# title = chrome.title
# sleep(1)
# print(title)
# assert title == 'The Internet'
# sleep(1)
# chrome.quit()

#3 Verificati textul de pe elementul xpath=//h2 e corect

#initializam chrome
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service = s)
#
# # maximizam fereastra
# chrome.maximize_window()
#
# # navigam catre un url
#
# chrome.get('https://the-internet.herokuapp.com')
# h2 = chrome.find_element(By.XPATH, '//*[@id="content"]/h2').text
# sleep(1)
# print(h2)
# assert h2 == 'Available Examples'


#4 Verificati ca butonul de login este displayed

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service = s)
#
# # maximizam fereastra
# chrome.maximize_window()
#
# # navigam catre un url
#
# chrome.get('https://the-internet.herokuapp.com/login')
# sleep(2)
# afisare_login = chrome.find_element(By.XPATH, '//*[@id="login"]/button/i').is_displayed() #functie ce permite sa verifice daca se afiseaza corect un anumit element din site.
# sleep(1)
# if afisare_login is True:
#     print('Butonul de login se afiseaza corect')
# else:
#     print('Butonul nu se afiseaza corect')
# sleep(1)
# chrome.quit()



#5 Verificati ca atributul href al linkului ‘Elemental Selenium’ e corect

# initializam chrome
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service = s)
#
# # maximizam fereastra
# chrome.maximize_window()
#
# # navigam catre un url
#
# chrome.get('https://the-internet.herokuapp.com')
# elemental = chrome.find_element(By.XPATH, '//*[@id="page-footer"]/div/div/a').text
# sleep(1)
# print(elemental)
# assert elemental == 'Elemental Selenium'


#6
'''
Lasati goale user si pass
Click login
Verifica ca eroarea e displayed

'''

# initializam chrome
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service = s)
#
# # maximizam fereastra
# chrome.maximize_window()
#
# # navigam catre un url
#
# chrome.get('https://the-internet.herokuapp.com/login')
# chrome.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
# eroare = chrome.find_element(By.XPATH, '//*[@id="flash"]').text
#
# print(eroare)
# assert eroare == 'Your username is invalid!'
# sleep(2)
# chrome.quit()

#7
'''
Completeaza cu user si pass invalide
Click login
Verifica ca mesajul de pe eroare e corect

'''

# initializam chrome
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service = s)
#
# # maximizam fereastra
# chrome.maximize_window()
#
# # navigam catre un url
#
# chrome.get('https://the-internet.herokuapp.com/secure')
# actual = chrome.find_element(By.XPATH, '//*[@id="flash"]')
# expected = chrome.find_element(By.XPATH, '//*[@id="flash"]')
# self.assertTrue(expected in actual, 'Error message text is incorrect.')
#
# sleep(3)
#
# chrome.quit()



'''
Test10
Completeaza cu user si pass valide
Click login
Verifica ca noul url CONTINE /secure
Foloseste un explicit wait pentru elementul cu clasa ’flash succes’
Verifica ca elementul cu clasa=’flash succes’ este displayed
Verifica ca mesajul de pe acest element CONTINE textul ‘secure area!’

'''

#initializez chrome
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service = s)
#
# # maximizam fereastra
# chrome.maximize_window()
#
# # navigam catre un url
#
# chrome.get('https://the-internet.herokuapp.com/login')
# sleep(1)
# chrome.find_element(By.XPATH, '//*[@id="username"]').send_keys('tomsmith')
# chrome.find_element(By.XPATH, '//*[@id="password"]').send_keys('SuperSecretPassword!')
# chrome.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
# sleep(3)
# secure_link = chrome.current_url
# print(f'You logged into a secure area! {secure_link}')
# sleep(1)
# chrome.quit()


'''
Test11
Completeaza cu user si pass valide
Click login
Click logout
Verifica ca ai ajuns pe https://the-internet.herokuapp.com/login

'''

# initializam chrome
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service = s)
#
# # maximizam fereastra
# chrome.maximize_window()
#
# # navigam catre un url
#
# chrome.get('https://the-internet.herokuapp.com/login')
# sleep(2)
# safe_area = chrome.current_url
# print(f'V-ati delogat cu succes: {safe_area}')
#
# sleep(1)
#
# chrome.quit()
