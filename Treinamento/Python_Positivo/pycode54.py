#!/usr/bin/python

# Uso:
# $ python parametros.py -o argumento_requerido
# teste
# 

from optparse import OptionParser

def main():
    parser = OptionParser()

    parser.add_option("-f", "--arquivo",  help="Imprime em arquivo")
    parser.add_option("-q", "--silencia", help="Não imprime a mensagem de saída")
    parser.add_option("-o", "--saida",    help="Imprime a mensagem de saída")

    (options, args) = parser.parse_args()

    if options.arquivo:
        import codecs
        f = codecs.open('optparse_teste.txt', 'a', 'utf-8')
        f.write("teste")
        f.close()
                
    if options.silencia:
        print ("")
        
    if options.saida:
        print ("teste")

if __name__ == "__main__":
    main()