import requests

api_url = 'https://viacep.com.br/ws/01001000/json/'

requisicao = requests.get(api_url)

dados_JSON = requisicao.json()

## Retorno dos dados JSON requisitados com método GET
print(f'\nJSON:\n {dados_JSON}\n') 

## Retorno dos dados JSON separados
cep = dados_JSON['cep']
cidade = dados_JSON['localidade']
estado = dados_JSON['uf']
print(f'''
DADOS SEPARADOS

CEP: {cep}

CIDADE: {cidade}

ESTADO: {estado}

''') 