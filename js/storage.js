document.getElementById("cart-eggs").addEventListener("click", function(){
  localStorage.setItem("eggs-tray", "1");
  console.log(localStorage.getItem("eggs-tray"));
});
