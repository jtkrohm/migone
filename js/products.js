const prodList = [
"Bananas", "Bluggoes", "Breadfruit", "Butternut Squash", 
"Cabbages", "Callaloo", "Cantiloupe", "Carrots", 
"Celery", "Chive & thyme", "Christophene", "Coconut", 
"Coconut Water", "Cucumbers", "Dasheen", "Eggs", 
"Ginger", "Honey", "Kale", "Lettuce", "Limes", "Nutmegs", 
"Ochroes", "Oranges", "Patchoi", "Parsley", "Pinapples", 
"Plantains", "String Beans", "Sea Moss", "Seasoning Peppers", "Sweet Potatoes", "Tomatoes",
"Watermelon", "Whole Chicken", "Yam" ]; 

/* {"item":"Bananas","picture":"path/to/picture","vendor":[{"name":"price"}]},*/
  
let prodJSON = '{"product":{{"item":"Bananas","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Bananas","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Bluggoes","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Breadfruit","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Butternut Squash","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Cabbages","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Callaloo","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Cantiloupe","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Carrots","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Celery","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Chive & thyme","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Coconut","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Coconut Water","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Cucumbers","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Dasheen","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Eggs","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Ginger","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Honey","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Kale","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Lettuce","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Limes","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Nutmegs","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Ochroes","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Oranges","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Patchoi","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Parsley","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Pinapples","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Plantains","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"String Beans","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Sea Moss","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Seasoning  peppers","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Sweet Potatoes","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Tomatoes","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Watermelons","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Whole Chicken","picture":"path/to/picture","vendor":[{"name":"John","price":20}]}, 
 {"item":"Yam","picture":"path/to/picture","vendor":[{"name":"John","price":20}]},
 }};

let prodObj = JSON.parse(prodJSON);

function test() {
document.getElementById("products").innerHTML=  "Vendor @ St.Paul's" ;
}

