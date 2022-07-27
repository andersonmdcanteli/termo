"""
Python script to develop a telegram bot to help choose the best first word and best first pair of words for the game Termo.
"""
### ---------- IMPORTS ---------- ###

## ----- Python Imports ----- ##
import os
## -------------------------- ##

## ----- Imports Third part ----- ##
import pandas as pd
import telebot
from dotenv import load_dotenv
## ------------------------------ ##

## ----- Imports home made ----- ##
from functions import functions
## ----------------------------- ##
### ---------------------------- ###

### ---------- GETTING API_KEY ---------- ###
load_dotenv()
API_KEY = os.environ.get('API_KEY') # <----------------------------- insira a chave do BOT aqui
### ------------------------------------- ###

### ---------- CONSTANTS ---------- ###
RIGHT_ARROW = u'\u2794'
RIGHT_ARROW_STYLED = u'\u27A1'
EMOTICON = '\U0001F607'
### ------------------------------- ###

### ---------- DATASETS ---------- ###
df = pd.read_csv("df_palavra.csv")
df2 = pd.read_csv("df_palavra_2.csv")
### ------------------------------ ###


### ---------- CODE ---------- ###

## ----- initializing the robot ----- ##
bot = telebot.TeleBot(API_KEY)
## ---------------------------------- ##


## ----- COMMANDS ----- ##
# --- START --- #
@bot.message_handler(commands=['start'])
def start(message):
    """Função que retorna as principais funcionalidades do bot. Deve ser igual quando diz oi.
    """
    resposta = f"""
    Olá *{message.chat.username}*!
    Eu sou o *TermoBot*, e estou aqui para te ajudar aumentar as chances de ganhar no jogo TERMO! \n
    Para obter quais são as principais palavras para o primeiro chute, utilize:
    {RIGHT_ARROW_STYLED} top rank

    Para saber o ranking de uma palavra específica, utilize:
    {RIGHT_ARROW_STYLED} rank TERMO
    onde TERMO é uma palavra de 5 letras únicas.

    Para obter quais são os principais pares de palavras para os primeiros dois chutes, utilize:
    {RIGHT_ARROW_STYLED} top rank2

    Para saber o ranking de um par de palavras específico, utilize:
    {RIGHT_ARROW_STYLED} rank2 TERM1 TERM2
    onde TERM1 e TERM2 são duas palavras de 5 letras contendo letras não repetidas.


    {RIGHT_ARROW_STYLED} Para outras opções, digite *opções*
    """
    bot.send_message(message.chat.id, resposta, parse_mode="Markdown")
# ------------- #
## -------------------- ##


## ----- FUNÇÔES DE INTERAÇÂO ----- ##
# --- SOBRE --- #
def sobre_request(message):
    """Esta função deve ser acionada apenas quando for digitado uma única palavra que seja igual a "sobre"
    """
    request = message.text.split()
    if request[0].lower() == "sobre":
        return True
    else:
        return False

@bot.message_handler(func=sobre_request)
def send_sobre(message):
    """Esta função retorna informações sobre o bot, como as estatísticas e contato
    """
    request = f"""
    Olá *{message.chat.username}*! \n
    O TermoBot é um bot desenvolvido com Python que ajuda você a escolher uma boa palavra para jogar Termo (e suas variantes).

    Ele foi desenvolvido utilizando um banco de dados contendo mais de 250 mil palavras. O método para ranquear as palavras se baseia na estimativa da probabilidade de cada letra aparecer nas palavras de cinco letras do português, além de aplicar pesos considerando a posição das letras nas palavras. Para saber mais detalhes em relação aos cálculos, banco de dados e premissas adotadas, veja este [notebook](https://colab.research.google.com/drive/1vmq6Hq2CaDEudNHVUDNd9e6bS1fikJqj?usp=sharing).

    {RIGHT_ARROW_STYLED} Para saber mais sobre este projeto, veja nosso repositório no [github](https://github.com/andersonmdcanteli/termo). Todas as informações estão armazenadas lá!

    {RIGHT_ARROW_STYLED} Tem Dúvidas, comentários e sugestões? Entre em contato com o criador através de um dos seguintes canais:

    {RIGHT_ARROW} e-mail: andersonmdcanteli@gmail.com
    {RIGHT_ARROW} instagram: [@andersonmdcanteli](https://www.instagram.com/andersonmdcanteli/)
    {RIGHT_ARROW} facebook: [@canteli2207](https://www.facebook.com/canteli2207)
    {RIGHT_ARROW} linkedin: [anderson canteli](https://www.linkedin.com/in/anderson-canteli-7431624a)

    {EMOTICON}
    """

    bot.send_message(message.chat.id, request, parse_mode="Markdown", disable_web_page_preview=True)
