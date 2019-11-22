import unittest
from modules.sign_gen import sign_gen

class TestSum(unittest.TestCase):
    def test_sing_gen_eur(self):
        """
        Sign Validity Test
        """
        data = {
            'amount': '20', 
            'currency': '978',  
            'shop_id': '5', 
            'shop_order_id': '23453'
            }
        result = sign_gen(data)
        sign_true = 'aa005598ffe97a566649f1ba3bda1fc7aaf2665595bae5c6072e89e854d17340'
        self.assertEqual(result, sign_true)

    def test_sing_gen_usd(self):
        data = {
            'shop_amount': '340', 
            'shop_currency': '840',
            'payer_currency': '840',  
            'shop_id': '5', 
            'shop_order_id': '12343'
            }
        result = sign_gen(data)
        sign_true = 'a5f3b3a759704bdb5e7a4883d9314d5a19346c2648aab2e55782a75262704b0c'
        self.assertEqual(result, sign_true)

    def test_sing_gen_rub(self):
        data = {
            'amount': '40', 
            'currency': '643',
            'payway': 'payeer_rub',  
            'shop_id': '5', 
            'shop_order_id': '543'
            }
        result = sign_gen(data)
        sign_true = '3b4afd2c09f07d70c2aa89609740f4c2a8834a8817d56f08c5cd420f815a01f3'
        self.assertEqual(result, sign_true)


if __name__ == '__main__':
    unittest.main()