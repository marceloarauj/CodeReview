using Models.Cliente;

public Cliente novoCliente(double saldo){
    Cliente cliente = new Cliente();
    cliente.Saldo = saldo;
    cliente.PodeComprar = (Produto.Valor - cliente) > 0 ? true:false
    return cliente;
}
