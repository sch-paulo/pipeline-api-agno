import requests

def extract():
    url = 'https://api.coinbase.com/v2/prices/spot'
    response = requests.get(url)
    return response.json()

def transform(dados_json):
    valor = dados_json['data']['amount']
    criptomoeda = dados_json['data']['base']
    moeda = dados_json['data']['currency']
    dados_tratados = {
        'valor': valor,
        'criptomoeda': criptomoeda,
        'moeda': moeda
    }
    return dados_tratados

if __name__ == '__main__':
    dados_json = extract()
    dados_tratados = transform(dados_json)
    print(dados_tratados)