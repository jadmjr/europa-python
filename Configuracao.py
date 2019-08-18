
class Configuracao:
    def __init__(self):

    def inicializa-navegador(self, webdriver driver):
        binary = FirefoxBinary('C:/Users/Morfeu/Documents/europa-python/geckodriver-v0.24.0-win64')
        driver = webdriver.Firefox()
        driver.get('http://google.com.br')
        