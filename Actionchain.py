from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import keyboard
import time
driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
driver.maximize_window()
driver.get("http://greenstech.in/selenium-course-content.html")
course = driver.find_element(By.XPATH,"//div[contains(text(),'Courses')]")
x = ActionChains(driver)
x.move_to_element(course).perform()
time.sleep(2)
oracle = driver.find_element(By.XPATH,"//span[contains(text(),'Oracle (48)')]")
x.move_to_element(oracle).perform()
time.sleep(2)
sql = driver.find_element(By.XPATH,"//span[contains(text(),'Oracle SQL')]")
x.move_to_element(sql).perform()
sql.click()
line = driver.find_element(By.XPATH,"//p[contains(text(),'Expert')]")
print(line.text)
















# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://www.homedepot.com/")
# time.sleep(3)
# all_dept = driver.find_element(By.XPATH,"//a[text()='All Departments']")
# acc = ActionChains(driver)
# acc.move_to_element(all_dept).perform()
# time.sleep(3)
# paint = driver.find_element(By.XPATH,"(//a[text()='Paint'])[1]")
# acc.move_to_element(paint).perform()
# time.sleep(3)
# Interior = driver.find_element(By.XPATH,"(//a[contains(text(),'Interior')])[1]")
# acc.move_to_element(Interior).perform()
# time.sleep(3)
# ceiling = driver.find_element(By.XPATH,"//a[text()='Ceiling Paint']")
# ceiling.click()












# driver = webdriver.Chrome(executable_path=r'C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe')
# driver.get("https://www.facebook.com/")
# driver.maximize_window()
# x = driver.find_element(By.ID,"email")
# y = driver.find_element(By.ID,"pass")
# x.send_keys("Thiyagu@gmail.com")
# acc = ActionChains(driver)
# acc.double_click(x).context_click().perform()
# for x in range(4):
#     keyboard.press('down')
#
# keyboard.press('enter')
# time.sleep(3)
# acc.double_click(y).context_click().perform()
# for y in range(3):
#     keyboard.press('down')
# keyboard.press('enter')
# acc.double_click(x).perform()
# keyboard.press_and_release('control+a')
# keyboard.press_and_release('control+x')
# time.sleep(2)
# acc.double_click(y).perform()
# keyboard.press_and_release('control+v')








# driver = webdriver.Chrome(executable_path=r'C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe')
# driver.get("http://demo.guru99.com/test/drag_drop.html")
# driver.maximize_window()
# time.sleep(10)
# x = driver.find_element(By.ID,"credit2")
# y = driver.find_element(By.XPATH, "//ol[@id='bank']")
# a = ActionChains(driver)
# a.drag_and_drop(x, y).perform()
# drag_amount = driver.find_element(By.XPATH,"(//li[@data-id='2'])[1]")
# drop_amount = driver.find_element(By.XPATH,"//ol[@id='amt7']")
# a.drag_and_drop(drag_amount,drop_amount).perform()
# sales = driver.find_element(By.ID,"credit1")
# sales_x = driver.find_element(By.XPATH,"//ol[@id='loan']")
# a.drag_and_drop(sales,sales_x).perform()
# sales_drag = driver.find_element(By.XPATH,"(//li[@data-id='2'])[2]")
# sales_drop = driver.find_element(By.XPATH,"//ol[@id='amt8']")
# a.drag_and_drop(sales_drag,sales_drop).perform()
# button = driver.find_element(By.XPATH,"//a[contains(text(),'Perfect!')]")
# print(button.text)
# if button.text == 'Perfect!':
#     print('the resulted is executed')
# else:
#     print('the result is not executed')







# driver = webdriver.Chrome(executable_path=r'C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe')
# driver.get("https://www.flipkart.com/")
# driver.maximize_window()
# time.sleep(10)
# driver.find_element(By.XPATH, "//button[text()='✕']").click()
# home = driver.find_element(By.XPATH,"//span[text()='Home & Furniture']")
# x = ActionChains(driver)
# x.move_to_element(home).perform()
# time.sleep(5)
# towel = driver.find_element(By.XPATH,"//a[@title='Bath Towels']")
# x.move_to_element(towel).click().perform()
# time.sleep(10)
# y = driver.find_element(By.XPATH,"(//a[contains(text(),'Bathe & Soak Microfiber 250 GSM Bath')])[1]")
# print(y.text)








# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("https://www.firstcry.com/")
# driver.maximize_window()
# time.sleep(15)
# categories = driver.find_element(By.XPATH,"//a[text()=' All Categories']")
# acc = ActionChains(driver)
# acc.move_to_element(categories).perform()
# time.sleep(2)
# footwear = driver.find_element(By.XPATH,"(//a[text()='FOOTWEAR'])[1]")
# acc.move_to_element(footwear).perform()
# time.sleep(2)
# casual = driver.find_element(By.XPATH,"(//a[text()='Casual Shoes'])[3]")
# casual.click()
# time.sleep(10)
# x = driver.find_element(By.XPATH,"//a[contains(text(),'526.5')]")
# print(x.text)















# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("https://www.shopclues.com/wholesale.html")
# sports = driver.find_element(By.XPATH,"//a[text()='Sports & More']")
# x = ActionChains(driver)
# x.move_to_element(sports).perform()
# time.sleep(2)
# weight = driver.find_element(By.XPATH,"//a[text()='Weight Gainers']")
# weight.click()







# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("https://www.shopclues.com/wholesale.html")
# mobile = driver.find_element(By.XPATH,"//a[text()='Mobiles & Electronics']")
# x = ActionChains(driver)
# x.move_to_element(mobile).perform()
# time.sleep(2)
# price = driver.find_element(By.XPATH,"//a[text()='Rs.5001 - Rs.10000']")
# price.click()





# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("https://www.amazon.in/")
# prime = driver.find_element(By.XPATH,"//span[text()='Try']")
# acc = ActionChains(driver)
# acc.move_to_element(prime).perform()
# time.sleep(2)
# y = driver.find_element(By.ID,"multiasins-img-link")
# y.click()





# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("https://www.firstcry.com/")
# categories = driver.find_element(By.XPATH,"//a[text()='ALL CATEGORIES']")
# x = ActionChains(driver)
# x.move_to_element(categories).perform()
# time.sleep(2)
# footwear = driver.find_element(By.XPATH,"(//a[text()='FOOTWEAR'])[1]")
# x.move_to_element(footwear).perform()
# time.sleep(2)
# casual = driver.find_element(By.XPATH,"(//a[text()='Casual Shoes'])[3]")
# casual.click()




# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("http://www.greenstechnologys.com/python-training.html")
# driver.maximize_window()
# course = driver.find_element(By.XPATH,"(//div[contains(text(),'Courses')])[1]")
# x = ActionChains(driver)
# print(type(x))
# x.move_to_element(course).perform()
# time.sleep(2)
# programming = driver.find_element(By.XPATH,"//span[text()='Programming (9)']")
# x.move_to_element(programming).perform()
# time.sleep(2)
# android = driver.find_element(By.XPATH,"//span[text()='Android Certification Training']")
# android.click()