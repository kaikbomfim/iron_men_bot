# IronBot - Chatbot da Academia Iron Men

A aplicação é um chatbot feito em python, para o atendimento do público que possui interesse em ingressar na academia Iron Men.

## Funcionalidades:

O atendente virtual esclarece informações a respeito da academia, como seu horário de funcionamento, localização, planos, principais equipamentos e modalidades. Perguntas dispoíveis:

1. Onde a Iron Men está localizada?
2. Qual é o horário de funcionamento da Iron Men?
3. Quais são os preços dos planos?
4. Há alguma taxa de inscrição?
5. A Iron Men oferece aulas experimentais?
6. Que tipos de equipamentos a Iron Men possui?
7. Além da musculação, a academia tem aulas de dança, artes marciais, pilates, yoga ou outras atividades?

## Configuração

Para utilizar a aplicação, é necessário ter o Python 3.7.9 e o Node.JS instalado em seu computador. Além disso, é preciso instalar as seguintes dependências:

- chatterbot==1.0.4
- chatterbot_corpus==1.2.0
- pytz
- flask

Para instalar as dependências, execute o seguinte comando no terminal:

```
pip install -r requirements.txt
```

## Como utilizar

Para utilizar o IronBot, execute, simultaneamente, os seguintes arquivos no terminal: `services.py` e `\chat\index.js`. Obs.: cada um dos arquivos devem ser executados em terminais distintos.

```
training.py --> Treinamento do chatbot para as possíveis perguntas (OBS_01)
services.py --> Arquivo principal do backend do programa
index.js --> Arquivo principal do frontend do programa, incializa a aplicação web na porta 3000
tests.py --> Arquivo de testes registrados com biblioteca unittest
```
Em seguida, acesse a aplicação através de um navegador, no endereço `localhost:3000` 

**OBS 01**: 

Certifique-se de que o robô está treinado. Isso pode ser verificado através da presença de um arquivo `db.sqlite3` dentre os arquivos nos diretórios. Caso não exista esse arquivo, deve-se treinar o chatbot para obter as informações. Isso pode ser feito através do arquivo `training.py`, **antes de executar os arquivos principais do programa**.

## Configuração de comandos

As mensagens estão configurados no diretório *conversations*. Para adicionar novos comandos, basta adicionar uma nova entrada no diretório, seguindo o seguinte formato:

```
 "conversations": [
        {
            "messages": [ "oi", "olá", "tudo bem?" ],
            "replies": "Olá, sou o IronBot, assistente virtual da academia Iron Men. Em que posso ajudar?"   
        },
        ...
 ]
```

Em seguida, deve-se treinar o chatbot para obter as novas informações, através do arquivo `training.py`.
