from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

# in aceasta pagina punem toate metodele care sunt utile in orice pagina din proiect
# si nu sunt specifice neaparat une singure pagini
# apoi paginile celelalte vor mosteni aceasta pagina => ca sa nu scriem de n ori wait_for_elem sau alte chestii ajutatoare

class Base_page(Browser, unittest.TestCase):
    def wait_for_elem(self,time,by,selector):
        WebDriverWait(self.chrome,time).until(EC.presence_of_element_located((by,selector)))