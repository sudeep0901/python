from selenium import webdriver
from selenium.webdriver.common.keys  import Keys 
import time
print("Hello World")
a = 10
b = 20



#put drivers in lib fodler in python install ation

driver = webdriver.Chrome()

# driver = webdriver.Chrome(executable_path=r'D:\github\python\src\autmation\python_selenium\drivers\chromedriver.exe')
# driver = webdriver.Firefox(executable_path=r'D:\github\python\src\autmation\python_selenium\drivers\geckodriver.exe')
# driver = webdriver.ie()

driver.set_page_load_timeout(10)
driver.get("https://google.com")
driver.find_element_by_name('q').send_keys("machine learning")
driver.implicitly_wait(10)

driver.find_element_by_name('btnK').send_keys(Keys.ENTER)

driver.maximize_window()
driver.refresh()
time.sleep()

driver.close()
driver.quit()

