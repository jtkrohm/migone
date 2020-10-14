vendors = {"vendor":[{"name":"Mr. Rennie","picture":"./images/vendors/lettuce.webp","address":"St. Paul's","item":[{"item":"vegetable","price":20,"unit":"lbs","in stock":"yes"}]}, 
 {"name":"Poultry Vendor ","picture":"./images/vendors/eggs_tray.webp","address":"St. Paul's","item":[{"item":"Eggs","price":20,"unit":"tray","in stock":"yes"}, {"item":"Eggs","price":10,"unit":"dozen","in stock":"yes"}]}
]} 
 








html = " "
html0 = " "
html1 = " "
html2 = " "
html3 = " "


for vendor in vendors["vendor"]:
       html1 =  f'''
                                <article class="product">
					<h2> Poultry Farmer </h2>
					<br>
					<div class="img-container-prod">
						<img src="./images/pexels/eggs_dozen.webp" alt="" class="product-img">
						</div>
					<div class="scrollproducts"> '''
       for item in vendor["item"]:
                    html2 = f'''
					    <div>
						<h5> Eggs</h5>
						<h5> $10 per dozen </h5>
  						<h5> <a href="tel: +0"> Call: +14734091240 </a> </h5>
					    </div> '''
       html3 = f'''
                                        </div>
				</article> 
			</div>	
'''
       html0 = html1 + html2 + html3
       html += html0


print (html)

text_file = open("vendors_text.txt", "w") 
n = text_file.write(html) 
text_file.close()
   
