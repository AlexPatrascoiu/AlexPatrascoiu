#1 Selectors by ID

#importam libariile necesare
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# # initializam chrome
#s = Service(ChromeDriverManager().install())
#chrome = webdriver.Chrome(service = s)

# maximizam fereastra
# chrome.maximize_window()
#
# # navigam catre un url
# chrome.get('https://www.phptravels.net')
#
# # selectam dupa ID
# e_mail = chrome.find_element(By.ID, 'exampleInputEmail1')
# e_mail.send_keys('alex.patrascoiu@yahoo.com')
#
# sleep(5)
# chrome.quit()




#2 Selectors by Link text

# #navigam catre un url
# chrome.get('https://www.phptravels.net')
#
# # selector by Partial Link Text
# # chrome.find_element(By.PARTIAL_LINK_TEXT, 'Ho').click()
# chrome.find_element(By.LINK_TEXT, 'Login').click() # Acelasi lucru, varianta mai lunga
# chrome.find_element(By.CLASS_NAME, 'form-control').send_keys('alecs.patrascoiu@yahoo.ro')
#
# sleep(3)
# chrome.quit()



#3 Selectors by Partial link text

#navigam catre un url
# chrome.get('https://jules.app/sign-in')
# #chrome.find_element(By.PARTIAL_LINK_TEXT,'password').click()
# sleep(2)
# chrome.find_element(By.LINK_TEXT,'Forgot password?').click()
# sleep(3)
# chrome.quit()



#4 Selectors by Tag NAME

# maximizam fereastra
#chrome.maximize_window()
#
# navigam catre un url
# chrome.get('https://www.phptravels.net')
#
# # selector by name
# chrome.find_element(By.LINK_TEXT, 'Signup').click()
#
# sleep(2)
#
# # gasim mai multe si punem in lista
# lista_formular = chrome.find_elements(By.TAG_NAME, 'input')
# lista_formular[1].send_keys('Alex')
# lista_formular[2].send_keys('Dorin')
# lista_formular[3].send_keys('0767365348')
# lista_formular[4].send_keys('alecs.patrascoiu@yahoo.ro')
# lista_formular[5].send_keys('parolaMea!')
# sleep(1)
#
# chrome.find_element(By.ID, 'select2-account_type-container').click()
# #chrome.find_element(By.ID, 'select2-account_type-result-5knr-agent').click()
# sleep(3)
# chrome.quit()
#




#5 Selectors by Class name


# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement

# navigam catre un url
# chrome.get('https://jules.app/sign-in')
# sleep(6)
# # selector by Class - ia primul tot tp. - e ok doar daca avem clasa unica
# lista_elemente = chrome.find_elements(By.CLASS_NAME,'MuiFilledInput-input')
# lista_elemente[0].send_keys('alecs.patrascoiu@yahoo.ro')
# lista_elemente[1].send_keys('parola')
# sleep(3)
# chrome.quit()



#6 Selectors by CSS

#maximizam fereastra
# chrome.maximize_window()
#
# # # navigam catre un url
# chrome.get('https://automationpractice.com/')
#
# # selector by CSS - ID
#
# chrome.find_element(By.CSS_SELECTOR,'input[placeholder="Search"').send_keys('shoes')
# sleep(1)
# chrome.find_element(By.CSS_SELECTOR, 'button[submit').click()
#
# sleep(3)
# chrome.quit()