# ------------- #


# --- OPCOES --- #
def opcoes_request(message):
    """Esta função deve ser acionada apenas quando for digitado uma única palavra qye seja igual a "opcoes"
    """
    request = message.text.split()
    if len(request) < 2 and functions.remove_accents(request[0].lower()) == "opcoes":
        return True
    else:
        return False

@bot.message_handler(func=opcoes_request)
def send_opcoes(message):
    """Esta função lista as opções de chaves
    """
    resposta = f"""
    *Chaves de informação:*
    {RIGHT_ARROW_STYLED} *ajuda*: {RIGHT_ARROW} ajuda geral sobre o TermoBot
    {RIGHT_ARROW_STYLED} *top*: {RIGHT_ARROW} ajuda sobre como obter os top primeiros chutes
    {RIGHT_ARROW_STYLED} *rank*: {RIGHT_ARROW} ajuda sobre como obter o rank de uma determinada palavra
    {RIGHT_ARROW_STYLED} *rank2*: {RIGHT_ARROW} ajuda sobre como obter o rank de duas palavras


    *Chaves de resultados:*
    {RIGHT_ARROW_STYLED} *top rank*: {RIGHT_ARROW} retorna uma lista com os 25 melhores chutes para a primeira palavra
    {RIGHT_ARROW_STYLED} *top rank num*: {RIGHT_ARROW} retorna uma lista com as palavras ranqueadas na posição "num" para uma única palavra
    {RIGHT_ARROW_STYLED} *top rank2*: {RIGHT_ARROW} retorna uma lista com os 25 melhores chutes para as duas primeiras palavras
    {RIGHT_ARROW_STYLED} *top rank2 num*: {RIGHT_ARROW} retorna uma lista com as palavras ranqueadas na posição "num" para os dois primeiros chutes
    {RIGHT_ARROW_STYLED} *rank TERMO*: {RIGHT_ARROW} retorna o ranking da palavra "TERMO"
    {RIGHT_ARROW_STYLED} *rank2 TERMO*: {RIGHT_ARROW} retorna uma lista de combinações com a palavra "TERMO" para os dois primeiros chutes
    {RIGHT_ARROW_STYLED} *rank2 TERM1 TERM2*: {RIGHT_ARROW} retorna o ranking do par de palavras "TERM1" e "TERM2"
    """

    bot.send_message(message.chat.id, resposta, parse_mode="Markdown")
# -------------- #



# --- Oi --- #
def oi_request(message):
    """Esta função deve retornar TRUE quando o usuario interage com saudações.
    """
    request = message.text.split()
    if len(request) > 0:
        request = functions.remove_accents(request[0])
        if request.lower() in ['oi', 'ola', 'hey', 'hi', 'hello']:
            return True
        else:
            return False
    else:
        return False

@bot.message_handler(func=oi_request)
def help_oi(message):
    """Ela é identica ao comando /start
    """
    start(message)
# ---------- #



# --- RANK --- #
def rank_request(message):
    """Esta função deve ser ativada quando a mensagem conter uma única palavra e ela for "rank"
    """
    request = message.text.split()
    if len(request) < 2 and request[0].lower() == "rank":
        return True
    else:
        return False

