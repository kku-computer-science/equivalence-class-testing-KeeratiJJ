import unittest
from ShippingBoxes import ShippingBoxes

def calculate_boxes(truck_capacity, large_boxes, medium_boxes, small_boxes):
    large_weight = 10
    medium_weight = 5
    small_weight = 1

    total_large_weight = large_boxes * large_weight
    total_medium_weight = medium_boxes * medium_weight
    total_small_weight = small_boxes * small_weight

    if total_large_weight <= truck_capacity:
        truck_capacity -= total_large_weight
    else:
        return -1

    if total_medium_weight <= truck_capacity:
        truck_capacity -= total_medium_weight
    else:
        return -1

    if total_small_weight <= truck_capacity:
        truck_capacity -= total_small_weight
    else:
        return -1

    return (large_boxes, medium_boxes, small_boxes)

class TestCalculateBoxes(unittest.TestCase):

    def test_1(self):
        self.assertEqual(calculate_boxes(100, 5, 5, 5), (5, 5, 5))

    def test_2(self):
        self.assertEqual(calculate_boxes(10, 2, 2, 2), -1)

if __name__ == '__main__':
    unittest.main()