from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import keyboard
driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.amazon.in/")
time.sleep(5)
sign_in = driver.find_element(By.XPATH,"//div[text()='Connect with Us']")
driver.execute_script("arguments[0].scrollIntoView(true)",sign_in)











# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://www.flipkart.com/")
# driver.find_element(By.XPATH,"//button[text()='✕']").click()
# time.sleep(2)
# grocery = driver.find_element(By.XPATH,"//h2[text()='Grocery/Supermart']")
# driver.execute_script("arguments[0].scrollIntoView(true)",grocery)
# x = driver.find_element(By.XPATH,"//span[text()='Men']")
# time.sleep(2)
# # driver.execute_script("arguments[0].scrollIntoView(true)",x)
# keyboard.press('end')
# keyboard.press('home')










# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.maximize_window()
# driver.get("http://www.greenstechnologys.com/python-training.html")
# Greens = driver.find_element(By.XPATH,"//h2[text()='Greens Technologies Official Branches']")
# features = driver.find_element(By.XPATH,"//h2[text()='Python  Training Features']")
# driver.execute_script("arguments[0].scrollIntoView(true)",Greens)
# time.sleep(3)
# driver.execute_script("arguments[0].scrollIntoView(true)",features)











# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.maximize_window()
# driver.get("http://www.greenstechnologys.com/index.html")
# peru = driver.find_element(By.XPATH,"//span[text()='Greens technology Perumbakkam']")
# time.sleep(3)
# driver.execute_script("arguments[0].scrollIntoView(true)",peru)














