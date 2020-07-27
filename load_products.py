list = ["Bananas",
"Bluggoes",
"Breadfruit",
"Butternut Squash",
"Cabbages",
"Callaloo",
"Cantaloupe",
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

prod = {"product":[{"item":"Bananas","picture":"./images/pexels/bananas.webp","vendor":[{"name":"John","price":20}]}, 
 #{"item":"Bananas","picture":"./images/pexels/bananas.webp","vendor":[{"name":"John","price":20}]}, 
 #{"item":"Bluggoes","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 #{"item":"Breadfruit","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Butternut Squash","picture":"./images/pexels/butternut_squash.webp","vendor":[{"name":"John","price":20}]}, 
 {"item":"Cabbages","picture":"./images/pexels/cabbages","vendor":[{"name":"John","price":20}]}, 
 #{"item":"Callaloo","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Cantaloupes","picture":"./images/pexels/cantaloupes.webp","vendor":[{"name":"John","price":20}]}, 
 {"item":"Carrots","picture":"./images/pexels/carrots.webp","vendor":[{"name":"John","price":20}]}, 
 #{"item":"Celery","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Chive & thyme","picture":"./images/pexels/chive.webp","vendor":[{"name":"John","price":20}]}, 
 {"item":"Coconuts","picture":"./images/pexels/coconuts.webp","vendor":[{"name":"John","price":20}]}, 
 {"item":"Coconut Water","picture":"./images/pexels/coconut_water.webp","vendor":[{"name":"John","price":20}]}, 
 {"item":"Cucumbers","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 #{"item":"Dasheen","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Eggs","picture":"./images/pexels/eggs_dozen.webp","vendor":[{"name":"John","price":20}]}, 
 {"item":"Ginger","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 #{"item":"Honey","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Kale","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Lettuce","picture":"./images/pexels/lettuce.webp","vendor":[{"name":"John","price":20}]}, 
 {"item":"Limes","picture":"./images/pexels/limes.webp","vendor":[{"name":"John","price":20}]}, 
 {"item":"Nutmegs","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Ochroes","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Oranges","picture":"./images/pexels/oranges.webp","vendor":[{"name":"John","price":20}]}, 
 #{"item":"Patchoi","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 #{"item":"Parsley","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 #{"item":"Pinapples","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 #{"item":"Plantains","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 #{"item":"String Beans","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 #{"item":"Sea Moss","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 #{"item":"Seasoning  peppers","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 #{"item":"Sweet Potatoes","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 #{"item":"Tomatoes","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 #{"item":"Watermelons","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 #{"item":"Whole Chicken","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 #{"item":"Yam","picture":"path/to/picture","vendor":[{"name":"John","price":20}]},
 ]}

html = ' ' 
html0 = ' '
html1 = ' '
html2 = ' '
html3 = ' '


for product in prod["product"]:
       html1 =  f'''
			        <article class="product">
					<h2 id="product-name"> {product["item"]} </h2>
					<br>
					<div class="img-container-prod">
						<img src="{product["picture"]}" alt="" class="product-img">
						<button class="bag-btn" data-id="1"><a href="tel: +14734091240"> Call Now </a> </button>
					</div>
					
					<div class="scrollproducts">
						'''
       for vendor in product["vendor"]:
              html2 = f'''              <div>
						<h3> {vendor["name"]} </h3>
						<h5> address</h5>
						<h5> {vendor["price"]} per lb </h5>
						</div>
						<div>
					'''
       html3 ='''
					</div>
				</article> 
			
'''
       html0 = html1 + html2 + html3
       html += html0


print (html)

text_file = open("products_html.txt", "w") 
n = text_file.write(html) 
text_file.close()
   
