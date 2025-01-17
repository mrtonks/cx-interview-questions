"""Helper file for Basket Pricer

This script allows the user to load the different textfiles containing
the information necessary to procees with the calculations in the Basket
Pricer script. Also, a helper function for rounding up is included.

This tool accepts only text files (.txt). And the format required for these
depend on the requirements set.

Examples of formats:
Catalogue
Baked Beans: £0.99

Offers
Baked Beans: buy 2 get 1 free
Sardines: 25% discount

Basket
Baked Beans x 4

This file can also be imported as a module and contains
the following
functions:
    * cat_textfile_to_dict - returns the catalogue dictionary
    * offers_textfile_to_dict - returns the offers dictionary
    * basket_textfile_to_dict - returns the basket dictionary
    * roundup - returns a rounded up floating point value
"""

import os
import math


def cat_textfile_to_dict(filename, prod_separator=":"):
    """Converts text file into the catalogue dictionary

    Parameters
    ----------
    filename : str
        The name and location of the of the text file inside the project
    prod_separator : str, optional
        Enclose the product name (default is ":")

    Returns
    -------
    dictionary
        A dictionary of products with product name as key and
        price as value
    """

    catalogue = {}
    filedir = os.path.dirname(os.path.realpath("__file__"))
    filepath = os.path.join(filedir, filename)
    if not os.path.isfile(filepath):
        raise FileNotFoundError("Catalogue file not found.")

    with open(filepath, "r") as f:
        for line in f:
            arr = line.strip().split(prod_separator)
            product = arr[0].strip()
            price = float(arr[1].strip().replace("£", ""))

            if price < 0:
                raise NotImplementedError(
                    "Product {} price is negative".format(product)
                )

            catalogue[product] = price

    print("Catalogue file loaded.")
    return dict(catalogue)


def offers_textfile_to_dict(filename, prod_separator=":"):
    """Converts text file into the offers dictionary

    Parameters
    ----------
    filename : str
        The name and location of the of the text file inside the project
    prod_separator : str, optional
        Enclose the product name (default is ":")

    Returns
    -------
    dictionary
        A dictionary of offers with product name as key and
        offer descriptors in an array as value
    """

    offers = {}
    filedir = os.path.dirname(os.path.realpath("__file__"))
    filepath = os.path.join(filedir, filename)
    if not os.path.isfile(filepath):
        raise FileNotFoundError("Offers file not found.")

    with open(filepath, "r") as f:
        for line in f:
            arr = line.strip().split(prod_separator)
            product = arr[0].strip()
            offer = arr[1].strip().replace("%", "").replace(",", "").split(" ")
            offers[product] = offer

            # TODO: future implementation of "cheapest"
            # elif "cheapest" in line:
            #     arr = line.split(",")
            #     arr_subset = arr[0].split("of")
            #     # Get {X}: N
            #     offers[arr_subset[1].strip()] = [
            #         "cheapest",
            #         int(arr_subset[0].split(" ")[1].strip()),
            #     ]

    print("Offers file loaded.")
    return dict(offers)


def basket_textfile_to_dict(filename, prod_separator="x"):
    """Converts text file into the basket dictionary

    Parameters
    ----------
    filename : str
        The name and location of the of the text file inside the project
    prod_separator : str, optional
        Enclose the product name (default is "x")

    Returns
    -------
    dictionary
        A dictionary of products with product name as key and
        number of products to buy as value
    """

    basket = {}
    filedir = os.path.dirname(os.path.realpath("__file__"))
    filepath = os.path.join(filedir, filename)

    if not os.path.isfile(filepath):
        raise FileNotFoundError("Basket file not found.")

    with open(filepath, "r") as f:
        for line in f:
            arr = line.strip().split(prod_separator)
            product = arr[0].strip()
            quantity = int(arr[1])

            if quantity < 0:
                raise NotImplementedError("Product {} cannot be negative".format(product))
            basket[product] = quantity

    print("Basket file loaded.")
    return dict(basket)


def roundup(x):
    """Rounds up a floating point number"""
    return math.ceil(x * 100) / 100
