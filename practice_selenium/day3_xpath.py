from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path=r'C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe')
driver.get('https://www.flipkart.com/')
driver.maximize_window()
try:
    driver.find_element(By.XPATH,"//a[@href='/account/login?ret=/']").click()
except:
    pass
finally:
    driver.find_element(By.XPATH, "//input[@class='_2zrpKA _1dBPDZ']").send_keys('sample')
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("23456")













# driver = webdriver.Chrome(executable_path=r'C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe')
# driver.get('https://www.myntra.com/register?referer=https://www.myntra.com/')
# driver.maximize_window()
# driver.find_element(By.XPATH,"//input[@maxlength='10']").send_keys("8982028298")








# driver = webdriver.Chrome(executable_path=r'C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe')
# driver.get('https://www.amazon.in/')
# driver.maximize_window()
# driver.find_element(By.XPATH,"(//span[@class='nav-line-1'])[2]").click()
# driver.find_element(By.XPATH,"//input[@type='email']").send_keys("ram12@gmail.com")








# driver = webdriver.Chrome(executable_path=r'C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe')
# driver.get('http://greenstech.in/selenium-course-content.html')
# driver.maximize_window()
# driver.find_element(By.XPATH,"(//h2[@class='mb-0'])[3]").click()
# driver.find_element(By.XPATH,"(//a[@title='Model Resume training in chennai'])[5]").click()









# driver = webdriver.Chrome(executable_path=r'C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe')
# driver.get('https://www.cleartrip.com/trains')
# driver.maximize_window()
# driver.find_element(By.XPATH,"//a[@href='/register']").click()
# x = driver.find_element(By.XPATH,"//input[@type='email']")
# x.send_keys("ram12@gmail.com")










# driver = webdriver.Chrome(executable_path=r'C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe')
# driver.get('http://greenstech.in/selenium-course-content.html')
# driver.maximize_window()
# driver.find_element(By.XPATH,"//h2[@class='title mb-0 center']").click()
# driver.find_element(By.XPATH,"(//a[@href='http://greenstech.in/interview-questions/Tcs%20telephonic.pdf#toolbar=0'])[2]").click()



















# driver = webdriver.Chrome(executable_path=r'C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe')
# driver.get('http://demo.automationtesting.in/Register.html')
# driver.maximize_window()
# driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Ram")
# driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("babu")
# driver.find_element(By.XPATH,"//textarea[@ng-model='Adress']").send_keys("no 2 s r nagar trichy")
# driver.find_element(By.XPATH,"//input[@type='email']").send_keys("Ram23@gmail.com")
# driver.find_element(By.XPATH,"//input[@ng-model='Phone']").send_keys("898328292")
# driver.find_element(By.XPATH,"//input[@value='Male']").click()
# driver.find_element(By.XPATH,"//input[@value='Cricket']").click()
# driver.find_element(By.XPATH,"//input[@id='firstpassword']").send_keys("Ram@123")









# driver = webdriver.Chrome(executable_path=r'C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe')
# driver.get('https://www.facebook.com/')
# driver.maximize_window()
# driver.find_element(By.XPATH,"//input[@id='u_0_m']").send_keys("thiyagu")
# driver.find_element(By.XPATH,"//input[@id='u_0_o']").send_keys("C")
# driver.find_element(By.XPATH,"//input[@id='u_0_r']").send_keys("898765433")
# driver.find_element(By.XPATH,"//input[@id='password_step_input']").send_keys("thiyagu268")
# driver.find_element(By.XPATH,"//select[@id='day']").send_keys("5")
# driver.find_element(By.XPATH,"//select[@title='Year']").send_keys("2000")
# driver.find_element(By.XPATH,"//input[@value='2']").click()






# driver = webdriver.Chrome(executable_path=r'C:\Users\ELCOT\PycharmProjects\Thiyagu\drivers\chromedriver.exe')
# driver.get('http://www.greenstechnologys.com/')
# driver.maximize_window()
# driver.find_element(By.XPATH,"//a[@href='contact.php']").click()
# driver.find_element(By.XPATH,"//input[@id='InputName']").send_keys("thiyagu")
# driver.find_element(By.XPATH,"//input[@id='InputEmail1']").send_keys("thiyagu12@gmail.com")
# driver.find_element(By.XPATH,"(//input[@name='phone'])[1]").send_keys("8986547643")
# driver.find_element(By.XPATH,"(//select[@name='courses'])[1]").send_keys("python")
# driver.find_element(By.XPATH,"(//select[@name='branch'])[1]").send_keys("OMR")
# driver.find_element(By.XPATH,"(//select[@name='time'])[1]").send_keys("Immediately")
# driver.find_element(By.XPATH,"(//textarea[@name='comments'])[1]").send_keys("interested to join python course")
