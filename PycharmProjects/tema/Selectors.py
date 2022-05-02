Urmatoarele exercitii au fost facute pe https://formy-project.herokuapp.com/autocomplete

# selector by Xpath - atribut=valoare
chrome.find_element(By.XPATH, '//input[@id="first-name"]').send_keys('test')

# selector by Xpath - in f de textul partial + luam textul de pe el cu proprietatea text
full_text = chrome.find_element(By.XPATH, '//a[contains(text(), "Auto")]').text

# selector by Xpath - in f de textul vizibil
chrome.find_element(By.XPATH, '//a[text()="Submit"]').click()


# selector by Xpath - OR primul gasit dintre variante  ->  | = sau
s = chrome.find_element(By.XPATH, '//input[@id="first-name"] | //input[@id="last-name"]')


# selector by Xpath cu *
chrome.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('test')

# selector by Xpath - selectare elem din lista - index incepe de la 1 (atunci cand se returneaza mai multe elemente pe site)
chrome.find_element(By.XPATH, '(//input[@class="form-control"])[2]').send_keys('i')



unul in care sa folosesti parent::

//div[@class="form-group"]/parent::form

unul in care sa folosesti fratele anterior sau de dupa (la alegere)

//div[@class="form-group"]/parent::form/following-sibling::script

# o functie ca si cea de la clasa prin care sa pot alege eu prin param cu ce element vreau sa interactionez.

def formy_input_by_placeholder(placeholder_text, input_value):
     input = chrome.find_element(By.XPATH, f'//input[@placeholder="{placeholder_text}"]')
     input.clear()
     input.send_keys(input_value)