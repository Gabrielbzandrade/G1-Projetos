from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

PATH = webdriver.ChromeService(executable_path="C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=PATH)

driver.get("http://127.0.0.1:8000/")
print(f"\nTeste de Acessar Afilhados no site {driver.title}")

try:
    sleep(2)
    erro = "clicar portal padrinhos"
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "portal_padrinhos")))
    elemento.click()

    sleep(3)
    erro = "clicar entrar"
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "entrar")))
    elemento.click()

    sleep(2)
    erro = "clicar calendario"
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "calendario")))
    elemento.click()

    for _ in range(3):
        sleep(1)
        driver.execute_script('window.scrollBy(0, 200)')

    sleep(3)
    
except:
    print(f"Erro: {erro}")

driver.quit()