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
print(f"\nTeste de Excluir Perfil no site {driver.title}")

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
    erro = "clicar acessar perfil"
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "acessarperfil")))
    elemento.click()

    sleep(2)
    erro = "clicar excluir perfil"
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "ir_para_excluir")))
    elemento.click()
    
    sleep(1)
    erro = "digitar nome"
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "nome")))
    elemento.clear()
    elemento.send_keys("Sandra")
    
    sleep(2)
    erro = "clicar excluir"
    elemento = driver.find_element(By.NAME, "excluir")
    elemento.click()
    
    sleep(4)
    erro = "printar tabela"
    tabela = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "tabela")))
    
    if "Sandra Hugo 09/12/2003 Artística e quieta Nunca teve acesso a uma educação de qualidade mas sempre gostou de desenhar Meu sonho é ser uma pintora famosa" not in tabela.text:
        print("Teste realizado com Sucesso!")
    else:
        print("Falha no teste")

except:
    print(f"Erro: {erro}")

driver.quit()