document.getElementById("cart-eggs").addEventListener("click", function(){
  localStorage.setItem("eggs-tray", "1");
  alert(localStorage.getItem("eggs-tray"));
});

