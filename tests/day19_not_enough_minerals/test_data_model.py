import unittest
from src.day19_not_enough_minerals.data_model import Inventory, Blueprint


class TestDay19DataModel(unittest.TestCase):
    def test_incorrect_buy_robot_type(self):
        blueprint = Blueprint(1, 2, 3, 1, 4, 2, 3)
        inventory = Inventory()
        self.assertRaises(TypeError, lambda i, t: i.buy_robot(t, blueprint), inventory, "Invalid")


if __name__ == '__main__':
    unittest.main()