@bot.message_handler(func=rank_request)
def rank_help(message):
    """
    Esta é uma função de ajuda de como se utiliza a chave "rank".
    """
    resposta = f"""Ajuda para "*rank*" \n
    A chave "*rank*" é utilizada para obter o ranking de uma palavra.
    Para isto, basta passar uma palavra de cinco letras únicas após a chave *rank*. Por exemplo, para saber qual o ranking da palavra termo, basta:
    {RIGHT_ARROW_STYLED} rank termo

    {RIGHT_ARROW_STYLED} Para obter outras informações, digite *opções*
    """
    bot.send_message(message.chat.id, resposta, parse_mode="Markdown")
# ------------ #



# --- RANK TERMO --- #
def rank_request(message):
    """Esta função deve retornar TRUE se for passado 2 palavras e a primeira for rank
    """
    request = message.text.split()
    if len(request) == 2 and request[0].lower() == "rank":
        return True
    else:
        return False

@bot.message_handler(func=rank_request)
def send_rank(message):
    """Esta função deve ser acionada quando a mensagem enviada tiver 2 palavras, sendo que a primeira é 'rank'. Ela retorna o ranking da palavra passada na segunda posição

    rank TERMO

    testes:
    # ----- CORRETO ----- #

    rank afins --> retorna mensagem com a posição 2122
    rank serao --> retornar mensagem de top 10
    rank serão --> retornar mensagem de top 10
    rank induz --> retornar messagem de top 10 piores
    rank telão --> retornar mensagem de top 50
    # ----- ----- #


    # ----- INCORRETO ----- #
    rank falar --> erro de palavra repetida
    rank z --> erro de uma palavra
    rank tentar --> erro de 6 letras
    rank amor --> erro de 4 letras

    """
    palavra = functions.remove_accents(message.text.split()[1].upper())
    resposta = ""
    # caso tenho apenas 1 letra
    if len(palavra) == 1:
        resposta = functions.palavra_check_len_1(palavra)
    # caso não tenha 5 letras
    elif len(palavra) != 5:
        resposta = functions.palavra_check_len_not_5(palavra)
    # caso tenha letras repetidas
    else:
        resposta = functions.palavra_check_letra_repetida(palavra)
    # se resposta não for vazio, retornar o valor de resposta mesmo
    if resposta != "":
        pass
    # se passou pelos checks, resposta vai ser uma string vazia, e então verificar os resultados.
    else:
        # filtrando
        filtro = df[df['palavras'] == palavra]['rank_global_peso']
        # caso o resultado seja uma series nula, avusar que a palavra não consta no banco de dados
        if len(filtro) == 0:
            resposta = f"A palavra '{palavra}' não consta no banco de dados"
        # caso o filto tenha um resultado (esperado), retornar o ranking da palavra
        elif len(filtro) == 1:
            maximo = df['rank_global_peso'].max()
            if int(filtro) < 10:
                resposta = f"A palavra {palavra} esta na posição *{int(filtro)}* (de {maximo} posições)! Esta é uma palavra *TOP 10!!!*"
            elif int(filtro) < 50:
                resposta = f"A palavra {palavra} esta na posição *{int(filtro)}* (de {maximo} posições)! Ela é uma das melhores escolhas para o primeiro chute (*TOP 50*)!"
            elif int(filtro) > 3060:
                resposta = f"A palavra {palavra} esta na posição *{int(filtro)}* (de {maximo} posições)!. Ela é *TOP 10* no ranking de *PIORES* escolhas!"
            else:
                resposta = f"A palavra {palavra} esta na posição *{int(filtro)}* (de {maximo} posições)."
        else:
            resposta = f"Algo inesperado aconteceu! Por favor, entre em contato através de andersonmdcanteli@gmail.com infomando que um erro aconteceu ao utilizar a palavra '{palavras[0]}'!"

    bot.send_message(message.chat.id, resposta, parse_mode="Markdown")

# ------------------ #



# --- RANK2 --- #
def rank2_request(message):
    """Esta função deve ser ativada quando a mensagem conter uma única palavra e ela for "rank2"
    """
    request = message.text.split()
    if len(request) < 2 and request[0].lower() == "rank2":
        return True
    else:
        return False

