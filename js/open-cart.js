closeCart() {
  document.getElementById('cart0').style.visibility="hidden";
  document.getElementById('cart1').style.transform="translateX(-100vw)";
}

openCart() {
  document.getElementById('cart0').style.visibility="visible";
  document.getElementById('cart1').style.transform="translateX(0)";
}
