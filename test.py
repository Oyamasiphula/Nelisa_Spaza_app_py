import products
import unittest
productMap = products.groupedProducts()
mostPopularPdt = products.mostPopularProduct(productMap)
leastPopularPdt = products.leastPopularProduct(productMap)

class MyTest(unittest.TestCase):
    def test_mostPopularProduct(self):
    	print mostPopularPdt
        self.assertEqual('Mixed Sweets 5s', mostPopularPdt['mostPopular'])
        self.assertEqual(172, mostPopularPdt['qty'])

    def test_leastPopularProduct(self):
    	print leastPopularPdt
    	self.assertEqual('Valentine Cards', leastPopularPdt['leastPopular'])
        self.assertEqual(14, leastPopularPdt['qty'])

if __name__ == '__main__':
    unittest.main()