import pycep_correios 

#========================================================
# Correios Script 
#=======================================================



""" TodoList
[ X ] Pesquisa de CEP básica
[   ] Pesquisa de Código de Rastreio 
     - https://www2.correios.com.br/sistemas/rastreamento/default.cfm

"""

print("==== CEP Finder ====")
print()



inf_cep = pycep_correios.get_address_from_cep(sys.argv[1])

print("CEP         => {}".format(inf_cep["cep"]))
print("Cidade      => {}".format(inf_cep["cidade"]))
print("Estado      => {}".format(inf_cep["uf"]))
print("Bairro      => {}".format(inf_cep["bairro"]))
print("Endereço    => {}".format(inf_cep["logradouro"]))
print("Complemento => {}".format(inf_cep["complemento"]))

correios.Correios.get_encomenda('PY721171027BR')




#PY721171027BR