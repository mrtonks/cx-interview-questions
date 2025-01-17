import unittest

from shopping_basket import basket_pricer
from shopping_basket import helpers


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
        filepath = "shopping_basket/data/catalogue_test.txt"
        catalog = {"Baked Beans": 0.99, "Biscuits": 1.20, "Sardines": 1.89}

        dict_cat = helpers.cat_textfile_to_dict(filepath)

        self.assertEqual(
            dict_cat, catalog, "The catalog is not correct.",
        )

    def test_get_incorrect_filename_catalog_from_textfile(self):
        filepath = "catalogue.txt"

        with self.assertRaises(FileNotFoundError):
            helpers.cat_textfile_to_dict(filepath)

    def test_get_offers_from_textfile(self):
        filepath = "shopping_basket/data/offers_test.txt"
        offers = {
            "Baked Beans": ["buy", "2", "get", "1", "free"],
            "Sardines": ["25", "discount"]
        }

        dict_offers = helpers.offers_textfile_to_dict(filepath)

        self.assertEqual(
            dict_offers, offers, "The offers are not correct.",
        )

    def test_get_basket_from_textfile(self):
        filepath = "shopping_basket/data/basket_test_1.txt"
        basket = {"Baked Beans": 4, "Biscuits": 1}

        dict_basket = helpers.basket_textfile_to_dict(filepath)

        self.assertEqual(
            dict_basket, basket, "The basket is not correct.",
        )

    def test_get_subtotal_error_with_catalogue_empty(self):
        test_pricer = basket_pricer.BasketPricer()

        filepath_basket = "shopping_basket/data/basket_test_1.txt"

        dict_basket = helpers.basket_textfile_to_dict(filepath_basket)
        dict_catalog = {}

        with self.assertRaises(NotImplementedError):
            test_pricer.calculate_subtotal(dict_basket, dict_catalog)

    def test_get_subtotal_zero_with_empty_basket(self):
        test_pricer = basket_pricer.BasketPricer()

        filepath_catalogue = "shopping_basket/data/catalogue_test.txt"

        dict_basket = {}
        dict_catalogue = helpers.cat_textfile_to_dict(filepath_catalogue)

        test_pricer.calculate_subtotal(dict_basket, dict_catalogue)

        self.assertEqual(test_pricer.subtotal, 0.0, "The subtotal is not zero.")

    def test_get_subtotal_with_basket_1(self):
        test_pricer = basket_pricer.BasketPricer()

        filepath_basket = "shopping_basket/data/basket_test_1.txt"
        filepath_catalogue = "shopping_basket/data/catalogue_test.txt"

        dict_basket = helpers.basket_textfile_to_dict(filepath_basket)
        dict_catalogue = helpers.cat_textfile_to_dict(filepath_catalogue)

        subtotal = 5.16

        test_pricer.calculate_subtotal(dict_basket, dict_catalogue)

        self.assertEqual(test_pricer.subtotal, subtotal, "The subtotal is incorrect.")

    def test_get_discount_zero_with_empty_basket(self):
        test_pricer = basket_pricer.BasketPricer()

        filepath_catalogue = "shopping_basket/data/catalogue_test.txt"
        filepath_offers = "shopping_basket/data/offers_test.txt"

        dict_basket = {}
        dict_catalogue = helpers.cat_textfile_to_dict(filepath_catalogue)
        dict_offers = helpers.offers_textfile_to_dict(filepath_offers)

        test_pricer.calculate_discount(dict_basket, dict_catalogue, dict_offers)

        self.assertEqual(test_pricer.discount, 0.0, "The discount is incorrect.")

    def test_get_discount_error_with_empty_catalogue(self):
        test_pricer = basket_pricer.BasketPricer()

        filepath_basket = "shopping_basket/data/basket_test_1.txt"
        filepath_offers = "shopping_basket/data/offers_test.txt"

        dict_basket = helpers.basket_textfile_to_dict(filepath_basket)
        dict_catalogue = {}
        dict_offers = helpers.offers_textfile_to_dict(filepath_offers)

        with self.assertRaises(NotImplementedError):
            test_pricer.calculate_discount(dict_basket, dict_catalogue, dict_offers)

    def test_get_discount_with_basket_1(self):
        test_pricer = basket_pricer.BasketPricer()

        filepath_basket = "shopping_basket/data/basket_test_1.txt"
        filepath_catalogue = "shopping_basket/data/catalogue_test.txt"
        filepath_offers = "shopping_basket/data/offers_test.txt"

        dict_basket = helpers.basket_textfile_to_dict(filepath_basket)
        dict_catalogue = helpers.cat_textfile_to_dict(filepath_catalogue)
        dict_offers = helpers.offers_textfile_to_dict(filepath_offers)

        discount = 0.99

        test_pricer.calculate_discount(dict_basket, dict_catalogue, dict_offers)

        self.assertEqual(test_pricer.discount, discount, "The discount is incorrect.")

    def test_get_discount_with_basket_2(self):
        test_pricer = basket_pricer.BasketPricer()

        filepath_basket = "shopping_basket/data/basket_test_2.txt"
        filepath_catalogue = "shopping_basket/data/catalogue_test.txt"
        filepath_offers = "shopping_basket/data/offers_test.txt"

        dict_basket = helpers.basket_textfile_to_dict(filepath_basket)
        dict_catalogue = helpers.cat_textfile_to_dict(filepath_catalogue)
        dict_offers = helpers.offers_textfile_to_dict(filepath_offers)

        discount = 0.95

        test_pricer.calculate_discount(dict_basket, dict_catalogue, dict_offers)

        self.assertEqual(test_pricer.discount, discount, "The discount is incorrect.")

    def test_get_all_totals_basket_1(self):
        test_pricer = basket_pricer.BasketPricer()

        filepath_basket = "shopping_basket/data/basket_test_1.txt"
        filepath_catalogue = "shopping_basket/data/catalogue_full.txt"
        filepath_offers = "shopping_basket/data/offers_test.txt"

        dict_basket = helpers.basket_textfile_to_dict(filepath_basket)
        dict_catalogue = helpers.cat_textfile_to_dict(filepath_catalogue)
        dict_offers = helpers.offers_textfile_to_dict(filepath_offers)

        subtotal = 5.16
        discount = 0.99
        total = 4.17

        test_pricer.calculate_total(dict_basket, dict_catalogue, dict_offers)

        self.assertEqual(test_pricer.subtotal, subtotal, "The subtotal is incorrect.")
        self.assertEqual(test_pricer.discount, discount, "The discount is incorrect.")
        self.assertEqual(test_pricer.total, total, "The total is incorrect.")

    def test_get_all_totals_basket_2(self):
        test_pricer = basket_pricer.BasketPricer()

        filepath_basket = "shopping_basket/data/basket_test_2.txt"
        filepath_catalogue = "shopping_basket/data/catalogue_full.txt"
        filepath_offers = "shopping_basket/data/offers_test.txt"

        dict_basket = helpers.basket_textfile_to_dict(filepath_basket)
        dict_catalogue = helpers.cat_textfile_to_dict(filepath_catalogue)
        dict_offers = helpers.offers_textfile_to_dict(filepath_offers)

        subtotal = 6.96
        discount = 0.95
        total = 6.01

        test_pricer.calculate_total(dict_basket, dict_catalogue, dict_offers)

        self.assertEqual(test_pricer.subtotal, subtotal, "The subtotal is incorrect.")
        self.assertEqual(test_pricer.discount, discount, "The discount is incorrect.")
        self.assertEqual(test_pricer.total, total, "The total is incorrect.")

    def test_get_all_totals_basket_3(self):
        test_pricer = basket_pricer.BasketPricer()

        filepath_basket = "shopping_basket/data/basket_test_3.txt"
        filepath_catalogue = "shopping_basket/data/catalogue_full.txt"
        filepath_offers = "shopping_basket/data/offers_test.txt"

        dict_basket = helpers.basket_textfile_to_dict(filepath_basket)
        dict_catalogue = helpers.cat_textfile_to_dict(filepath_catalogue)
        dict_offers = helpers.offers_textfile_to_dict(filepath_offers)

        subtotal = 15.92
        discount = 2.93
        total = 12.99

        test_pricer.calculate_total(dict_basket, dict_catalogue, dict_offers)

        self.assertEqual(test_pricer.subtotal, subtotal, "The subtotal is incorrect.")
        self.assertEqual(test_pricer.discount, discount, "The discount is incorrect.")
        self.assertEqual(test_pricer.total, total, "The total is incorrect.")

    def test_get_all_totals_zero_with_empty_basket(self):
        test_pricer = basket_pricer.BasketPricer()

        filepath_catalogue = "shopping_basket/data/catalogue_full.txt"
        filepath_offers = "shopping_basket/data/offers_test.txt"

        dict_basket = {}
        dict_catalogue = helpers.cat_textfile_to_dict(filepath_catalogue)
        dict_offers = helpers.offers_textfile_to_dict(filepath_offers)

        test_pricer.calculate_total(dict_basket, dict_catalogue, dict_offers)

        self.assertEqual(test_pricer.subtotal, 0.0, "The subtotal is incorrect.")
        self.assertEqual(test_pricer.discount, 0.0, "The discount is incorrect.")
        self.assertEqual(test_pricer.total, 0.0, "The total is incorrect.")

    def test_get_all_totals_error_with_empty_catalogue(self):
        test_pricer = basket_pricer.BasketPricer()

        filepath_basket = "shopping_basket/data/basket_test_1.txt"
        filepath_offers = "shopping_basket/data/offers_test.txt"

        dict_basket = helpers.basket_textfile_to_dict(filepath_basket)
        dict_catalogue = {}
        dict_offers = helpers.offers_textfile_to_dict(filepath_offers)

        with self.assertRaises(NotImplementedError):
            test_pricer.calculate_total(dict_basket, dict_catalogue, dict_offers)

    def test_get_all_totals_error__with_empty_offers(self):
        test_pricer = basket_pricer.BasketPricer()

        filepath_basket = "shopping_basket/data/basket_test_1.txt"
        filepath_catalogue = "shopping_basket/data/catalogue_full.txt"

        dict_basket = helpers.basket_textfile_to_dict(filepath_basket)
        dict_catalogue = helpers.cat_textfile_to_dict(filepath_catalogue)
        dict_offers = {}

        with self.assertRaises(NotImplementedError):
            test_pricer.calculate_total(dict_basket, dict_catalogue, dict_offers)


if __name__ == "__main__":
    unittest.main()
