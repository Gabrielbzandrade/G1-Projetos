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
print(f"\nTeste de Criar Perfil no site {driver.title}")

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
    erro = "clicar voltar"
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "voltar")))
    elemento.click()

    sleep(2)
    erro = "clicar criar perfil"
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "criar_perfil")))
    elemento.click()
    
    sleep(1)
    erro = "digitar nome"
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "nome")))
    elemento.clear()
    elemento.send_keys("Sandra")
    
    sleep(1)
    erro = "digitar padrinho"
    elemento = driver.find_element(By.NAME, "padrinho")
    elemento.clear()
    elemento.send_keys("Hugo")
    
    sleep(1)
    erro = "digitar data de nascimento"
    elemento = driver.find_element(By.NAME, "data_nascimento")
    elemento.clear()
    elemento.send_keys("09/12/2003")
    
    sleep(1)
    erro = "digitar caracteristicas"
    elemento = driver.find_element(By.NAME, "caracteristicas")
    elemento.clear()
    elemento.send_keys("Artística e quieta")

    sleep(1)
    erro = "digitar historia"
    elemento = driver.find_element(By.NAME, "historia")
    elemento.clear()
    elemento.send_keys("Nunca teve acesso a uma educação de qualidade mas sempre gostou de desenhar")

    sleep(1)
    erro = "digitar sobre mim"
    elemento = driver.find_element(By.NAME, "sobre_mim")
    elemento.clear()
    elemento.send_keys("Meu sonho é ser uma pintora famosa")
    
    sleep(2)
    erro = "clicar cadastrar criança"
    elemento = driver.find_element(By.NAME, "cadastrar_aluno")
    elemento.click()
    
    sleep(4)
    erro = "printar tabela"
    tabela = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "tabela")))
    
    if "Sandra Hugo 09/12/2003 Artística e quieta Nunca teve acesso a uma educação de qualidade mas sempre gostou de desenhar Meu sonho é ser uma pintora famosa" in tabela.text:
        print("Teste realizado com Sucesso!")
    else:
        print("Falha no teste")

except:
    print(f"Erro: {erro}")

driver.quit()