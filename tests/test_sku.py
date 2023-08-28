from src.tf2_sku import to_sku, from_sku

from unittest import TestCase


MANN_CO_KEY = {
    "defindex": 5021,
    "quality": 6,
    "effect": -1,
    "australium": False,
    "craftable": True,
    "wear": -1,
    "skin": -1,
    "strange": -1,
    "killstreak_tier": -1,
    "target_defindex": -1,
    "festivized": False,
    "craft_number": -1,
    "crate_number": -1,
    "output_defindex": -1,
    "output_quality": -1,
    "paint": -1,
}


class TestSKU(TestCase):
    def test_key(self):
        sku = "5021;6"
        item = {"defindex": 5021, "quality": 6}
        result = to_sku(item)

        item_dict = from_sku(sku)

        skued = to_sku(MANN_CO_KEY)

        self.assertEqual(result, sku)
        self.assertEqual(item_dict, MANN_CO_KEY)
        self.assertEqual(sku, skued)

    def test_from_sku(self):
        sku = "5021;6"
        item = from_sku(sku)

        self.assertEqual(item, MANN_CO_KEY)

    def test_ellis_cap_double(self):
        item = {"defindex": 236, "quality": 6}
        sku = to_sku(item)

        item_again = from_sku(sku)
        sku_again = to_sku(item_again)

        self.assertEqual(sku, sku_again)

    def test_skin(self):
        original = "199;5;u702;w3;pk292;strange;kt-3"
        item = from_sku(original)
        sku = to_sku(item)

        self.assertEqual(sku, original)

    def test_types(self):
        item_dict = from_sku("5021;6")
        sku = to_sku(item_dict)

        self.assertTrue(isinstance(item_dict, dict))
        self.assertTrue(isinstance(sku, str))
