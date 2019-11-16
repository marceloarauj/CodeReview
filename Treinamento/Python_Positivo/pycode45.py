# Search for messages of python-brasil on yahoo

import re
import urllib2
from urllib import quote
import sys

def busca_pybrasil(query):
    """
    Funcao que busca por determinada query no site do yahoogrupos, python-brasil,
    e retorna um dicionario com: 'idmensagem':'titulo mensagem'

    TODO: Implementar no dicionario as paginas coseguintes (proximas..)
    """
    # variaveis
    conteudo = urllib2.urlopen('http://br.groups.yahoo.com/' + \
        'group/python-brasil/messagesearch?query='+quote(query)).read()
    links = re.findall('<a href="/group/python-brasil/message/(.*?)">',conteudo)
    titulos = re.findall('"/group/python-brasil/message/[0-9]*">(.*)</a>',conteudo)

    # ve se retornou algum titulo e algum link
    if links and titulos:
        pass
    else:
        return None

    # cria um dicionario
    dicionario = {}

    # loop pra criar o dicionario
    x = 0
    for i in links:
        dicionario[i] = titulos[x]
        x = x + 1

    # retorna o dicinario recem-criado
    return dicionario