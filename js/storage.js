document.getElementById("cart-eggs").addEventListener("click", function(){
  localStorage.setItem("eggs-tray", "1");
  console.log(localStorage.getItem("eggs-tray"));
});

const buttons = document.querySelectorAll(".bag-btn");
console.log(buttons);


//buttons.forEach(button => {
//  button.addEventlistener("click", event=> {
