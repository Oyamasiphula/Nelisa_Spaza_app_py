
import products
#from products import groupedProducts

#print dir(products)

productMap = products.groupedProducts()

print products.mostPopularProduct(productMap)
print products.leastPopularProduct(productMap)