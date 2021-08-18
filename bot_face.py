import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class bot_face():
    def __init__(self):

        # email e senha ficticios para usarmos no facebook
        self.cel_email = input('Digite seu email: ')
        self.password = input('Digite sua senha: ')
        self.drive = webdriver.Chrome(
            executable_path=r'D:\gil26\Documents\Atom Projects\chromedriver.exe')

    def formulario(self):
        drive = self.drive
        drive.get('https://www.facebook.com/')

        # Tempo para preenchimento das credenciais no site
        time.sleep(3)

        cel_email = drive.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input')

        password = drive.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input')

        botton = drive.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')

        cel_email.send_keys(self.cel_email)
        password.send_keys(self.password)
        botton.click()


bot = bot_face()
bot.formulario()
