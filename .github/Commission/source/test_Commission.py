import unittest
from Commission import Commission

class TestCommissionCalculation(unittest.TestCase):

    def setUp(self):
        self.comm = Commission()

    def sales_fixture(self):
        return [
            (10, 10, 10, 16500),
            (10, 10, -1, -1),
            (10, 10, 91, "out of stock"),
            (10, -1, 10, -1),
            (10, -1, -1, -1),
            (10, -1, 91, -1),
            (10, 81, 10, "out of stock"),
            (10, 81, -1, -1),
            (10, 81, 91, "out of stock"),
            (0, 10, 10, 10500),
            (0, 10, -1, -1),
            (0, 10, 91, "out of stock"),
            (0, -1, 10, -1),
            (0, -1, -1, -1),
            (0, -1, 91, -1),
            (0, 81, 10, "out of stock"),
            (0, 81, -1, -1),
            (0, 81, 91, "out of stock"),
            (71, 10, 10, "out of stock"),
            (71, 10, -1, -1),
            (71, 10, 91, "out of stock"),
            (71, -1, 10, -1),
            (71, -1, -1, -1),
            (71, -1, 91, -1),
            (71, 81, 10, "out of stock"),
            (71, 81, -1, -1),
            (71, 81, 91, "out of stock")
        ]

    def test_commission_calculations(self):
        for num_lock, num_stock, num_barrel, expected_result in self.sales_fixture():
            with self.subTest(num_lock=num_lock, num_stock=num_stock, num_barrel=num_barrel):
                self.assertEqual(self.comm.check_commission(num_lock, num_stock, num_barrel), expected_result)

if __name__ == '__main__':
    unittest.main()
