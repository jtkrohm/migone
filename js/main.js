const thisYear = new Date().getFullYear();

//querySelect or getElement by id the footer
// setup up text in a function
//innerhtml ,innertext? /document write / create Element / 
// addList/ inner Child it to screen

document.getElementById('page-footer').innerHTML= ` 
		<br>
		<hr>
                <p> Copyright &copy; <span> ${thisYear} </span> migone.cc </p>

                <a href="https://www.instagram.com/migone.cc"> <i class="fab fa-instagram" id="footer-icon"> </i> </a>

                <i class="fab fa-facebook" id="footer-icon"></i> 

                <a href="https://api.whatsapp.com/send?phone=14734044438&text=example"> <i class="fab fa-whatsapp" id="footer-icon"> </i> </a>

                <p> <a href="/html/privacy.html">Privacy </a> </p>

                <p> <a href="/html/contact.html">Contact </a> </p>
  
                <p> <a href="/html/terms.html">Terms and Agreements </a> </p>
 
` ;
