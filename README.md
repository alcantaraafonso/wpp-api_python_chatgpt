# wpp-api_python_chatgpt
Este projeto é uma PoC para mostrar o funcionamento de uma aplicação em python que se comunica com a API do Whatsapp

## Pre-reqs
Criar uma aplicação no Meta for Developers e gerar um token permanente

## Execução 
A aplicação roda sobre um container docker e para executá-la, rode:

```
docker build -t wppapi_python .

docker run -dp 8000:8000 --name wppapi_python wppapi_python
```

## deploy
AWS?

## Testes da API do Whatsapp
Foi usado a extensão do Postman no VSCode com a seguinte chamada. Para realizar esta chamada, é necessário criar um token de autorização no Meta For Developers, da Meta.

Use a API do whatapp relativa a sua aplicação criada no Meta For Developers e faça uma requisição POST 
```json
{ "messaging_product": "whatsapp", "to": "<num tel destino>", "type": "template", "template": { "name": "hello_world", "language": { "code": "en_US" } } }
```

O resultado da chamada é:

```json
{
    "messaging_product": "whatsapp",
    "contacts": [
        {
            "input": "<num tel destino>",
            "wa_id": "<num tel destino>"
        }
    ],
    "messages": [
        {
            "id": "wamid.HBgNNTUxMTk4NDMxNzQ0NhUCABEYEkQyOTE1ODExRjBENjZDMjU0NQA=",
            "message_status": "accepted"
        }
    ]
}
```
Para mais informações sobre as API do Whatsapp Cloud, acesse: https://www.postman.com/meta/workspace/whatsapp-business-platform/collection/13382743-84d01ff8-4253-4720-b454-af661f36acc2

### Formatação de mensagens whatsapp
```
*negrito* 
_itálico_ 
~riscado/tachado~ 
```

### Preços
*User Initiated*: Se inicia quando uma empresa responde ao usuário. Cobrança por conversão, que incluem todas as mensagens, num intervalo de 24hrs.<br>
*Business Initiated*: Se inicia quando uma empresa manda uma mensagem ao usuário. As mensagens devem ser do tipo Template

Mais informações: https://developers.facebook.com/docs/whatsapp/pricing
