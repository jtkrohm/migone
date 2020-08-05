vendors = {"vendor":[{"name":"Mr. Rennie","picture":"./images/vendors/lettuce.webp","address":"St. Paul's","item":[{"item":"vegetable","price":20,"unit":"lbs","in stock":yes}]}, 
 








html = " "
html0 = " "
html1 = " "
html2 = " "


for vendor in vendors["vendor"]:
       html1 =  f'''
			        <div class="products-center"> 
			        <article class="product">
					<div class="img-container">
						<img src="./images/pexels/eggs_tray.webp" alt="" class="product-img">
						<button class="bag-btn" data-id="1"><a href="tel: +14734091240"> Call Now </a> </button>
					</div>
					<h2> Poultry Vendor @ St. Paul's </h2>
					<h5> eggs @ $20 per tray</h5>
					<h5> eggs @ $10 per dozen </h5>
				</article> 
			</div>	
			
'''
       html0 = html1 + html2 + html3
       html += html0


print (html)

text_file = open("vendors_text.txt", "w") 
n = text_file.write(html) 
text_file.close()
   
