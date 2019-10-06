import Modelos_Treinados
from sklearn.feature_extraction.text import CountVectorizer
  

svm = Modelos_Treinados.svm_treinado()
codigo = ['function soma() { var a = 20; var b = 30; return a + b }']
codigo = svm['vetor'].transform(codigo)

print(svm['modelo'].predict(codigo))

def identificacao_da_linguagem():
    print("A")