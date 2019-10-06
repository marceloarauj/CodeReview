import Modelos_Treinados
from sklearn.feature_extraction.text import CountVectorizer
  


def classificador_de_linguagem():
    svm = Modelos_Treinados.random_forest_treinado()
    codigo = ['using']
    codigo = svm['vetor'].transform(codigo)

    print(svm['modelo'].predict(codigo))

def classificador_de_padrao(linguagem):
    