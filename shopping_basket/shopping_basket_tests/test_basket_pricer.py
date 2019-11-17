import unittest
from shopping_basket import basket_pricer


class TestBasketPricer(unittest.TestCase):
    """
    Tests for Basket-Pricer.
    """

    def test_is_instance_BasketPricer(self):
        test_pricer = basket_pricer.BasketPricer()
        self.assertIsInstance(
            test_pricer,
            basket_pricer.BasketPricer,
            "Object is not instance of BasketPricer class.",
        )

    def test_is_empty_basket_zeros(self):
        test_pricer = basket_pricer.BasketPricer()
        self.assertEqual(test_pricer.discount, 0.0, "Discount is not zero.")
        self.assertEqual(test_pricer.subtotal, 0.0, "Subtotal is not zero.")
        self.assertEqual(test_pricer.total, 0.0, "Total is not zero.")

    def test_get_catalog_from_textfile(self):
        test_pricer = basket_pricer.BasketPricer()
        filepath = "shopping_basket/shopping_basket_tests/catalogue_test.txt"
        catalog_dict = {"Baked Beans": 0.99, "Biscuits": 1.20, "Sardines": 1.89}

        test_pricer.cat_textfile_to_dict(filepath)

        self.assertEqual(
            test_pricer.catalogue, catalog_dict, "The catalog is not correct.",
        )

    def test_get_incorrect_filename_catalog_from_textfile(self):
        test_pricer = basket_pricer.BasketPricer()
        filepath = "catalogue.txt"

        self.assertEqual(
            test_pricer.cat_textfile_to_dict(filepath),
            "Error: {} not a valid filename".format(filepath),
            "Incorrect filename message not working.",
        )

    def test_get_offers_from_textfile(self):
        test_pricer = basket_pricer.BasketPricer()

        filepath = "shopping_basket/shopping_basket_tests/offers_test.txt"
        offers_dict = {
            "Baked Beans": ["buy", "2", "get", "1", "free"],
            "Sardines": ["25", "discount"],
            "Shampoo": ["cheapest", 3]
        }
        test_pricer.offers_textfile_to_dict(filepath)

        self.assertEqual(
            test_pricer.offers, offers_dict, "The offers are not correct.",
        )

    def test_get_subtotal_zero_with_basket_none(self):
        test_pricer = basket_pricer.BasketPricer()

        filepath_catalogue = "shopping_basket/shopping_basket_tests/catalogue_test.txt"
        filepath_offers = "shopping_basket/shopping_basket_tests/offers_test.txt"

        test_pricer.cat_textfile_to_dict(filepath_catalogue)
        test_pricer.offers_textfile_to_dict(filepath_offers)

        self.assertEqual(
            test_pricer.calculate_subtotal(),
            "Basket or Catalogue is not loaded.",
            "The error message is not correct.",
        )

    def test_get_basket_from_textfile(self):
        test_pricer = basket_pricer.BasketPricer()

        filepath = "shopping_basket/shopping_basket_tests/basket_test.txt"
        basket_dict = {"Baked Beans": 4, "Biscuits": 1}
        test_pricer.basket_textfile_to_dict(filepath)

        self.assertEqual(
            test_pricer.basket, basket_dict, "The basket is not correct.",
        )

    def test_get_subtotal_zero_with_only_catalogue_none(self):
        test_pricer = basket_pricer.BasketPricer()

        filepath_basket = "shopping_basket/shopping_basket_tests/basket_test.txt"
        filepath_offers = "shopping_basket/shopping_basket_tests/offers_test.txt"

        test_pricer.basket_textfile_to_dict(filepath_basket)
        test_pricer.offers_textfile_to_dict(filepath_offers)

        self.assertEqual(
            test_pricer.calculate_subtotal(),
            "Basket or Catalogue is not loaded.",
            "The error message is not correct.",
        )

    def test_get_subtotal_zero_with_basket_and_catalog_none(self):
        test_pricer_b = basket_pricer.BasketPricer()
        filepath_offers = "shopping_basket/shopping_basket_tests/offers_test.txt"

        test_pricer_b.offers_textfile_to_dict(filepath_offers)

        self.assertEqual(
            test_pricer_b.calculate_subtotal(),
            "Basket or Catalogue is not loaded.",
            "The error message is not correct.",
        )

    def test_get_subtotal(self):
        test_pricer = basket_pricer.BasketPricer()

        filepath_basket = "shopping_basket/shopping_basket_tests/basket_test.txt"
        filepath_catalogue = "shopping_basket/shopping_basket_tests/catalogue_test.txt"

        test_pricer.basket_textfile_to_dict(filepath_basket)
        test_pricer.cat_textfile_to_dict(filepath_catalogue)

        subtotal = 5.16

        test_pricer.calculate_subtotal()

        self.assertEqual(test_pricer.subtotal, subtotal, "The subtotal is incorrect.")

    def test_get_discount(self):
        test_pricer = basket_pricer.BasketPricer()

        filepath_basket = "shopping_basket/shopping_basket_tests/basket_test.txt"
        filepath_catalogue = "shopping_basket/shopping_basket_tests/catalogue_test.txt"
        filepath_offers = "shopping_basket/shopping_basket_tests/offers_test.txt"

        test_pricer.basket_textfile_to_dict(filepath_basket)
        test_pricer.cat_textfile_to_dict(filepath_catalogue)
        test_pricer.offers_textfile_to_dict(filepath_offers)

        discount = 0.99

        test_pricer.calculate_discount()

        self.assertEqual(test_pricer.discount, discount, "The discount is incorrect.")

    def test_get_total_basket_1(self):
        test_pricer = basket_pricer.BasketPricer()

        filepath_basket = "shopping_basket/shopping_basket_tests/basket_1.txt"
        filepath_catalogue = "shopping_basket/shopping_basket_tests/catalogue_full.txt"
        filepath_offers = "shopping_basket/shopping_basket_tests/offers_test.txt"

        test_pricer.basket_textfile_to_dict(filepath_basket)
        test_pricer.cat_textfile_to_dict(filepath_catalogue)
        test_pricer.offers_textfile_to_dict(filepath_offers)

        subtotal = 5.16
        discount = 0.99
        total = 4.17

        test_pricer.calculate_total()

        self.assertEqual(test_pricer.subtotal, subtotal, "The subtotal is incorrect.")
        self.assertEqual(test_pricer.discount, discount, "The discount is incorrect.")
        self.assertEqual(test_pricer.total, total, "The total is incorrect.")

    def test_get_total_basket_2(self):
        test_pricer = basket_pricer.BasketPricer()

        filepath_basket = "shopping_basket/shopping_basket_tests/basket_2.txt"
        filepath_catalogue = "shopping_basket/shopping_basket_tests/catalogue_full.txt"
        filepath_offers = "shopping_basket/shopping_basket_tests/offers_test.txt"

        test_pricer.basket_textfile_to_dict(filepath_basket)
        test_pricer.cat_textfile_to_dict(filepath_catalogue)
        test_pricer.offers_textfile_to_dict(filepath_offers)

        subtotal = 6.96
        discount = 0.95
        total = 6.01

        test_pricer.calculate_total()

        self.assertEqual(test_pricer.subtotal, subtotal, "The subtotal is incorrect.")
        self.assertEqual(test_pricer.discount, discount, "The discount is incorrect.")
        self.assertEqual(test_pricer.total, total, "The total is incorrect.")


if __name__ == "__main__":
    unittest.main()
