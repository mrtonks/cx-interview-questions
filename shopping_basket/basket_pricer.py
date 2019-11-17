"""
Class for Basket-Pricer
"""
import io
import os
import math


class BasketPricer:
    """
    Class
    """

    def __init__(self):
        self.subtotal = 0.0
        self.discount = 0.0
        self.total = 0.0
        self.basket = None
        self.catalogue = None
        self.offers = None

    def calculate_subtotal(self):
        subtotal = 0.0
        if self.basket is None or self.catalogue is None:
            return "Basket or Catalogue is not loaded."

        for p, q in self.basket.items():
            if p in self.catalogue:
                subtotal += self.catalogue[p] * q
        self.subtotal = roundup(subtotal)

    def calculate_discount(self):
        discount = 0.0
        if self.basket is None or self.offers is None:
            return "Basket or Offers is not loaded."

        for p, q in self.basket.items():
            if p in self.offers or p.split(" ")[0] in self.offers:
                offer = self.offers[p]

                if "discount" in offer:
                    # if [N, 'discount']
                    percentage = int(offer[0]) / 100
                    if p in self.catalogue:
                        discount += percentage * (self.catalogue[p] * q)
                        
                if "cheapest" in offer:
                    # ['cheapest', N]
                    to_buy = int(offer[1])

                if "buy" in offer:
                    # ['buy', N, 'get', n, 'free']
                    to_buy = int(offer[1])
                    to_get = int(offer[3])
                    for_free = q // (to_buy + to_get)
                    if p in self.catalogue:
                        discount += self.catalogue[p] * for_free
                
        self.discount = roundup(discount)

    def calculate_total(self):
        self.calculate_subtotal()
        self.calculate_discount()
        total = self.subtotal - self.discount

        # Adjust
        self.total = roundup(total) if total >= 0.0 else 0.0

    def print_results(self):
        print("Subtotal: £%.2f" % self.subtotal)
        print("Discount: £%.2f" % self.discount)
        print("Total: £%.2f" % self.total)

    def start_pricer(
        self, filename_basket=None, filename_offers=None, filename_catalogue=None
    ):
        print("Loading text files...")
        self.basket_textfile_to_dict(filename_basket)
        self.offers_textfile_to_dict(filename_offers)
        self.cat_textfile_to_dict(filename_catalogue)
        print("Doing calculations...")
        self.calculate_total()
        self.print_results()

    def cat_textfile_to_dict(self, filename, prod_decorator="**"):
        catalogue = {}
        filedir = os.path.dirname(os.path.realpath("__file__"))
        filepath = os.path.join(filedir, filename)
        if not os.path.isfile(filepath):
            return "Error: {} not a valid filename".format(filename)

        with open(filepath, "r") as f:
            for line in f:
                arr = line.strip().split(prod_decorator + " ")
                catalogue[arr[0].replace("*", "")] = float(arr[1].replace("£", ""))

        self.catalogue = catalogue
        print("Catalogue file loaded.")

    def offers_textfile_to_dict(self, filename, prod_decorator="***"):
        offers = {}
        filedir = os.path.dirname(os.path.realpath("__file__"))
        filepath = os.path.join(filedir, filename)
        if not os.path.isfile(filepath):
            return "Error: {} not a valid filename".format(filename)

        with open(filepath, "r") as f:
            for line in f:
                if prod_decorator in line:
                    arr = line.strip().split(prod_decorator + ": ")
                    offers[arr[0].replace("*", "")] = (
                        arr[1].replace("%", "").replace(",", "").split(" ")
                    )
                elif "cheapest" in line:
                    arr = line.split(",")
                    arr_subset = arr[0].split("of")
                    # Get {X}: N
                    offers[arr_subset[1].strip()] = [
                        "cheapest",
                        int(arr_subset[0].split(" ")[1].strip()),
                    ]

        self.offers = offers
        print("Offers file loaded.")

    def basket_textfile_to_dict(self, filename, basket_decorator="x"):
        basket = {}
        filedir = os.path.dirname(os.path.realpath("__file__"))
        filepath = os.path.join(filedir, filename)
        if not os.path.isfile(filepath):
            return "Error: {} not a valid filename".format(filename)

        with open(filepath, "r") as f:
            for line in f:
                arr = line.strip().split(basket_decorator)
                basket[arr[0].strip()] = int(arr[1])

        self.basket = basket
        print("Basket file loaded.")


def roundup(x):
    return math.ceil(x * 100) / 100
