from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import os
import unicodedata
import requests,json
import traceback

"""método que trata os dados , motivo: a conversão do arquivo para string possui \n e não usar o replace
uma vez que remove os espaços em branco""" 

def trata_dados(codigo):
    retorno = ''
    for cod in codigo.splitlines():
        retorno = str(retorno) + str(cod) + ' '

    return retorno   

def obter_dados():
    linguagens = os.listdir("Treinamento")
    dados = {'Codigo':[],'Linguagem':[]}

    for linguagem in linguagens:
        arquivos = os.listdir("Treinamento/"+str(linguagem))
        diretorio = "Treinamento/"+str(linguagem) + "/"

        if(linguagem == 'Python_Negativo'):
            for arquivo in arquivos:
                arquivo_python = open(str(diretorio)+str(arquivo))
                dados['Codigo'].append(trata_dados((arquivo_python.read())))
                dados['Linguagem'].append(0)
                arquivo_python.close()

        if(linguagem == 'Python_Positivo'):
            for arquivo in arquivos:
                arquivo_python = open(str(diretorio)+str(arquivo))
                dados['Codigo'].append(trata_dados((arquivo_python.read())))
                dados['Linguagem'].append(1)
                arquivo_python.close()
        
    data = pd.DataFrame(dados)
    
    return data             

def kmeans_treinado():
    dados = obter_dados()

    count_vector = CountVectorizer()
    X_train = count_vector.fit_transform(dados['Codigo'])
    y_train = dados['Linguagem']
    

    km = KMeans()
    sup = svm.SVC(C=1, gamma="auto")
    sup.fit(X_train,y_train)
    codigo = count_vector.transform(codigo)


def svm_treinado():
    dados = obter_dados()
    count_vector = CountVectorizer()
    X_train = count_vector.fit_transform(dados['Codigo'])
    y_train = dados['Linguagem']
    sup = svm.SVC(C=1, gamma="auto")
    sup.fit(X_train,y_train)
    
    return {'vetor':count_vector,'modelo':sup}

def random_forest_treinado():
    dados = obter_dados()
    count_vector = CountVectorizer()
    X_train = count_vector.fit_transform(dados['Codigo'])
    y_train = dados['Linguagem']
    rdc = RandomForestClassifier()
    rdc.fit(X_train,y_train)
    return {'vetor':count_vector,'modelo':rdc}

def gerar_csv():
    excel = obter_dados()
    excel.to_excel(r'C:/Users/Marcelo/Desktop/database_ia/Codigos.xlsx')

def gerar_codigo_negativo(index):
    #gera 50 códigos negativos com palavras aleatorias
    indice = index +50

    local= 'C:/Users/Marcelo/Documents/GitHub\MachineLearning/Treinamento/Python_Negativo'
    
    chave_url = requests.get("https://random-word-api.herokuapp.com/key?")

    for i in range(index,indice):
        try:
            api_url = requests.get("https://random-word-api.herokuapp.com/word?key={}&number=4".format(chave_url.text))
            lista_palavras = json.loads(api_url.text,encoding='utf-8')

            filename = 'codigoruimteste' + str(i) + '.py'

            file = open(local + "/"+filename,"w+")

            classe = lista_palavras[0]
            classe = classe.capitalize()

            palavra1 = lista_palavras[1]
            palavra2 = lista_palavras[2]
            palavra_parametro = lista_palavras[3]
            
            file.write("class "+classe+": \n\n")

            file.write("def get_"+palavra1+": \n")
            file.write("\t return "+palavra1 + "\n\n")

            file.write("def get_"+palavra2+": \n")
            file.write("\t return "+palavra2 +"\n\n")

            file.write("def set_"+palavra1+"("+palavra_parametro+"_"+palavra1 +"): \n")
            file.write("\t"+palavra1 + " = "+palavra_parametro +"_"+palavra1 + "\n\n")

            file.write("def set_"+palavra2+"("+palavra_parametro+"_"+palavra2 +"): \n")
            file.write("\t"+palavra2 + " = "+palavra_parametro+ "_"+palavra2 +"\n\n")

            file.close()
        except:
            print("Erro")

def gerar_codigo_positivo(index):
    #gera 50 códigos positivos com palavras aleatorias
    indice = index +100

    local= 'C:/Users/Marcelo/Documents/GitHub\MachineLearning/Treinamento/Python_Positivo'
    
    chave_url = requests.get("https://random-word-api.herokuapp.com/key?")

    for i in range(index,indice):

        api_url = requests.get("https://random-word-api.herokuapp.com/word?key={}&number=4".format(chave_url.text))
        lista_palavras = json.loads(api_url.text,encoding='utf-8')

        filename = 'codigobomteste' + str(i) + '.py'

        file = open(local + "/"+filename,"w+")

        classe = lista_palavras[0]
        classe = classe.capitalize()

        palavra1 = lista_palavras[1]
        palavra2 = lista_palavras[2]
        palavra_parametro = lista_palavras[3]
            
        file.write("class "+classe+": \n\n")

        file.write("def "+palavra1+": \n")
        file.write("\t "+palavra2+" = "+palavra1+ " + "+ palavra2+"\n")
        file.write("\t return "+palavra2 + "\n\n")

        file.write("def "+palavra2+": \n")
        file.write("\t" + palavra1 + " = "+palavra2+ " + "+ palavra1 +"\n")
        file.write("\t return "+palavra1 +"\n\n")

        file.write("def "+palavra1+"("+palavra_parametro+"_"+palavra1 +"): \n")
        file.write("\t"+palavra1 + " = "+palavra_parametro +"_"+palavra1 + "\n\n")

        file.write("def "+palavra2+"("+palavra_parametro+"_"+palavra2 +"): \n")
        file.write("\t"+palavra2 + " = "+palavra_parametro+ "_"+palavra2 +"\n\n")

        file.close()

def gerar_codigo_negativo_metodos(index):
    #gera 50 códigos negativos com palavras aleatorias
    indice = index +50

    local= 'C:/Users/Marcelo/Documents/GitHub\MachineLearning/Treinamento/Python_Negativo'
    
    chave_url = requests.get("https://random-word-api.herokuapp.com/key?")

    for i in range(index,indice):
        try:
            api_url = requests.get("https://random-word-api.herokuapp.com/word?key={}&number=4".format(chave_url.text))
            lista_palavras = json.loads(api_url.text,encoding='utf-8')

            filename = 'codigoruimtestemetodo' + str(i) + '.py'

            file = open(local + "/"+filename,"w+")

            classe = lista_palavras[0]

            palavra1 = lista_palavras[1]
            palavra2 = lista_palavras[2]
            palavra_parametro = lista_palavras[3]
            
            file.write(classe+"."+palavra1+"()."+palavra2+"() \n")
            file.write(classe+"."+palavra1+"()."+palavra2+"()."+palavra_parametro+"()")

            file.close()
        except:
            print("Erro")