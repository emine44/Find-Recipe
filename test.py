from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.utils import ChromeType


browser = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())


driver.get("http://0.0.0.0:5000/")
w_title=driver.title
print(assertEqual(w_title, "homepage"))