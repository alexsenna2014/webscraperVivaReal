import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

all_apto = []
for i in range(1,16):
    url_base = "https://www.vivareal.com.br/aluguel/sp/sao-paulo/zona-oeste/butanta/apartamento_residencial/?__vt=lgpd:a&pagina="
    
    option = Options()
    option.headless = True
    driver = webdriver.Firefox(options=option)

    time.sleep(5)

    page_index = str(i)
    page = url_base + page_index

    driver.get(page)    

# Faz o parser da página web:
    res = requests.get(page)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

# Seleciona todos os elementos de determinada classe:
    aptos = soup.find_all(class_='js-card-selector')

# Seleciona os atributos de interesse de cada elemento e os armazena em um dicionário:
    for apto in aptos:
        info = apto.find(class_='property-card__main-content')
        end = info.h2.span.text
        detalhe = info.ul.text
        valor = info.section.text

        all_apto.append({'endereço': end, 'informações': detalhe, 'preço': valor})
    
    driver.quit()

# Converter e salvar em um arquivo JSON
with open('vivareal_scraper.json', 'w', encoding='utf-8') as jp:
    js = json.dumps(all_apto, indent=4)
    jp.write(js)