@bot.message_handler(func=rank2_request)
def rank2_help(message):
    """
    Esta é uma função de ajuda de como se utiliza a chave "rank2".
    """
    resposta = f"""Ajuda para "*rank2*" \n
    A chave "*rank2*" é utilizada para obter o ranking de um par de palavras. Ela pode ser utilizada de duas formas:

    Para obter o ranking de um par de palavras, basta utilizar a chave *rank2* seguida das duas palavras de cinco letras únicas, da seguinte forma:
    {RIGHT_ARROW_STYLED} *rank2 term1 term2*

    A segunda forma retorna uma lista baseada em uma única palavra. Esta lista irá conter as melhores combinações encontradas com uma palavra especificada, jutamente com seu ranking. Por exemplo, para obter as combinações possíveis da palavra TERMO com as demais palavras do banco de dados que maximizam as chances de acerto, basta utilizar:
    {RIGHT_ARROW_STYLED} *rank2 TERMO*

    {RIGHT_ARROW_STYLED} Para obter outras informações, digite *opções*
    """

    bot.send_message(message.chat.id, resposta, parse_mode="Markdown")
# ------------- #



# --- RANK2 TERMO TERMO --- #
def rank2_request(message):
    """Para quando a mensagem tem 3 palavras e a primeira é 'rank2'
    """
    request = message.text.split()
    if len(request) == 3 and request[0].lower() == "rank2":
        return True
    else:
        return False

