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
print(f"\nTeste de Criar Eventos no site {driver.title}")

try:
    sleep(2)
    erro = "clicar portal funcionarios"
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "portal_funcionarios")))
    elemento.click()

    sleep(3)
    erro = "clicar entrar"
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "entrar")))
    elemento.click()

    sleep(2)
    erro = "clicar atualizar calendário"
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "calendario")))
    elemento.click()
    
    sleep(1)
    erro = "digitar data"
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "data")))
    elemento.clear()
    elemento.send_keys("11/30/2023")
    
    sleep(1)
    erro = "digitar evento"
    elemento = driver.find_element(By.NAME, "evento")
    elemento.clear()
    elemento.send_keys("SR2")
    
    sleep(2)
    erro = "clicar salvar"
    elemento = driver.find_element(By.NAME, "salvar")
    elemento.click()
    
    sleep(4)
    erro = "printar tabela"
    tabela = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "tabelaCalendario")))
    
    if "Nov. 30, 2023 SR2" in tabela.text:
        print("Teste realizado com Sucesso!")
    else:
        print("Falha no teste")

except:
    print(f"Erro: {erro}")

driver.quit()