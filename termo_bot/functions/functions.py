from unidecode import unidecode
from collections import Counter


# with tests
def remove_accents(text):
    """
    This function removes the accents from a `str`

    Parameters
    ----------
    text: ``str``
        The text to remove the accents

    Returns
    -------
    text: ``str``
        The text without the accents
    """
    return unidecode(text, "utf-8")

def palavra_check_len_1(palavra):
    resposta = f"São aceitas apenas palavras com cinco (5) letras, mas a palavra *'{palavra.upper()}'* tem apenas uma letra! \n"
    return resposta

def palavra_check_len_not_5(palavra):
    resposta = f"São aceitas apenas palavras com cinco (5) letras, mas a palavra *'{palavra.upper()}'* tem {len(palavra)} letras! \n"
    return resposta

# with tests
def palavra_check_letra_repetida(palavra):
    # verificando se tem letras repetidas
    if len(set(palavra)) != 5:
        palavra = palavra.upper()
        letras_repetidas = [k for k,v in Counter(palavra).items() if v>1]
        word = ""
        for letra in palavra:
            if letra in letras_repetidas:
                word += "*" + letra + "*"
            else:
                word += letra
        resposta = f"O banco de dados contém palavras com cinco (5) *letras distintas*, mas a palavra '{word}' possui letras repetidas. \n"
        return resposta
    else:
        return ""
























#
