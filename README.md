# Web Scraper VivaReal
@autor: ALEX DOS SANTOS SENA
email: alex.sena@usp.br 

PROJETO 

Parâmetros:
Alugar, Apartamento, Butantã - SP

Dados de interesse:
Endereço, Área, Banheiros, Vaga Garagem, Quartos, Aluguel, Condomínio, 

Passos:
1) Aprender as bibliotecas (requests, BeautifulSoup, selenium.webdriver, json)
2) Configurar as variáveis de ambiente para poder utilizar as bibs - no caso, utilizei Firefox (geckodriver)
3) Aprender a manipular o Selenium e a função .click()
4) Utilizar o Requests para pegar informações das páginas web, juntamente com as bibs do BeautifulSoup
5) Parsear os elementos html das páginas
6) Pegar os dados dos imóveis por paginação 

Resultados:
Foi possível acessar o site de maneira automatizada, selecionar os "buttons" para categorizar a busca por "Aluguel", "Apartamento", "Bairro".
Plano A: obter todos os acessos ao site de maneira automatizada, pelo Selenium e deixar o bairro como um parâmetro que poderia ser um input.
Porém, o botão "Busca" no site não funciona (nem mesmo manualmente);
Plano B: ir para link da primeira página gerado através de busca. Foi possível obter todos os dados de interesse da primeira página. 

Problemas e Erros:
Fazendo a paginação, embora o link por página fosse gerado e passado como parâmetro em URL, o "soup.find_all(class_='js-card-selector')"
encontrou os dados da primeira página em todas as páginas. Acredito que o erro esteja nessa função cujo o "js-card-selector" é lido como 
da primeira página. Não foi possível pegar os valores de IPTU, isto porque o problema de paginação consumiu a maior parte do tempo do projeto. 

Trabalhos inspirados:
Código Fonte TV
https://www.youtube.com/watch?v=Vxl5jUltHBo
https://github.com/gabrielfroes/webscraping_python_selenium

Digital Innovation One
https://www.youtube.com/watch?v=QzD86JyeKXE

Links úteis:
https://imasters.com.br/back-end/autenticacao-em-um-website-usando-selenium-python-exemplo-de-selenium-python
https://www.it-swarm.dev/pt/selenium/digitar-tecla-enter-retorno-no-selenio/968905201/#:~:text=ENTER%20%3D%20u%20'%5C%20ue007',-consulte%20a%20documenta%C3%A7%C3%A3o&text=se%20voc%C3%AA%20est%C3%A1%20procurando%20%22como,c%C3%B3digo%20definitivamente%20ir%C3%A1%20ajud%C3%A1%2Dlo.&text=Voc%C3%AA%20pode%20chamar%20submit(),qual%20voc%C3%AA%20digitou%20seu%20texto
