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
    erro = "clicar relato"
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "atualizacao")))
    elemento.click()
    
    sleep(1)
    erro = "digitar titulo"
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "titulo")))
    elemento.clear()
    elemento.send_keys("Sandra")

    sleep(1)
    erro = "digitar relato"
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "texto")))
    elemento.clear()
    elemento.send_keys("Ela participou de uma oficina de arte e pintou um quadro cheio de cores e sorrisos. Foi tão legal ver como ela estava concentrada, escolhendo as cores e desenhando com tanto carinho. Depois, ela mostrou para todos com um brilho nos olhos. A alegria que ela sentiu ao compartilhar sua obra nos deixou emocionados.")
    
    sleep(2)
    erro = "clicar feliz"
    elemento = driver.find_element(By.ID, "Feliz")
    elemento.click()
    
    sleep(2)
    erro = "clicar cadastrar relato"
    elemento = driver.find_element(By.NAME, "cadastrar_relato")
    elemento.click()
    
    sleep(4)
    erro = "printar tabela"
    tabela = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "tabela")))
    
    if "Sandra Ela participou de uma oficina de arte e pintou um quadro cheio de cores e sorrisos. Foi tão legal ver como ela estava concentrada, escolhendo as cores e desenhando com tanto carinho. Depois, ela mostrou para todos com um brilho nos olhos. A alegria que ela sentiu ao compartilhar sua obra nos deixou emocionados. Feliz" in tabela.text:
        print("Teste realizado com Sucesso!")
    else:
        print("Falha no teste")

except:
    print(f"Erro: {erro}")

driver.quit()