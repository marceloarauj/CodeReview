import Modelos_Treinados
from sklearn.feature_extraction.text import CountVectorizer
  

svm = Modelos_Treinados.random_forest_treinado()
codigo = ['using']
codigo = svm['vetor'].transform(codigo)

print(svm['modelo'].predict(codigo))

def identificacao_da_linguagem():
    print("A")