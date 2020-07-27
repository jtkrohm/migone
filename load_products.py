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

prod = {"product":[{"item":"Bananas","picture":"./images/pexels/bananas.webp","vendor":[{"name":"John","price":20,"number":0}]}, 
 #{"item":"Bananas","picture":"./images/pexels/bananas.webp","vendor":[{"name":"John","price":20,"number": 0}]}, 
 #{"item":"Bluggoes","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 #{"item":"Breadfruit","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 {"item":"Butternut Squash","picture":"./images/pexels/butternut_squash.webp","vendor":[{"name":"John","price":20,"number": 0}]}, 
 {"item":"Cabbages","picture":"./images/pexels/cabbages","vendor":[{"name":"John","price":20,"number": 0}]}, 
 #{"item":"Callaloo","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 {"item":"Cantaloupes","picture":"./images/pexels/cantaloupes.webp","vendor":[{"name":"John","price":20,"number": 0}]}, 
 {"item":"Carrots","picture":"./images/pexels/carrots.webp","vendor":[{"name":"John","price":20,"number": 0}]}, 
 #{"item":"Celery","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 {"item":"Chive & thyme","picture":"./images/pexels/chive.webp","vendor":[{"name":"John","price":20,"number": 0}]}, 
 {"item":"Coconuts","picture":"./images/pexels/coconuts.webp","vendor":[{"name":"John","price":20,"number": 0}]}, 
 {"item":"Coconut Water","picture":"./images/pexels/coconut_water.webp","vendor":[{"name":"John","price":20,"number": 0}]}, 
 {"item":"Cucumbers","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 #{"item":"Dasheen","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 {"item":"Eggs","picture":"./images/pexels/eggs_dozen.webp","vendor":[{"name":"John","price":20,"number": 0}]}, 
 {"item":"Ginger","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 #{"item":"Honey","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 {"item":"Kale","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 {"item":"Lettuce","picture":"./images/pexels/lettuce.webp","vendor":[{"name":"John","price":20,"number": 0}]}, 
 {"item":"Limes","picture":"./images/pexels/limes.webp","vendor":[{"name":"John","price":20,"number": 0}]}, 
 {"item":"Nutmegs","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 {"item":"Ochroes","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 {"item":"Oranges","picture":"./images/pexels/oranges.webp","vendor":[{"name":"John","price":20,"number": 0}]}, 
 #{"item":"Patchoi","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 #{"item":"Parsley","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 #{"item":"Pinapples","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 #{"item":"Plantains","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 #{"item":"String Beans","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 #{"item":"Sea Moss","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 #{"item":"Seasoning  peppers","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 #{"item":"Sweet Potatoes","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 #{"item":"Tomatoes","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 #{"item":"Watermelons","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 #{"item":"Whole Chicken","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]}, 
 #{"item":"Yam","picture":"path/to/picture","vendor":[{"name":"John","price":20,"number": 0}]},
 ]}

html = ' ' 
html0 = ' '
html1 = ' '
html2 = ' '
html3 = ' '


for product in prod["product"]:
       html1 =  f'''
			        <article class="product">
					<h3 id="product-name"> {product["item"]} </h3>
					<br>
					<div class="img-container-prod">
						<img src="{product["picture"]}" alt="" class="product-img">
						<button class="bag-btn" data-id="1"><a href="tel: +14734091240"> Call Now </a> </button>
					</div>
					
					<div class="scrollproducts">
					'''
       for vendor in product["vendor"]:
              html2 = f'''    <div>
						<h3> {vendor["name"]} </h3>
						<h5> address</h5>
						<h5> {vendor["price"]} per lb </h5>
  						<a href="tel: +{vendor["number"]}" style="color: var(--mainRed)"> <h5> Call: +{vendor["number"]} </h5> </a>
					     </div>
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
   
