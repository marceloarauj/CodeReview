
function mostrarCarro() {
    var carro = 'Fusca';
    console.log(carro);
  }
  
  mostrarCarro(); 
  console.log(carro); 

  function mostrarCarro() {
    carro = 'Fusca';
    console.log(carro);
  }
  mostrarCarro(); 
  console.log(carro); 

  var carro = 'Fusca';
  
  function mostrarCarro() {
    var frase = `Meu carro é um ${carro}`;
    console.log(frase);
  }
  
  mostrarCarro(); 
  console.log(carro);  

  
  if(true) {
    var carro = 'Fusca';
    console.log(carro);
  }
  console.log(carro); 

  if(false) {
    var carro = 'Fusca';
    console.log(carro);
  }
  console.log(carro); 
  
  
  if(true) {
    const carro = 'Fusca';
    console.log(carro);
  }
  console.log(carro); 
  {
    var carro = 'Fusca';
    const ano = 2018;
  }
  console.log(carro); 
  console.log(ano); 
  
  
  for(var i = 0; i < 10; i++) {
    console.log(`Número ${i}`);
  }
  console.log(i); // 10
  
  for(let i = 0; i < 10; i++) {
    console.log(`Número ${i}`);
  }
  console.log(i); 
  
    
  const mes = 'Dezembro';
  mes = 'Janeiro'; 
  const semana; 
  
  const data = {
    dia: 28,
    mes: 'Dezembro',
    ano: 2018,
  }
  
  data.dia = 29; 
  data = 'Janeiro'; 

  
  let ano;
  ano = 2018;
  ano++;
  console.log(ano); 
  
  let ano = 2020;