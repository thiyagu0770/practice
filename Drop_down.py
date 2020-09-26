from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.guru99.com/test/newtours/register.php")
first_name = driver.find_element(By.NAME,"firstName")
first_name.send_keys("Ravi")
print(first_name.get_attribute('value'))
last_name = driver.find_element(By.NAME,"lastName")
last_name.send_keys("Kumar")
print(last_name.get_attribute('value'))
phone = driver.find_element(By.NAME,"phone")
phone.send_keys("9836762627")
print(phone.get_attribute('value'))
email = driver.find_element(By.ID,"userName")
email.send_keys("Ravi@gmail.com")
print(email.get_attribute('value'))
address = driver.find_element(By.NAME,"address1")
address.send_keys("no-2 k k nagar")
print(address.get_attribute('value'))
city = driver.find_element(By.NAME,"city")
city.send_keys("AY")
print(city.get_attribute('value'))
state = driver.find_element(By.NAME,"state")
state.send_keys("Albania")
print(state.get_attribute('value'))
postal_code = driver.find_element(By.NAME,"postalCode")
postal_code.send_keys("354567")
print(postal_code.get_attribute('value'))
print("\n")
country = driver.find_element(By.XPATH,"//select[@name='country']")
s_country = Select(country)
all_countries = s_country.options
for x in all_countries:
    print(x.get_attribute('value'))








# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.maximize_window()
# driver.get("http://adactinhotelapp.com/")
# user = driver.find_element(By.ID,"username").send_keys("testingworld")
# password = driver.find_element(By.ID,"password").send_keys("LOWO26")
# login = driver.find_element(By.ID,"login").click()
# time.sleep(5)
# location = driver.find_element(By.ID,"location")
# s_location = Select(location).select_by_index(2)
# hotels = driver.find_element(By.ID,"hotels")
# s_hotels = Select(location).select_by_index(3)
# room = driver.find_element(By.ID,"room_type")
# s_room = Select(location).select_by_index(4)
# submit = driver.find_element(By.ID,"Submit").click()
# select = driver.find_element(By.ID,"radiobutton_1").click()
# click_continue = driver.find_element(By.ID,"continue").click()
# first_name = driver.find_element(By.ID,"first_name").send_keys("Ragu")
# last_name = driver.find_element(By.ID,"last_name").send_keys("426823")
# address = driver.find_element(By.ID,"address").send_keys("No-2\nashok nagar\nchennai")
# card_no = driver.find_element(By.ID,"cc_num").send_keys("6865459876234765")
# Card_detail = driver.find_element(By.ID,"cc_type")
# s_card = Select(Card_detail).select_by_index(2)
# Expiry_month = driver.find_element(By.ID,"cc_exp_month")
# s_month = Select(Expiry_month).select_by_index(5)
# Expiry_year = driver.find_element(By.ID,"cc_exp_year")
# s_year = Select(Expiry_year).select_by_index(7)
# cvv_number = driver.find_element(By.ID,"cc_cvv").send_keys("533")
# book_now = driver.find_element(By.ID,"book_now").click()
# time.sleep(5)
# order_no =driver.find_element(By.ID,"order_no")
# print(order_no.get_attribute("value"))







# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.maximize_window()
# driver.get("http://demo.guru99.com/test/newtours/register.php")
# location = driver.find_element(By.XPATH,"//select[@name='country']")
# store = Select(location)
# x = store.options
# for location in x:
#     print(location.get_attribute("value"))














# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.maximize_window()
# driver.get("http://demo.guru99.com/test/newtours/register.php")
# location = driver.find_element(By.XPATH,"//select[@name='country']")
# store = Select(location)
# x = store.options
# for location in x:
#     print(location.text)






















