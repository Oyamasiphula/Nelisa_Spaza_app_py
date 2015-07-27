import csv

def groupedProducts():
    f = open('sales.csv')
    csv_f = csv.reader(f)
    products = {}
    for row in csv_f:
        productName = row[2]
        soldItems = row[3]
        if products.has_key(productName) == False:
            products[productName] = 0
        products[productName] += int(soldItems)
    return products

def mostPopularProduct(products):
    my_max_val = 0
    for product,amount in products.items():
        if amount > my_max_val:
            # print "%s - %s" % (product, amount)
            my_max_val=amount
            my_max_key=product
            mostPopular = {
            'mostPopular' : my_max_key,
            'qty' : my_max_val
            }
    return mostPopular


def leastPopularProduct(products):
    min_value = 172
    for product,amount in products.items():
        if amount < min_value:
            min_value = amount
            product_name = product
            leastPopular = {
            'leastPopular' : product_name,
            'qty' : min_value
            }
    return leastPopular