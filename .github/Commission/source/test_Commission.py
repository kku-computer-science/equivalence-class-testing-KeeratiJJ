import unittest
from Commission import Commission

class TestCommissionCalculation(unittest.TestCase):

    def setUp(self):
        self.comm = Commission()

#===============================================================================================

    def test_sales1(self):
        self.assertEqual(self.comm.check_commission(10, 10, 10), 16500)

    def test_sales2(self):
        self.assertEqual(self.comm.check_commission(10, 10, -1), -1)
    
    def test_sales3(self):
        self.assertEqual(self.comm.check_commission(10, 10, 91), "out of stock")

    def test_sales4(self):
        self.assertEqual(self.comm.check_commission(10, -1, 10), -1)

    def test_sales5(self):
        self.assertEqual(self.comm.check_commission(10, -1, -1), -1)

    def test_sales6(self):
        self.assertEqual(self.comm.check_commission(10, -1, 91), -1)

    def test_sales7(self):
        self.assertEqual(self.comm.check_commission(10, 81, 10), "out of stock")

    def test_sales8(self):
        self.assertEqual(self.comm.check_commission(10, 81, -1), -1)

    def test_sales9(self):
        self.assertEqual(self.comm.check_commission(10, 81, 91), "out of stock")


    def test_sales10(self):
        self.assertEqual(self.comm.check_commission(0, 10, 10), 10500)

    def test_sales11(self):
        self.assertEqual(self.comm.check_commission(0, 10, -1), -1)

    def test_sales12(self):
        self.assertEqual(self.comm.check_commission(0, 10, 91), "out of stock")

    def test_sales13(self):
        self.assertEqual(self.comm.check_commission(0, -1, 10), -1)

    def test_sales14(self):
        self.assertEqual(self.comm.check_commission(0, -1, -1), -1)

    def test_sales15(self):
        self.assertEqual(self.comm.check_commission(0, -1, 91), -1)

    def test_sales16(self):
        self.assertEqual(self.comm.check_commission(0, 81, 10), "out of stock")

    def test_sales17(self):
        self.assertEqual(self.comm.check_commission(0, 81, -1), -1)

    def test_sales18(self):
        self.assertEqual(self.comm.check_commission(0, 81, 91), "out of stock")


    def test_sales19(self):
        self.assertEqual(self.comm.check_commission(71, 10, 10), "out of stock")

    def test_sales20(self):
        self.assertEqual(self.comm.check_commission(71, 10, -1), -1)

    def test_sales21(self):
        self.assertEqual(self.comm.check_commission(71, 10, 91), "out of stock")

    def test_sales22(self):
        self.assertEqual(self.comm.check_commission(71, -1, 10), -1)

    def test_sales23(self):
        self.assertEqual(self.comm.check_commission(71, -1, -1), -1)

    def test_sales24(self):
        self.assertEqual(self.comm.check_commission(71, -1, 91), -1)

    def test_sales25(self):
        self.assertEqual(self.comm.check_commission(71, 81, 10), "out of stock")

    def test_sales26(self):
        self.assertEqual(self.comm.check_commission(71, 81, -1), -1)

    def test_sales27(self):
        self.assertEqual(self.comm.check_commission(71, 81, 91), "out of stock")

#===============================================================================================

if __name__ == '__main__':
    unittest.main()
