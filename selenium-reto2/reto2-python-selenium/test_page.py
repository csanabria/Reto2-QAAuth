
#ejecutar con: pytest desde la carpeta reto2-python-selenium

import time
from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
#from elements_manager import *


def test_validar_formulario_login():

    options = Options()
    options.add_argument("--start-maximized")
    #driver = webdriver.Chrome(executable_path=r"C:\Chrome\chromedriver.exe")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.demoblaze.com/index.html")

        # to click on the element(Log in) found
        #driver.find_element(By.ID, locator('#login2')).click()
        driver.find_element(By.ID, "login2").click()

        # Localizar campo Username y escribir valor
        driver.find_element(By.ID, "loginusername").send_keys("demoQA")

        # Localizar campo Password y escribir valor
        driver.find_element(By.ID, "loginpassword").send_keys("demo123")

        # Localizar botón Login y hacer clic
        driver.find_element(By.XPATH, "//button[text()='Log in']").click()

        #driver.find_element(By.ID, "loginusername").send_keys("tomsmith")
        #driver.find_element(By.ID, "loginpassword").send_keys("SuperSecretPassword!")

        #driver.find_element(By.ID, "login2").click()

        

        #driver.find_element(By.XPATH, "//button[contains(., 'Login')]").click()

        # Hacer clic en el botón de login
        # page.click("button[onclick='logIn()']")
        wait = WebDriverWait(driver, 20)
        # result_element = wait.until(
        #     EC.visibility_of_element_located((By.ID, "flash"))
        # )

        # assert "You logged into a secure area!" in result_element.text

        # Pausa para ver el resultado
        time.sleep(5)

    finally:
        driver.quit()




# to click on input field
#driver.find_element(By.XPATH,get_xpath(driver,'2ZTMmQKtlE26byf')).click()

# to click on the element(Log in) found
#driver.find_element(By.XPATH,get_xpath(driver,'GTHgpgxezo3vy3V')).click()