@bot.message_handler(func=rank2_request)
def send_rank2(message):
    """Esta função deve ser acinada quando o usuário solicita o rank de 2 palavras.
    A chave para ser acionada é a palavra 'rank2' seguido de duas palavras:

    rank2 TERMO TERMO

    testes:
    # ----- CORRETO ----- #

    rank2 afins cetro --> retornar valor correto, com mensagem generica
    rank2 cures pilao --> retornar valor correto, com mensagem top 10
    rank2 pilao cures --> retornar valor correto, com mensagem top 10
    rank2 licao mures --> retornar valro correto, com mensagem top 50
    rank2 lição mures --> retornar valro correto, com mensagem top 50
    rank2 cures PILÃO --> retornar valor correto, com mensagem top 10
    rank2 GLOSE INDUZ --> retornar valor correto, com mensagem top PIOR
    # ----- ----- #


    # ----- INCORRETO ----- #

    rank2 afins amor ---> retornar aviso dizendo que amor tem 4 letras
    rank2 amor afins ---> retornar aviso dizendo que amor tem 4 letras
    rank2 nao nada ----> retornar aviso dizendo que amor tem 4 letras e nao tem 4 letras
    rank2 amarelo afins -> retornar aviso dizendo que amarelo tem 7 letras
    rank2 cetro batman -> retornar aviso dizendo que batman tem 6 letras
    rank2 amarelo batman -> retornar aviso dizendo que amarelto tem 7 letras e batman tem 6 letras
    rank2 amora cetro -> retornar aviso dizendo que amora tem a repetido
    rank2 amora temer -> retornar aviso que amora tem a repetido e temer tem valor repetido
    rank2 a cetro -> retornar aviso que a tem 1 letra
    rank2 cetro b -> retornar aviso que b tem 1 letra
    # ----- ----- #

    """
    request = message.text.split()
    # obtendo as duas palavras
    palavras = [functions.remove_accents(request[1].upper()), functions.remove_accents(request[2].upper())]
    # verificando se a palavra tem 5 letras
    resposta = ""
    for palavra in palavras:
        # caso tenho apenas 1 letra
        if len(palavra) == 1:
            resposta += functions.palavra_check_len_1(palavra)
        # caso não tenha 5 letras
        elif len(palavra) != 5:
            resposta += functions.palavra_check_len_not_5(palavra)
        # caso tenha letras repetidas
        else:
            resposta += functions.palavra_check_letra_repetida(palavra)
    # se resposta não for vazio, não fazer nenhum check e retornar o valor de resposta mesmo
    if resposta != "":
        pass
    # se passou pelos checks, resposta vai ser uma string vazia, e então verificar os resultados.
    else:
        # filtrando
        # verificando as as duas palavras juntas existem
        df_filtro = df2[(df2['palavra_1'] == palavras[0]) & (df2['palavra_2'] == palavras[1])]
        # invertendo a combinação
        df_filtro_aux = df2[(df2['palavra_1'] == palavras[1]) & (df2['palavra_2'] == palavras[0])]
        # combinando o resultado
        df_filtro = pd.concat([df_filtro, df_filtro_aux], axis=0)

        # Caso o dataframe resultante seja vazio
        if len(df_filtro) == 0:
            resposta = f"O par de palavras '{palavras[0]}' e '{palavras[1]}' não consta no banco de dados!"
        # Caso o dataframe resultante seja cotenha um único resultado (esperado)
        elif len(df_filtro) == 1:
            # obtendo o ranking
            ranking = int(df_filtro['rank_global_peso'])
            # obtendo o número máximo de comparacoes
            max_comp = df2['rank_global_peso'].max()
            # se for top 10
            if ranking < 11:
                resposta = f"O par de palavras '{palavras[0]}' e '{palavras[1]}' esta na posição *{ranking}* (de um total de {max_comp} pares)! Este par de palavras é *TOP 10!!!*"
            # se for top 50
            elif ranking < 51:
                resposta = f"O par de palavras '{palavras[0]}' e '{palavras[1]}' esta na posição *{ranking}* (de um total de {max_comp} pares)! Ela é uma das melhores escolhas para os dois primeiros chutes (*TOP 50*)!"
            # se for top 10 piores
            elif ranking > (max_comp-10):
                resposta = f"O par de palavras '{palavras[0]}' e '{palavras[1]}' esta na posição *{ranking}* (de um total de {max_comp} pares)!. Ela é *TOP 10* no ranking de *PIORES* escolhas!"
            # outros casos resposta genérica
            else:
                resposta = f"O par de palavras '{palavras[0]}' e '{palavras[1]}' esta na posição *{ranking}* (de um total de {max_comp} pares)"
        # Caso o dataframe resultante seja cotenha mais de uma linha, algo esta errado!
        else:
            resposta = f"Algo inesperado aconteceu! Por favor, entre em contato através de andersonmdcanteli@gmail.com infomando que um erro aconteceu ao utilizar as palavras '{palavras[0]}' e '{palavras[1]}'!"

    bot.send_message(message.chat.id, resposta, parse_mode="Markdown")

# ------------------------- #



# --- RANK2 TERMO --- #
def rank2_comb_request(message):
    """Para quando a mensagem tem 2 palavras e a primeira é 'rank2'
    """
    request = message.text.split()
    if len(request) == 2 and request[0].lower() == "rank2":
        return True
    else:
        return False

