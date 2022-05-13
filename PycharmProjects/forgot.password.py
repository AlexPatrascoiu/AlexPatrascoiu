from time import sleep

from pages.base_page import Base_page
from selenium.webdriver.common.by import By

class Forgot_password_page(Base_page):
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder ='Enter your email']")
    INVALID_EMAIL_MESSAGE = (By.XPATH,'//p[contains(text(),"Please enter a valid email address!")]')
    SEND_EMAIL_BTN = (By.XPATH,"//*[@id='root']/div/div[2]/div/div[2]/button")

    def set_email(self,time, email):
        self.wait_for_elem(time,*self.EMAIL_INPUT)
        self.chrome.find_element(*self.EMAIL_INPUT).send_keys(email)
        sleep(1)

    def click_send_email_button(self):
        self.chrome.find_element(*self.SEND_EMAIL_BTN).click()

    def verify_email_error_msg(self):
        expected = 'Please enter a valid email address!'
        actual = self.chrome.find_element(*self.INVALID_EMAIL_MESSAGE).text
        self.assertEqual(expected,actual,"The message returned by the page is incorrect")