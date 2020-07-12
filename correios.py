import pycep_correios , sys , requests 
from bs4 import BeautifulSoup
"""
Agradecimento      : Michell Stuttgart , @evertonmatos 
E ao Script de https://github.com/th3ch4os/rastreio/blob/master/rastreio , serviu de base para implementar e entender
Requests usando o método post

Alterações Básicas : TH3 CH4OS
"""


# Uso essa função para verificar se os parametros de fato existem
def list_check_value(value,lista):
  """[Verifica se um Value na List existe ou não]

  Args:
      value ([int]): [Index da lista]
      lista ([list]): [Lista Desejada]

  Returns:
      [bool]: [True ou False]
  """
  try:
    if (lista[int(value)] in lista):
      return True
  except IndexError:
    return False


if (list_check_value(1,sys.argv) == False):
     print('Digite Algo')
     quit()






def cep(x):
     print("========== CEP=============")
     #  O CEP é armazenado como um dicionário e utilizando o módulo get_address_from_cep()
     inf_cep = pycep_correios.get_address_from_cep(x) #sys.argv[1] irá pegar o input do usuário
     print("CEP         => {}".format(inf_cep["cep"]))
     print("Cidade      => {}".format(inf_cep["cidade"]))
     print("Estado      => {}".format(inf_cep["uf"]))
     print("Bairro      => {}".format(inf_cep["bairro"]))
     print("Endereço    => {}".format(inf_cep["logradouro"]))
     print("Complemento => {}".format(inf_cep["complemento"]))



def rastreio(codigo):
     print("==== Código de Rastreio ====")
     s     = requests.Session()
     payload = { 'objetos':codigo , 'btnPesq':'+Buscar'}
     s.headers.update({
        'Host': 'www2.correios.com.br',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://www2.correios.com.br/sistemas/rastreamento/default.cfm',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '37',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
                   })
     req  = s.post('https://www2.correios.com.br/sistemas/rastreamento/resultado.cfm?', data=payload, allow_redirects=True)
     req.encoding = 'ISO-8859-1'
     soup = BeautifulSoup(req.content,"html.parser")
     conteudo = soup.find_all('td')
     for i in conteudo:
          print(i.text)

if ( sys.argv[1] != '') and ( list_check_value(2,sys.argv)==False):
     cep(str(sys.argv[1]))



try:
     if ( sys.argv[2]== "--c"):
         rastreio(str(sys.argv[1]))
except IndexError:
     pass
