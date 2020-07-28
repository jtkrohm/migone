vendors = {"vendor":[{"name":"John","picture":"./images/vendors/bananas.webp","address":"St. Paul's","item":[{"item":"vegetable","price":20,"unit":"lbs","in stock":yes}]}, 
 








html = " "
html0 = " "
html1 = " "
html2 = " "


for vendor in vendors["vendor"]:
       html1 =  f'''
			        <article class="product">
					<h3> {product["item"]} </h3>
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
  						<h5> <a href="tel: +{vendor["number"]}"> Call: +{vendor["number"]} </a> </h5>
					     </div>
					'''
       html3 ='''
                                        </div>
				</article> 
			
'''
       html0 = html1 + html2 + html3
       html += html0


print (html)

text_file = open("vendors_html.txt", "w") 
n = text_file.write(html) 
text_file.close()
   
