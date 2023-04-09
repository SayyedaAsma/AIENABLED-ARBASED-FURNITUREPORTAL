const productAmt = document.getElementById('product_amt');
const shippingAmt = document.getElementById('shipping_amt');
const totalAmt = document.getElementById('total_cart_amt');
const error = document.getElementById('error_trw');

const decreaseNumber = (incdec, price) => {
  let textbox = document.getElementById(incdec);
  let amount = document.getElementById(price);
  if (textbox.value <= 0) textbox.value = 0;
  else {
    textbox.value = parseInt(textbox.value) - 1;
    textbox.style.background = '';
    amount.innerHTML = parseInt(amount.innerHTML) - 200;
    productAmt.innerHTML = parseInt(productAmt.innerHTML) - 200;
    shipping();
    totalAmt.innerHTML =
      parseInt(productAmt.innerHTML) + parseInt(shippingAmt.innerHTML);
  }
};

const increaseNumber = (incdec, price) => {
  let textbox = document.getElementById(incdec);
  let amount = document.getElementById(price);
  if (textbox.value >= 5) {
    textbox.style.background = 'red';
    alert('Maximum No. of items is 5');
  } else {
    textbox.value = parseInt(textbox.value) + 1;
    amount.innerHTML = parseInt(amount.innerHTML) + 200;
    productAmt.innerHTML = parseInt(productAmt.innerHTML) + 200;
    shipping();
    totalAmt.innerHTML =
      parseInt(productAmt.innerHTML) + parseInt(shippingAmt.innerHTML);
  }
};

const shipping = () => {
  if (productAmt.innerHTML >= 50) {
    shippingAmt.innerHTML = 0;
  } else if (productAmt.innerHTML <= 50) {
    shippingAmt.innerHTML = 50;
  } else {
    shippingAmt.innerHTML = 50;
  }
};

const discountCode = () => {
  let discount_code = document.getElementById('discount_code1');
  if (discount_code.value == 'gesypo') {
    totalAmt.innerHTML = parseInt(totalAmt.innerHTML) - 200;
  } else {
    error.innerHTML = 'Try Again! Valid code is gesypo';
  }
};