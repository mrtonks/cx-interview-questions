#!/usr/bin/env python3

import sys, argparse

import shopping_basket.basket_pricer as bp
import shopping_basket.helpers as helpers


def parse_args():
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

    basket = args.basket
    catalogue = args.catalogue
    offers = args.offers

    if basket is None or catalogue is None or offers is None:
        print("Error: All file locations must be provided.")
        sys.exit(1)

    bp = bp.BasketPricer()

    print("\nLoading files...")
    dict_basket = helpers.basket_textfile_to_dict(basket)
    dict_catalogue = helpers.cat_textfile_to_dict(catalogue)
    dict_offers = helpers.offers_textfile_to_dict(offers)

    print("\n***************************************")
    print("Calculating totals")
    bp.calculate_total(dict_basket, dict_catalogue, dict_offers)

    print("***************************************\n")
    bp.print_totals()
