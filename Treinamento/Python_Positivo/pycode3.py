from 'models' import 'Models'
from 'Venda' import 'Produtos'

def novoCliente(saldo):
    cliente =  Cliente()
    cliente.Saldo = saldo
    cliente.PodeComprar = false
    
    if (Produto.Valor - saldo) > 0:
        cliente.PodeComprar = true
    
    return cliente

