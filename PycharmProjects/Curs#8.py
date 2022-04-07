#IDENTIFICARE BY ID
# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# selector by ID
first_name = chrome.find_element(By.ID, 'first-name')
first_name.send_keys('Ala Bala Portocala')

sleep(3)
chrome.quit()

#avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()




#IDENTIFICARE BY TAG NAME

# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# selector by Tag - ia primul tot tp. - e ok doar daca avem tag unic
chrome.find_element(By.TAG_NAME, 'input').send_keys('Test')

sleep(3)

# gasim mai multe si le punem in lista
lista_taguri = chrome.find_elements(By.TAG_NAME, 'input') # am definit o lista care sa stocheze toate elementele de pe site identificabile prin tag-ul de input
lista_taguri[1].send_keys('Test1')
print(len(lista_taguri))

sleep(3)

chrome.quit()


#IDENTIFICARE BY PARTIAL LINK TEXT


# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/')

# selector by Partial Link Text
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Enab').click()
# chrome.find_element(By.LINK_TEXT, 'Enabled and disabled elements').click() -> Acelasi lucru, varianta mai lunga

sleep(3)
chrome.quit()

#IDENTIFICARE BY CLASS NAME
# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# selector by Class - ia primul tot tp. - e ok doar daca avem clasa unica
chrome.find_element(By.CLASS_NAME, 'form-control').send_keys('Test')

# gasim mai multe si punem in lista
chrome.find_elements(By.CLASS_NAME, 'form-control')[1].send_keys("test1")

# lista_elemente_clasa = chrome.find_elements(By.CLASS_NAME, 'form-control') -> Acelasi lucru, varianta mai lunga
# lista_elemente_clasa[1].send_keys('Test1')

sleep(3)
chrome.quit()


#IDENTIFICARE BY CSS SELECTOR

# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# selector by CSS - ID
chrome.find_element(By.CSS_SELECTOR, 'input#first-name').send_keys('An')  # # = identificator pentru id

sleep(2)

chrome.find_element(By.CSS_SELECTOR, 'input#first-name').clear()  #

# selector by CSS - Class - only first one if multiple matches
chrome.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('dy')  # . = identificator pentru clasa

sleep(2)

# selector by CSS - atribut=valoare
chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter last name"]').send_keys(
    'S')  # [] = identificator pentru atribut = valoare

sleep(2)

# selector by CSS - atribut=valoare partiala + parinte -> copil
chrome.find_element(By.CSS_SELECTOR, 'div input[placeholder*="last name"]').send_keys(
    'inpetrean')  # * = marcator pentru valoare partiala a placeholderului

sleep(3)
chrome.quit()


#IDENTIFICARE BY XPATH

# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# Xpath -> recomandat - cel mai flexibil

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# selector by Xpath - atribut=valoare
chrome.find_element(By.XPATH, '//input[@id="first-name"]').send_keys('A')

sleep(2)

# selector by Xpath - * toate elementele care resecta regula
chrome.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('n')  #  * inseamna un inlocuitor pentru toate elementele care respecta regula

sleep(2)

# selector by Xpath - navigare in jos - trecem prin fiecare element
chrome.find_element(By.XPATH, '//div/div/input[@id="first-name"]').send_keys('r')

sleep(2)

# selector by Xpath - navigare in jos - skip tags - cautam oriunde sub form un input care sa respecte regula
chrome.find_element(By.XPATH, '//form//input[@id="first-name"]').send_keys('e') # // = orice mostenitor, / = primul mostenitor
sleep(2)

# selector by Xpath - selectare elem din lista - index incepe de la 1
chrome.find_element(By.XPATH, '(//input[@class="form-control"])[2]').send_keys('i')

sleep(3)

# Selector by Xpath - OR primul gasit dintre variante
s = chrome.find_element(By.XPATH, '//input[@id="last-name1"] | //input[@id="last-name2"] | //input[@id="last-name"]')
# stergem valorile din input
s.clear()
s.send_keys('Sinpetrean')

# seector by Xpath - in f de textul partial + luam textul de pe el cu proprietatea text
full_text = chrome.find_element(By.XPATH, '//a[contains(text(), "Sub")]').text
print(full_text)
assert full_text == 'Submit'

sleep(3)

# selector by Xpath - in f de textul vizibil
# chrome.find_element(By.XPATH, '//a[text()="Submit"]').click()

'''
x y axis navigation
cu parent in sus
cu /elem_type - ajungem la elementul copil
cu //elem_type - cauta prin toti descendentii
cu parent::elem_type in sus
cu following-sibling::elem_type - urmatorul frate de la acelasi nivel
cu preceding-sibling::elem_type - fratele anterior de la acelasi nivel
//label[text()="First name"]/parent::strong/following-sibling::input/preceding-sibling::strong
'''


# cu ajutorul unei functii cand avem foarte multe elemente de acelasi tip
# si vrem sa parametrizam selectorul
def formy_input_by_placeholder(placeholder_text, input_value):
    input = chrome.find_element(By.XPATH, f'//input[@placeholder="{placeholder_text}"]')
    input.clear()
    input.send_keys(input_value)


def formy_input_by_label(label, input_value):
    my_input = chrome.find_element(By.XPATH, f'//label[text()="{label}"]/parent::strong/parent::div//input')
    my_input.clear()
    my_input.send_keys(input_value)


formy_input_by_placeholder('Enter first name', 'ANDY')
formy_input_by_placeholder('Enter last name', 'SINPETREAN')

formy_input_by_label('Job title', 'Automation Engineer')

sleep(3)
chrome.quit()
