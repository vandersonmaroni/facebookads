# facebookads
## Configuração
É necessário criar um arquivo `config.py` colocando os dados necessários do **Facebook Ads**
### Arquivo config.py
```
class Config (object):
  def app_id:
    return "<app_id>"

  def app_secret:
    return "<app_secret>"

  def access_token:
    return "<access_token>"

  def account_id:
    return "<account_id>"
```

## Execução
Para executar o Script é necessário ativar o ambiente virtual
```
Scripts\activate
```
Depois executar o arquivo `.py`
```
python __init__.py
```
Estou colocando somente "python", mas estou utilizando o python3 na máquina
