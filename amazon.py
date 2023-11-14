import requests
from bs4 import BeautifulSoup


source = requests.get("https://www.amazon.in/smartphones-basic-mobiles/b/ref=dp_bc_3?ie=UTF8&node=1389432031")
soup = BeautifulSoup(source.content, 'html.parser')

#print(soup.prettify())

price = soup.find('span', {'class' : 'a-size-base a-color-price acs_product-price__buying'})
name = soup.find('span', {'class' : 'a-size-small'})
print(name.text,' ',price.text)


product = soup.find(class_="a-box-group a-spacing-top-micro acs_product-title")
product_tags = product.select(".a-link-normal .a-size-small")
#price_tags = product.select(".a-size-base a-color-price acs_product-price__buying")

products = [pt.get_text() for pt in product_tags]
#prices = [pc.get_text() for pc in price_tags]

#print(products)
#print(prices)

#sample git change

