list = ["Bananas",
"Bluggoes",
"Breadfruit",
"Butternut Squash",
"Cabbages",
"Callaloo",
"Cantiloupe",
"Carrots",
"Celery",
"Chive & thyme",
"Christophene",
"Coconut",
"Coconut Water",
"Cucumbers",
"Dasheen",
"Eggs",
"Ginger",
"Honey",
"Kale",
"Lettuce",
"Limes",
"Nutmegs",
"Ochroes",
"Oranges",
"Patchoi",
"Parsley",
"Pinapples",
"Plantains",
"String Beans",
"Sea Moss",
"Seasoning Peppers",
"Sweet Potatoes",
"Tomatoes",
"Whole Chicken",
"Yam" ]

html = ' '


for product in list:
       html +=  f'''


			        <article class="product">
					<h2 id="product-name"> {product} </h2>
					<br>
					<div class="img-container-prod">
						<img src="./images/eggs_tray.webp" alt="" class="product-img">
						<button class="bag-btn" data-id="1"><a href="tel: +14734091240"> Call Now </a> </button>
					</div>
					
					<div class="scrollproducts">
						<div>
						<h3> Poultry Vendor @ St. Paul's </h3>
						<h5> $20 per tray</h5>
						<h5> $10 per dozen </h5>
						</div>
						<div>
						<h3> Poultry Vendor @ St. Paul's </h3>
						<h5> $20 per tray</h5>
						<h5> $10 per dozen </h5>
						</div>
						<div>
						<h3> Poultry Vendor @ St. Paul's </h3>
						<h5> $20 per tray</h5>
						<h5> $10 per dozen </h5>
						</div>
					</div>
				</article> 
			
'''

print (html)

