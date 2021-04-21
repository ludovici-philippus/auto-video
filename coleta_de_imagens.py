from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class ColetaImagens():
    # Variáveis e constântes
    tema = str(input("Digite um tema ou algo que se relacione com sua miniatura: "))
    driver = webdriver.Firefox()

    def main(self):
        # Executa outras funções
        self.entrar_pexels()
        self.pesquisar_pexels()
        self.selecionar_imagem()
        self.baixar_imagem()

    def entrar_pexels(self):
        self.driver.get("https://www.pexels.com/pt-br/")

    def pesquisar_pexels(self):
        elem = self.driver.find_element_by_xpath("//div[@class='hero__search-container']//input[@name='s']")
        elem.clear()
        elem.send_keys(self.tema)
        elem.send_keys(Keys.ENTER)

    def selecionar_imagem(self):
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='js-search-filter-trigger-text']")))
        self.driver.get(f"{self.driver.current_url}/?orientation=landscape")
        elem = self.driver.find_element_by_xpath("//img[@class='photo-item__img']")
        elem.click()

    def baixar_imagem(self):
        time.sleep(3)
        elem = self.driver.find_element_by_xpath("//img[@class='js-photo-page-image-img']")
        elem.screenshot(f"{self.tema}.png")

coleta = ColetaImagens()
coleta.main()
