# webscraperVivaReal
Raspagem de dados no site da imobiliária Viva Real
Busca: alugar -> apartamento -> Butantã
Erro: sempre retorna as mesmas informações de página web base, mesmo passando outras URL para pegar dados de outros endereços
      Acredito que o erro esteja na linha 30 do código fonte, em "aptos = soup.find_all(class_='js-card-selector')"
