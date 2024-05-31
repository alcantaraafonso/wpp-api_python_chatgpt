# wpp-api_python_chatgpt
Este projeto é uma PoC para mostrar o funcionamento de uma aplicação em python que se comunica com a API do Whatsapp

## Pre-reqs
Criar uma aplicação no Meta for Developers e gerar um token permanente

## Execução 
Docker?

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

### Formatação de mensagens
```
*negrito* 
_itálico_ 
~riscado/tachado~ 
```
