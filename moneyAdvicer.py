import requests

def pegarcotacoes(cod_moeda):
    try:
        requisicao = requests.get(f"https://economia.awesomeapi.com.br/json/last/{cod_moeda}-BRL")
        # return requisicao.json()
        requisicao_dic = requisicao.json()
        # return requisicao_dic['GBPBRL']['bid']
        cotacao = requisicao_dic[f'{cod_moeda}BRL']['bid']
        return cotacao
    except:
        print('Código da moeda inválido!')
        return None

# print(pegarcotacoes('GBP'))