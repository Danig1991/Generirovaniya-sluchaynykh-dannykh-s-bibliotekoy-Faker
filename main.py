import time

from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# базовый url
base_url = 'https://www.saucedemo.com/'

# добавить опции/оставить браузер открытым
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())

# открытие браузера с параметрами
driver_chrome = webdriver.Chrome(
    options=options,
    service=service
)

# переход по url в браузере/развернуть на весь экран
driver_chrome.get(base_url)
driver_chrome.maximize_window()

# создать случайное имя и вставить его в поле Username
fake_name = Faker("en_Us").first_name()
driver_chrome.find_element(By.ID, "user-name").send_keys(fake_name)
print(f"Имя, вставленное в поле Username - \"{fake_name}\".")

# пауза
time.sleep(2)

# закрыть страницу
driver_chrome.quit()
print("Страница закрыта.")
