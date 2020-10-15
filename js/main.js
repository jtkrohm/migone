const thisYear = new Date().getFullYear();

//querySelect or getElement by id the footer
// setup up text in a function
//innerhtml ,innertext? /document write / create Element / 
// addList/ inner Child it to screen

document.getElementById('page-footer').innerHTML= ` 
		<br>
		<hr>
                <p> Copyright &copy; <span> ${thisYear} </span> migone.cc </p>
` ;
