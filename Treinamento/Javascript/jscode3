import Cliente from 'Models.js';
import Produto from 'Venda.js';

function novoCliente(saldo){
    var cliente = new Cliente();
    cliente.Saldo = saldo;
    cliente.PodeComprar = (Produto.Valor - cliente) > 0 ? true:false
    return cliente;
}
