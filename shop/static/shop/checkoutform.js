// pegar o elemento na pagina

// ao clicar no elemento quero que chame uma function 

// dentro da function, vai ler o valor que encontra dentro do elemento que sera manipulado

// se clicar no button de aumentar ou diminuir produtos,
//vai multiplicar o valor do produto pela quantidade

// o resultado da multiplicacao ira enviar de volta para a pagina

const totalValue = document.getElementById('totalValue');
const qtdOfProduct = document.getElementsByClassName('qtdOfProduct');
const shoppingForm = document.getElementById('shoppingForm');

let kingBedProduct = {
  qtd: 1,
  cost: 54.99,
}
let singleSofaProduct = {
  qtd: 1,
  cost: 74.99
}

function handleSubmit(e) {
  alert('Purchase Completed Successfully!')
  e.preventDefault()
};

function manipulateProductValue(product, addOrRemove) {
  if(addOrRemove === 'add') {
    product === 'kingBed' ?
    qtdOfProduct[0].innerHTML = String(kingBedProduct.qtd += 1) :
    qtdOfProduct[1].innerHTML = String(singleSofaProduct.qtd += 1)
  } else {
    if(product === 'kingBed') {
      kingBedProduct.qtd === 0 ?
      qtdOfProduct[0].innerHTML = String(kingBedProduct.qtd) :
      qtdOfProduct[0].innerHTML = String(kingBedProduct.qtd -= 1)
    } else {
      singleSofaProduct.qtd === 0 ?
      qtdOfProduct[1].innerHTML = String(singleSofaProduct.qtd) :
      qtdOfProduct[1].innerHTML = String(singleSofaProduct.qtd -= 1)
    } 
  }

  totalValue.innerHTML = `$${(
    ((kingBedProduct.qtd * kingBedProduct.cost) +
    (singleSofaProduct.qtd * singleSofaProduct.cost)
    + 50).toFixed(2)
  )}`
};

qtdOfProduct[0].innerHTML = String(kingBedProduct.qtd)
qtdOfProduct[1].innerHTML = String(singleSofaProduct.qtd)
totalValue.innerHTML = `$${(
  (kingBedProduct.qtd * kingBedProduct.cost) +
  (singleSofaProduct.qtd * singleSofaProduct.cost)
  + 50
)}`