import Modelos_Treinados
from sklearn.feature_extraction.text import CountVectorizer

Modelos_Treinados.gerar_csv()
#Modelos_Treinados.gerar_codigo_negativo(151)
#Modelos_Treinados.gerar_codigo_negativo_metodos(1)
#Modelos_Treinados.gerar_codigo_positivo(101)

def classificador_de_linguagem():
    svm = Modelos_Treinados.random_forest_treinado()
    codigo = ["function ABC(){ return 'abc';}","Using MvcCode; Using Apache; Console.Log('ABC')","from mvc import pymvc print('ABC') if (a < b): print('a menor que b')"]
    codigo = svm['vetor'].transform(codigo)

    print(svm['modelo'].predict(codigo))

def classificador_de_padrao(linguagem):
    print('Em desenvolvimento')

#classificador_de_linguagem()