@bot.message_handler(func=rank2_comb_request)
def send_rank2_comb(message):
    """Esta função deve ser acionada quando o usuário solicita o rank de 2 palavras, mas passa apenas a primeira
    A chave para ser acionada é a palavra 'rank2' seguido de UMA palavra:

    rank2 TERMO

    testes:
    # ----- CORRETO ----- #
    rank2 serao --> retorna resultados
    rank2 termo --> retorna 50 + resultados

    # ----- ----- #


    # ----- INCORRETO ----- #
    rank2 sera --> aviso que sera tem 4 letras
    rank2 a --> aviso que a tem 1 letra
    rank2 amarelo --> aviso que amarelo tem 7 letras
    rank2 cetre --> aviso que tem letra repetida

    # ----- ----- #

    """
    request = message.text.split()
    # obtendo as palavra
    palavra = functions.remove_accents(request[1].upper())
    # verificando se a palavra tem 5 letras
    resposta = ""
    # caso tenho apenas 1 letra
    if len(palavra) == 1:
        resposta = functions.palavra_check_len_1(palavra)
    # caso não tenha 5 letras
    elif len(palavra) != 5:
        resposta = functions.palavra_check_len_not_5(palavra)
    # caso tenha letras repetidas
    else:
        resposta = functions.palavra_check_letra_repetida(palavra)
    # se resposta não for vazio, retornar o valor de resposta mesmo
    if resposta != "":
        pass
    # se passou pelos checks, resposta vai ser uma string vazia, e então verificar os resultados.
    else:
        # filtrando
        # obtendo todas as linhas onde a palavra informada consta na coluna palavra_1
        df_filtro = df2[df2['palavra_1'] == palavra].copy()
        # obtendo todas as linhas onde a palavra informada consta na coluna palavra_2
        df_filtro2 = df2[df2['palavra_2'] == palavra].copy()
        # invertendo o nome das colunas no segundo dataframe para deixar a palavra solicidatada na primeira coluna
        df_filtro2.rename(columns={'palavra_1': 'palavra_2', 'palavra_2': 'palavra_1'}, inplace=True)
        # concatenando os dois dataframes
        df_filtro = pd.concat([df_filtro, df_filtro2], axis=0)
        # ordenando com base no rank
        df_filtro.sort_values(by="rank_global_peso", inplace=True)

        # Caso o dataframe resultante seja vazio
        if len(df_filtro) == 0:
            resposta = f"A palavra '{palavra}' não faz par com nenhuma outra palavra do banco de dados!"
        # Caso contraio
        else:
            # limitando o número de resultados para 50
            if df_filtro.shape[0] > 50:
                max_size = 50
                # adicionando um aviso de que existem mais resultados
                aviso = f"\n {RIGHT_ARROW_STYLED} são apresentados apenas as 50 melhores combinações (de {df_filtro.shape[0]})"
            else:
                # caso o tamanho não passe de 50, utilizar o df completo
                max_size = df_filtro.shape[0]
                aviso = ""
            # iterando para obter a resposta
            resposta = ""
            for index in range(max_size):
                resposta += (f"| {df_filtro['palavra_1'].iloc[index]} + {df_filtro['palavra_2'].iloc[index]} {RIGHT_ARROW}  {df_filtro['rank_global_peso'].iloc[index]}  | \n")
            # adicionando o aviso
            resposta += aviso

    bot.send_message(message.chat.id, resposta, parse_mode="Markdown")

# ------------------- #



# --- TOP --- #
def top_request(message):
    """Esta função deve ser ativada quando a mensagem conter uma única palavra e ela for "top"
    """
    request = message.text.split()
    if len(request) < 2 and request[0].lower() == "top":
        return True
    else:
        return False

@bot.message_handler(func=top_request)
def top(message):
    """
    Esta é uma função de ajuda de como se utiliza a chave "top".
    """
    resposta = f"""Ajuda para "*top*" \n
    A chave "*top*" é utilizada para obter uma lista com as **melhores escolhas** de palavras para o jogo Termo (e variantes).
    Para obter as top 25 palavras para o *PRIMEIRO* chute, utilize a chave *top rank*, desta forma:
    {RIGHT_ARROW_STYLED} top rank

    Caso queira uma lista com todas as palavras ranqueadas com um determinado rank, utilize a chave *top rank* seguida do número correspondente ao ranking desejado. Por exemplo, para obter uma lista de todas as palavras rankeadas na quadragésima segunda posição, utilize:
    {RIGHT_ARROW_STYLED} top rank 42

    Para obter os top 25 pares de palavras para os *DOIS PRIMEIROS* chutes, utilize a chave *top rank2*, desta forma:
    {RIGHT_ARROW_STYLED} top rank2

    Caso queira uma lista com todos os pares de palavras ranqueados com um determinado rank, utilize a chave *top rank2* seguida do número correspondente ao ranking desejado. Por exemplo, para obter uma lista de todos os pares de palavras rankeadas na quadragésima segunda posição, utilize:
    {RIGHT_ARROW_STYLED} top rank2 42
    \n

    {RIGHT_ARROW_STYLED} Para obter outras informações, digite *opções*
    """
    bot.send_message(message.chat.id, resposta, parse_mode="Markdown")

