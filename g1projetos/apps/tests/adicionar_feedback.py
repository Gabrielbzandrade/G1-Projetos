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
print(f"\nTeste de Adicionar feedback no site {driver.title}")

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
    erro = "clicar feedback"
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "feedback")))
    elemento.click()
    
    sleep(1)
    erro = "digitar texto"
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "texto")))
    elemento.clear()
    elemento.send_keys("Um texto de possíveis melhorias aqui")
    
    sleep(2)
    erro = "clicar normal"
    elemento = driver.find_element(By.ID, "Normal")
    elemento.click()
    
    sleep(2)
    erro = "clicar enviar feedback"
    elemento = driver.find_element(By.NAME, "enviar_feedback")
    elemento.click()
    
    sleep(4)
    erro = "printar tabela"
    tabela = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "feedback")))
    
    if "Um texto de possíveis melhorias aqui Normal" in tabela.text:
        print("Teste realizado com Sucesso!")
    else:
        print("Falha no teste")

except:
    print(f"Erro: {erro}")

driver.quit()