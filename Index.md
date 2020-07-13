<!DOCTYPE html>
<html> 

	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title>Migonecc: Shop Grenada</title>

		<!-- custom css-->  
		<link rel="stylesheet" href="./css/styles.css" />

		<!-- font awesome -->
		<link rel="stylesheet" href="./css/all.css" /> <!--load all styles -->
		<script defer src="./all.js"></script> <!--load all styles -->

	</head>

	<body onload="startTime(); sectionTime();displayProducts(); getProducts();" >
		<!-- Nav Bar-->
		<nav class="navbar">
			<div class="navbar-center">
				<span class="nav-icon">
					<i class="fas fa-bars"></i> <!-- increase the size of the bar icon and the search ocon -->
				</span>
				<a href="./index.html"> <h2 class="nav-icon">Migone.cc</h2> </a>  <!--replace with logo -->
				<div class="cart-btn"> <!-- add style for "search-btn" and "user-btn" -->
					<span class="nav-icon">
						<i class="fas fa-search"></i>
					</span>
					<div class="cart-items">0</div> <!-- change to notification-items -->
				</div>
			</div>
		</nav>
		<!-- End of Nav Bar-->

		<!-- Cart icon will be sticky button on the top right of the page-->

		<!-- cart btn-->
		<!-- End of cart btn-->

        <!-- Banner -->
        <header class="hero">
			<div class="banner">
				<h1 class="banner-title"> Connect With Vendors Nationwide</h1>
					<button class="banner-btn"> Search Now </button>
			</div>
		</header>
		<!-- End of Banner-->
		<!-- Stores Section-->
		<section class="products">
			<div class="section-title">
				<h1> What's In Stock</h1>
			</div>
			<div class="products-center">
		
			</div>		
			<!-- end of stores section -->
			<br>
			<br>
			<br>
			<br>
			<br>
			<br>
			<br>
			<br>
			<!-- New Section -->
			<div class="section-title">
			<h2 id="open-hours"> </h2>
			<div id="clock" class="clock"></div> 

			</div>
			<!-- duplicate the products class for closing soon section -->
			<div class="products-center">
			<!-- single store-->
				<article class="product">
					<div class="img-container">
						<img src="./images/grocery.jpeg" alt="groceries" class="product-img">
						<button class="bag-btn" data-id="1"> Explore </button>
					</div>
					<h2> Store 1 </h2>
					<h4> closes at X pm </h4>
				</article>
				<!-- end of single store -->
			</div>		
			
     		<!-- cart-->
			<div class="cart-overlay">
				<div class="cart">
					<span class="close-cart">
						<i class="fas fa-window-close"></i>
					</span>
					<h2> Your List </h2>
					<div class="cart-content">
					<!-- Cart Item --> 
					<div class="cart-item">						
						<img  src="./images/grocery.jpeg" alt="product">
						<div>							
							<h4> Eggs </h4>
							<h5> $20 </h5>						
							<div class="remove-item"> remove </div>
						</div>						
						<div>
							<i class="fas fa-chevron-up"> </i>
							<p> 1 </p>
							<i class="fas fa-chevron-down"> </i>			
						</div>
					</div>					
					<div class="cart-footer">
						<span class="cart-total"> <h3> Total : $ 0 </h3> </span>
						<button class= "clear-cart 	banner-btn"> clear list </button>		
					</div>
				
				<!-- end of cart-->
				</div>
			</div>	
        <script src="clock.js"> </script>	
	    <script src="app.js"> </script>
        <script src="open_section.js"> </script> 
	</body>

</html>
