#!/usr/bin/env python3

import sys
import argparse

import shopping_basket.basket_pricer as bp
import shopping_basket.helpers as helpers


def parse_args():
    """Parses all parameters"""
    parser = argparse.ArgumentParser(description="Shopping_basket")

    parser.add_argument(
        "--basket-filename",
        dest="basket",
        help="Location of the basket file in the project",
        default=None,
        type=str,
    )

    parser.add_argument(
        "--catalogue-filename",
        dest="catalogue",
        help="Location of the catalogue file in the project",
        default=None,
        type=str,
    )

    parser.add_argument(
        "--offers-filename",
        dest="offers",
        help="Location of the offers file in the project",
        default=None,
        type=str,
    )

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()

    BASKET = args.basket
    CATALOGUE = args.catalogue
    OFFERS = args.offers

    if BASKET is None or CATALOGUE is None or OFFERS is None:
        print("Error: All file locations must be provided.")
        sys.exit(1)

    bp = bp.BasketPricer()

    print("\nLoading files...")
    DICT_BASKET = helpers.basket_textfile_to_dict(BASKET)
    DICT_CATALOGUE = helpers.cat_textfile_to_dict(CATALOGUE)
    DICT_OFFERS = helpers.offers_textfile_to_dict(OFFERS)

    print("\n***************************************")
    print("Calculating totals")
    bp.calculate_total(DICT_BASKET, DICT_CATALOGUE, DICT_OFFERS)

    print("***************************************\n")
    bp.print_totals()
    sys.exit(1)