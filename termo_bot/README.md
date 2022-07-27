# TermoBot

Termo Bot é um robô para Telegram desenvolvido para ajudar na escolha de quais letras utilizar para dominar o jogo Termo. Ele é baseado em uma análise estatística que esta disponível em um outro folder neste repositório.

O TermoBot foi desenvolvido utilizando pyTelegramBotAPI (4.6.1) como interface com o Telegram, e os dados são gerenciados através do Pandas (1.4.3).

Esta é uma aplicação simples, porém instrutiva e muito útil para quem deseja melhorar seus resultados em jogos do tipo Termo

Para rodar este robô, instale as seguintes dependências:

- pip install pyTelegramBotAPI
- pip install pandas
- pip install unidecode
- pip install python-dotenv


ou se preferir:

> pip install requirements.txt


Após instalar as dependências, ative o ambiente virtual e execute o arquivo `app.py` para inicializar o servidor. Mas, para que o robô se conecte com o Telegram é necessário criar uma chave através do BotFather. Esta API_KEY deve ser inserida na linha 23 do script `app.py`.


<p align="center">
<img src="https://raw.githubusercontent.com/andersonmdcanteli/termo/main/images/screenshot.PNG" alt="screenshot do TermoBot ao ser inicializado e com a solicitação do ranking da palavra termo" width="800px">
</p>
