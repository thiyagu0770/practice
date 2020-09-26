from selenium import webdriver
from selenium.webdriver.common.by import By



    # instant method
    # def example(self):
    # self.driver = webdriver.Chrome(r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
    # self.driver.maximize_window()
    #class method(inside the class we can't call the instant variable or instant method)
class Base:
    def __init__(self,url):
        self.driver = webdriver.Chrome(r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
        self.x = self.driver.get(url)

    def test(self):
        x = self.driver.title
        return x