# ----------- #



# --- TOP RANK --- #
def top_rank_request(message):
    """Esta função deve ser acionada quando a mensagem tiver pelo menos 2 palavras, sendo que a primeira é top e a segunda é rank
    """
    request = message.text.split()

    if len(request) > 1 and request[0].lower() == "top" and request[1].lower() == "rank":
        return True
    else:
        return False

@bot.message_handler(func=top_rank_request)
def send_top_rank(message):
    """Esta função retorna uma lista das melhores palavras únicas para o primeiro chute, ou uma lista para um determinado ranking

    top rank -> retorna as 25 primeiras resultados

    top rank num -> retorna n primeiros resultados


    testes:
    # ----- CORRETO ----- #
    top rank -> retornar 25 resultados
    top rank 10 -> retornar resultado para rank 10
    top rank -1 -> retornar o pior resultado

    # ----- ----- #


    # ----- INCORRETO ----- #
    top rank 0 -> avisar ranking invalido
    top rank -0 -> avisar valor negativo
    top rank 3071 -> ranking exece limite

    # ----- ----- #


    """
    request = message.text.split()

    # caso tenha sido passado apenas top e rank, retornar os primeiros 25 resultados
    if len(request) == 2:
        resposta = ""
        for index in range(25):
            resposta += (f"| {df['palavras'].iloc[index]} {RIGHT_ARROW}  {df['rank_global_peso'].iloc[index]}  | \n")


    # caso tenha sido passsado top, rank e um número, retornar a quantidade de valores do número
    elif len(request) == 3:
        # verificar ser a terceira palavra é um número
        try:
            n_rank = int(request[2])
        except ValueError:
            # caso não, avisar que não foi possível
            resposta = f"O terceiro valor passado deve ser um número, mas recebemos {request[2]}"

        # verificando se o n_rank valor é igual a zero
        if n_rank == 0:
            resposta = f"Não existe nenhuma palavra com ranking igual a 0!"
        # verificando se n_rank é menor do que -1
        elif n_rank < -1:
            resposta = f"Com excessão da chave '-1' que retorna o pior ranking, valores negativos não são válidos (o ranking {n_rank} não é válido!)"
        # verificando se o rank desajado existe
        elif n_rank > df['rank_global_peso'].max():
            resposta = f"O conjunto de dados tem palavras classificados com ranking entre 1 e {df['rank_global_peso'].max()}, mas foi solicitado as palavra com ranking igual a {n_rank}, que não é um ranking válido!"
        # obtendo o pior rank
        elif n_rank == -1:
            df_filtro = df[df['rank_global_peso'] == df['rank_global_peso'].max()].copy()
            resposta = ""
            for index in range(df_filtro.shape[0]):
                resposta += (f"| {df_filtro['palavras'].iloc[index]} {RIGHT_ARROW}  {df_filtro['rank_global_peso'].iloc[index]}  | \n")
        # finalmente retornando o rank solicitado
        else:
            df_filtro = df[df['rank_global_peso'] == n_rank].copy()
            resposta = ""
            for index in range(df_filtro.shape[0]):
                resposta += (f"| {df_filtro['palavras'].iloc[index]} {RIGHT_ARROW}  {df_filtro['rank_global_peso'].iloc[index]}  | \n")


    # caso o tamanho da mensagem seja errado, avisar que ta errado
    else:
        resposta = f"""
        Chave não reconhida. Por favor, verifique a estrutura e tente novamente. Para maiores detalhes digite:
        {RIGHT_ARROW_STYLED} *top*
        {RIGHT_ARROW_STYLED} *opções*
        """



    bot.send_message(message.chat.id, resposta, parse_mode="Markdown")

# ---------------- #



# --- TOP RANK2 --- #
def top_rank2_request(message):
    """Esta função deve ser acionada quando a mensagem tiver pelo menos 2 palavras, sendo que a primeira é top e a segunda é rank2
    """
    request = message.text.split()

    if len(request) > 1 and request[0].lower() == "top" and request[1].lower() == "rank2":
        return True
    else:
        return False

