from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import keyboard
import time
driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Alerts.html")
driver.find_element(By.XPATH,"//button[@onclick='alertbox()']").click()
time.sleep(3)
driver.switch_to.alert.accept()
x = driver.find_element(By.XPATH, "//a[contains(text(),'Widgets')]")
z= ActionChains(driver)
z.move_to_element(x).perform()
with_ok = driver.find_element(By.XPATH,"//a[text()='Alert with OK & Cancel ']").click()
confirm = driver.find_element(By.XPATH,"//button[@onclick='confirmbox()']").click()
driver.switch_to.alert.accept()
with_text = driver.find_element(By.XPATH,"//a[text()='Alert with Textbox ']").click()
prompt = driver.find_element(By.XPATH,"//button[@onclick='promptbox()']").click()
time.sleep(3)
driver.switch_to.alert.accept()












# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("http://greenstech.in/selenium-course-content.html")
# driver.maximize_window()
# x = driver.find_element(By.XPATH,"//h2[contains(text(),'Interview ')]").click()
# cts = driver.find_element(By.XPATH,"//a[text()='CTS Interview Question ']")
# a = ActionChains(driver)
# a.context_click(cts).perform()
# time.sleep(3)
# keyboard.press('down')
# time.sleep(2)
# keyboard.press('enter')







# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# sign_in = driver.find_element(By.XPATH,"//span[text()='Hello, Sign in']")
# acc = ActionChains(driver)
# acc.move_to_element(sign_in).perform()
# time.sleep(2)
# y = driver.find_element(By.XPATH,"(//span[text()='Sign in'])[1]").click()
# time.sleep(3)
# email = driver.find_element(By.XPATH,"//input[@id='ap_email']")
# email.send_keys("Abu@gmail.com")
# time.sleep(3)
# b = ActionChains(driver)
# b.double_click(email).perform()
# keyboard.press_and_release("control+a")
# time.sleep(2)
# keyboard.press_and_release("control+x")








# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("http://www.greenstechnologys.com/")
# driver.maximize_window()
# x = driver.find_element(By.XPATH,"//font[text()='GREENS TECHNOLOGY']")
# acc = ActionChains(driver)
# acc.double_click(x).perform()
# keyboard.press('down')
# keyboard.press('enter')
# print(x.text)








# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("https://www.flipkart.com/")
# driver.maximize_window()
# time.sleep(2)
# # driver.find_element(By.XPATH,"//a[text()='Login']").click()
# x = driver.find_element(By.XPATH,"//input[@class='_2zrpKA _1dBPDZ']")
# y = driver.find_element(By.XPATH,"//input[@class='_2zrpKA _3v41xv _1dBPDZ']")
# x.send_keys("Ragu@gmail.com")
# acc = ActionChains(driver)
# acc.double_click(x).perform()
# keyboard.press_and_release("control+a")
# keyboard.press_and_release("control+x")
# time.sleep(2)
# acc.double_click(y).perform()
# keyboard.press_and_release("control+v")