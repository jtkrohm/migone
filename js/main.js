//core js files  ##
//page-specific js files
//modular js files

const thisYear = new Date().getFullYear();
const openCartBtn = document.getElementById('open-cart-icon');
const closeCartBtn = document.getElementById('close-cart-icon');
const cartOverlay = document.getElementById('cart0');
const actualCart = document.getElementById('cart1');
const pageHeaderBtn = document.getElementById('page-header-btn');
const pageHeader = document.getElementById('page-header');
const pageFooter = document.getElementById('page-footer');

window.addEventListener('DOMContentLoaded', function() {
    pageFooter.innerHTML= ` 
		<br>
		<hr>
                <p> Copyright &copy; <span> ${thisYear} </span> migone.cc </p>

                <a href="https://www.instagram.com/migone.cc"> <i class="fab fa-instagram" id="footer-icon"> </i> </a>

                <i class="fab fa-facebook" id="footer-icon"></i> 

                <a href="https://api.whatsapp.com/send?phone=14734044438&text=example"> <i class="fab fa-whatsapp" id="footer-icon"> </i> </a>

                <p> <a href="/html/privacy.html">Privacy </a> </p>

                <p> <a href="/html/contact.html">Contact </a> </p>
  
                <p> <a href="/html/terms.html">Terms and Agreements </a> </p> ` ;
});

/*
pageHeaderBtn.addEventListener('click', function() {
    pageHeader.style.transform="translateY(-100%)" ;
    pageHeader.style.z-index="-1" ;
});
*/

openCartBtn.addEventListener('click', function() {
    cartOverlay.style.visibility="visible";
    actualCart.style.transform="translateX(0)";
   // alert('open cart works');
});

closeCartBtn.addEventListener('click', function() {
    cartOverlay.style.visibility="hidden";
    actualCart.style.transform="translateX(-100vw)";
});

cartOverlay.addEventListener('click', function() {
    cartOverlay.style.visibility="hidden";
    actualCart.style.transform="translateX(-100vw)";
});


