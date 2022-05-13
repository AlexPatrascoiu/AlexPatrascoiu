from pages.sign_in_page import Sign_in_page
from browser import Browser
from pages.forgot_password_page import Forgot_password_page

def before_all(context):
    context.browser = Browser()
    context.sign_in_page = Sign_in_page()
    context.forgot_pass = Forgot_password_page()

def after_all(context):
    context.browser.close()

    # contextul e ca o cutiuta care contine cate un obiect de tipul fiecarei clase de pagini
    # de fiecare data cand adaugam o pagina noua in proiect, o vom adauga in context