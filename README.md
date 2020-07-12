 
# Descrição 

 Script para conseguir informações básicas de CEP e Código de Rastreio utilizando Dados dos Correios , utilizando Requests e Beautifulsoup
 
## Utilização

* Informações do CEP

`python correios.py CEP`

* Código de Rastreio

` python correios.py XXXXXXXXX --c `

## Requerimentos

* Instalação dos Módulos pycep_correios , requests , bs4

`pip install pycep_correios && pip install requests && pip install bs4`


### Agradecimentos

 Ao Michell Stuttgart pelo módulo básico de pesquisa dos Correios.
 
 Ao Código do @rennancockles https://github.com/th3ch4os/rastreio por me servir de base para a implementação 
 do método POST via Requests
