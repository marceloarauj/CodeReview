from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import os

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

        if(linguagem == 'Csharp'):
            for arquivo in arquivos:
                arquivo_csharp = open(str(diretorio)+str(arquivo))
                dados['Codigo'].append((trata_dados(arquivo_csharp.read())))
                dados['Linguagem'].append(1)
                arquivo_csharp.close()
                
        if(linguagem == 'Javascript'):
            for arquivo in arquivos:
                arquivo_javascript = open(str(diretorio)+str(arquivo))
                dados['Codigo'].append((trata_dados(arquivo_javascript.read())))
                dados['Linguagem'].append(2)
                arquivo_javascript.close()

        if(linguagem == 'Python'):
            for arquivo in arquivos:
                arquivo_python = open(str(diretorio)+str(arquivo))
                dados['Codigo'].append(trata_dados((arquivo_python.read())))
                dados['Linguagem'].append(3)
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