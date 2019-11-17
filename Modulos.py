import subprocess
import sys

def importa_modulos():
    try:
        subprocess.call([sys.executable,"-m","pip","install","pandas"])
        subprocess.call([sys.executable,"-m","pip","install","numpy"])
        subprocess.call([sys.executable,"-m","pip","install","sklearn"])
        subprocess.call([sys.executable,"-m","pip","install","scipy"])
        subprocess.call([sys.executable,"-m","pip","install","seaborn"])
        subprocess.call([sys.executable,"-m","pip","install","openpyxl"])
        subprocess.call([sys.executable,"-m","pip","install","random-word"])

    except:
        print("ERRO NA INSTALAÇÃO DE MÓDULOS")

if __name__ == '__main__':
    importa_modulos()