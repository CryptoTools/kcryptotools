import unittest
from crypto_qty import *

class TestCryptoQty(unittest.TestCase):
    def setUp(self):
        pass

    def test_basic(self):

        self.assertEqual(100000000,getBaseUnitsPerNominal('BTC'))
        self.assertEqual(100000000,getBaseUnitsPerNominal('LTC'))
        self.assertEqual(100000000,getBaseUnitsPerNominal('DOGE'))
        self.assertEqual(100000000,getBaseUnitsPerNominal('btc'))
        self.assertEqual(100000000,getBaseUnitsPerNominal('ltc'))
        self.assertEqual(100000000,getBaseUnitsPerNominal('doge'))

        # test string to qty function 
        self.assertEqual(1010500000000, convertStringToQty('10105','BTC'))
        self.assertEqual(5099990000,    convertStringToQty('50.9999','BTC'))
        self.assertEqual(230000000,     convertStringToQty('2.3','BTC'))
        self.assertEqual(200000000,     convertStringToQty('2','BTC'))
        self.assertEqual(200000000,     convertStringToQty('2.0','BTC'))
        self.assertEqual(30000000,      convertStringToQty('0.3','BTC'))
        self.assertEqual(50000000,      convertStringToQty('.5','BTC'))
        self.assertEqual(202000,        convertStringToQty('.00202','BTC'))
        self.assertEqual(10009000000,   convertStringToQty('100.09','BTC'))
        self.assertEqual(1,             convertStringToQty('.00000001','BTC'))
        self.assertEqual(211,           convertStringToQty('.00000211','BTC'))
        self.assertEqual(200211,        convertStringToQty('.00200211','BTC'))
        self.assertEqual(200211,        convertStringToQty('0.00200211','BTC'))
        self.assertEqual(200000,        convertStringToQty('0.00200','BTC'))
        
        with self.assertRaises(Exception):
            convertStringToQty('ade','BTC')
        with self.assertRaises(Exception):
            convertStringToQty('0.0.1','BTC')
        with self.assertRaises(Exception):
            convertStringToQty('0.000000001','BTC')
            
        #test qty to string function
        self.assertEqual('0.8',         convertQtyToString(80000000,'BTC'))
        self.assertEqual('1',           convertQtyToString(100000000,'BTC'))
        self.assertEqual('10',          convertQtyToString(1000000000,'BTC'))
        self.assertEqual('100',         convertQtyToString(10000000000,'BTC'))
        self.assertEqual('100.01',      convertQtyToString(10001000000,'BTC'))
        self.assertEqual('445.32',      convertQtyToString(44532000000,'BTC'))
        self.assertEqual('100.101',     convertQtyToString(10010100000,'BTC'))
        self.assertEqual('1.3',         convertQtyToString(130000000,'BTC'))
        self.assertEqual('0.75',        convertQtyToString(75000000,'BTC'))
        self.assertEqual('0.001',       convertQtyToString(100000,'BTC'))
        self.assertEqual('0.00000001',  convertQtyToString(1,'BTC'))
        self.assertEqual('1.00000001',  convertQtyToString(100000001,'BTC'))


if __name__ == '__main__':

    unittest.main()