@bot.message_handler(func=top_rank2_request)
def send_top_rank2(message):
    """Esta função retorna uma lista das melhores DUAS palavras únicas para os primeiros dois chutes, ou uma lista para um determinado rank.

    top rank2 -> retorna os 25 primeiros resultados

    top rank2 num -> retorna todos os resultados para o rank num


    testes:
    # ----- CORRETO ----- #
    top rank2 -> retornar 25 resultados (até o rank 17)
    top rank2 10 -> retornar 10 resultados com rank 10
    top rank2 30 -> retornar 10 resultados com rank 30 (4 resultados)
    top rank2 -1 -> retornar o pior resultado (rank = 189718)

    # ----- ----- #


    # ----- INCORRETO ----- #
    top rank -10 -> avisar valor negativo
    top rank2 0 -> avisar ranking inválido
    top rank2 189719 -> avisar ranking
    top rank2 1 1 -> avisar que a chave não foi reconhecida
    # ----- ----- #


    """
    request = message.text.split()

    # caso tenha sido passado apenas top e rank, retornar os primeiros 25 resultados
    if len(request) == 2:
        resposta = ""
        for index in range(25):
            resposta += (f"| {df2['palavra_1'].iloc[index]} + {df2['palavra_2'].iloc[index]} {RIGHT_ARROW}  {df2['rank_global_peso'].iloc[index]}  | \n")

    # caso tenha sido passsado top, rank e um número, retornar a quantidade de valores do número
    elif len(request) == 3:
        # verificar ser a terceira palavra é um número
        try:
            n_rank = int(request[2])
        except ValueError:
            # caso não, avisar que não foi possível
            resposta = f"O terceiro valor passado deve ser um número, mas recebemos {request[2]}"

        # verificando se o n_rank valor é igual a zero
        if n_rank == 0:
            resposta = f"Não existe nenhuma palavra com ranking igual a 0!"
        # verificando se n_rank é menor do que -1
        elif n_rank < -1:
            resposta = f"Com excessão da chave '-1' que retorna o pior ranking, valores negativos não são válidos (o ranking {n_rank} não é válido!)"
        # verificando se o rank desajado existe
        elif n_rank > df2['rank_global_peso'].max():
            resposta = f"O conjunto de dados tem pares de palavras classificados com ranking entre 1 e {df2['rank_global_peso'].max()}, mas foi solicitado os pares de palavra com ranking igual a {n_rank}, que não é um ranking válido!"
        # obtendo o pior rank
        elif n_rank == -1:
            df_filtro = df2[df2['rank_global_peso'] == df2['rank_global_peso'].max()].copy()
            resposta = ""
            for index in range(df_filtro.shape[0]):
                resposta += (f"| {df_filtro['palavra_1'].iloc[index]} + {df_filtro['palavra_2'].iloc[index]} {RIGHT_ARROW}  {df_filtro['rank_global_peso'].iloc[index]}  | \n")
        # finalmente retornando o rank solicitado
        else:
            df_filtro = df2[df2['rank_global_peso'] == n_rank].copy()
            resposta = ""
            for index in range(df_filtro.shape[0]):
                resposta += (f"| {df_filtro['palavra_1'].iloc[index]} + {df_filtro['palavra_2'].iloc[index]} {RIGHT_ARROW}  {df_filtro['rank_global_peso'].iloc[index]}  | \n")


    # caso o tamanho da mensagem seja errado, avisar que ta errado
    else:
        resposta = f"""
        Chave não reconhida. Por favor, verifique a estrutura e tente novamente. Para maiores detalhes digite:
        {RIGHT_ARROW_STYLED} *top*
        {RIGHT_ARROW_STYLED} *opções*
        """



    bot.send_message(message.chat.id, resposta, parse_mode="Markdown")

# ----------------- #

## -------------------------------- ##


## ----- polling the bot ----- ##
if __name__ == "__main__":
    bot.infinity_polling()
## --------------------------- ##


### -------------------------- ###
