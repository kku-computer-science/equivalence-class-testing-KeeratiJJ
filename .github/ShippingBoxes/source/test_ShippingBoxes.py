import pytest
from ShippingBoxes import ShippingBoxes

@pytest.mark.parametrize("small_size, medium_size, large_size, expected", [
    (0, 0, 0, [0, 0, 0]),
    (0, 0, 1, [1, 0, 0]),
    (0, 1, 0, [0, 0, 1]),
    (3, 2, 1, [1, 0, 3]),  
    (7, 3, 1, [1, 1, 2]),  
])
def test_valid_cases(small_size, medium_size, large_size, expected):
    shipping_boxes = ShippingBoxes()
    result = shipping_boxes.calculate(small_size, medium_size, large_size)
    assert result == expected
    print(f"Test case with small_size={small_size}, medium_size={medium_size}, large_size={large_size}: Passed")

@pytest.mark.parametrize("small_size, medium_size, large_size, expected", [
    (-1, 0, 0, [-1]),
    (0, -5, 0, [-1]),
    (0, 0, 2, [-1]),
    (1, 5, 2, [-1]),
])
def test_invalid_cases(small_size, medium_size, large_size, expected):
    shipping_boxes = ShippingBoxes()
    result = shipping_boxes.calculate(small_size, medium_size, large_size)
    assert result == expected
    print(f"Test case with small_size={small_size}, medium_size={medium_size}, large_size={large_size}: Passed")

if __name__ == "__main__":
    pytest.main()
