from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

service = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

try:
    driver.get("https://demoqa.com/automation-practice-form")

    driver.implicitly_wait(10)

    campo_nome = driver.find_element(By.ID, "firstName")
    campo_nome.send_keys("Thalita")

    time.sleep(1)

    campo_sobrenome = driver.find_element(By.ID, "lastName")
    campo_sobrenome.send_keys("Teles")

    time.sleep(1)

    campo_email = driver.find_element(By.ID, "userEmail")
    campo_email.send_keys("thalita.teles@example.com")

    time.sleep(1)

    campo_genero = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
    campo_genero.click()

    time.sleep(1)

    campo_numero = driver.find_element(By.ID, "userNumber")
    campo_numero.send_keys("9876543210")

    time.sleep(1)

    campo_data_nascimento = driver.find_element(By.ID, "dateOfBirthInput")
    campo_data_nascimento.send_keys("1990-01-01")

    time.sleep(1)

   
    time.sleep(5)

finally:
    driver.quit()
