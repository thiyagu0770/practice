from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
driver.get("https://www.shopclues.com/wholesale.html")
driver.maximize_window()
x = driver.find_element(By.XPATH,"//span[contains(text(),'Jackly')]")
print(x.text)
y = driver.find_element(By.XPATH,"//span[contains(text(),'Women Em')]")
print(y.text)





# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("https://www.snapdeal.com/")
# driver.maximize_window()
# x = driver.find_element(By.XPATH,"(//div[contains(text(),'bhawna collection  L')])[1]")
# print(x.text)
# y = driver.find_element(By.XPATH,"(//div[contains(text(),'Veirdo 100 Percent Cotton Green Color Block T-Shirt')])[1]")
# print(y.text)












# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("https://www.gmail.com")
# driver.maximize_window()
# x = driver.find_element(By.ID,"identifierId")
# x.send_keys("Ragu24343@gmail.com")
# print(x.get_attribute("value"))
# y = driver.find_element(By.XPATH, "(//button[@type='button'])[3]")
# y.click()











# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("https://www.shopclues.com/wholesale.html")
# driver.maximize_window()
# x = driver.find_element(By.ID,"autocomplete")
# x.send_keys("Mobiles")
# print(x.get_attribute("value"))
# print("\n")
# y = driver.find_element(By.ID,"autocomplete")
# y.send_keys("Headphones")
# print(y.get_attribute("value"))








# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("https://www.flipkart.com/")
# driver.maximize_window()
# try:
#     driver.find_element(By.XPATH,"//a[@href='/account/login?ret=/']").click()
# except:
#     pass
# finally:
#     x = driver.find_element(By.XPATH,"//input[@class='_2zrpKA _1dBPDZ']")
#     x.send_keys("Ragu")
#     print(x.get_attribute("value"))
#     y = driver.find_element(By.XPATH,"//input[@class='_2zrpKA _3v41xv _1dBPDZ']")
#     y.send_keys("Ragu@3537")
#     print(y.get_attribute("value"))











# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp")
# driver.maximize_window()
# x = driver.find_element(By.ID,"firstName")
# x.send_keys("Ragu")
# print(x.get_attribute("value"))
# y = driver.find_element(By.ID,"lastName")
# y.send_keys("c")
# print(y.get_attribute("value"))
# z = driver.find_element(By.NAME,"Username")
# z.send_keys("Ragu125")
# print(z.get_attribute("value"))
# p = driver.find_element(By.NAME,"Passwd")
# p.send_keys("Ragu@1235")
# print(p.get_attribute("value"))
# q = driver.find_element(By.NAME,"ConfirmPasswd")
# q.send_keys("Ragu@1235")
# print(q.get_attribute("value"))





# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("http://adactinhotelapp.com/")
# driver.maximize_window()
# x = driver.find_element(By.ID,"username")
# x.send_keys("ram")
# print(x.get_attribute("value"))
# y = driver.find_element(By.ID,"password")
# y.send_keys(232322)
# print(y.get_attribute("value"))







# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("http://www.facebook.com")
# driver.maximize_window()
# x = driver.find_element(By.ID,"email")
# x.send_keys("thiyagu")
# print(x.get_attribute('value'))
# y = driver.find_element(By.ID,"pass")
# y.send_keys(728342)
# print(y.get_attribute("value"))






# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("http://greenstech.in/selenium-course-content.html")
# driver.maximize_window()
# x = driver.find_element(By.XPATH,"(//h6[contains(text(),'Greens')])[2]")
# y = driver.find_element(By.XPATH,"//span[contains(text(),'Plot')]")
# z = driver.find_element(By.XPATH,"//span[contains(text(),'Bala')]")
# p = driver.find_element(By.XPATH,"//span[contains(text(),'Kan')]")
# q = driver.find_element(By.XPATH,"//span[contains(text(),'Okk')]")
# r = driver.find_element(By.XPATH,"//span[contains(text(),'Jai')]")
# s = driver.find_element(By.XPATH,"(//a[contains(text(),'+91')])[6]")
# t = driver.find_element(By.XPATH,"(//a[contains(text(),'contact')])[2]")
# print(x.text)
# print(y.text)
# print(z.text)
# print(p.text)
# print(q.text)
# print(r.text)
# print(s.text)
# print(t.text)





# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("http://greenstech.in/selenium-course-content.html")
# driver.maximize_window()
# x = driver.find_element(By.XPATH,"(//p[contains(text(),'Placement')])[1]")
# print(x.text)
# y = driver.find_element(By.XPATH,"//p[contains(text(),'Learn')]")
# print(y.text)









# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("http://greenstech.in/selenium-course-content.html")
# driver.maximize_window()
# x = driver.find_element(By.XPATH,"//span[@title='Review']").click()
# y = driver.find_element(By.XPATH,"(//p[contains(text(),'Manual')])[1]")
# print(y.text)







# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("http://www.greenstechnologys.com/")
# driver.maximize_window()
#
# y = driver.find_element(By.XPATH, "//font[contains(text(),'We')]")
# x = driver.find_element(By.XPATH,"//font[contains(text(),'emerging')]")
# print(y.text)
# print(x.text)









# driver = webdriver.Chrome(executable_path=r"C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe")
# driver.get("http://greenstech.in/selenium-course-content.html")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//span[@title='Review']").click()
# y = driver.find_element(By.XPATH,"(//p[contains(text(),'learned')])[1]")
# print(y.text)







