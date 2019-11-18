from shopping_basket import helpers


class BasketPricer:
    """
    A class used to represent the totals from the basket pricer

    ...

    Attributes
    ----------
    subtotal : float
        a floating point number to represent the subtotal of the
        basket
    discount : float
        a floating point number to represent the discounts applied
        to the basket
    total : float
        a floating point number to represent the total value of
        the basket after discounts

    Methods
    -------
    calculate_subtotal(basket, catalogue)
        calculates the subtotal
    calculate_discount(basket, catalogue, offers)
        calculates the discounts
    calculate_total(basket, catalogue, offers)
        calculates the subtotals, the discounts and the total value
    print_totals()
        prints the totals of the calculations
    """

    def __init__(self):
        self.subtotal = 0.0
        self.discount = 0.0
        self.total = 0.0

    def calculate_subtotal(self, basket, catalogue):
        """Calculates the subtotal value

        Parameters
        ----------
        basket : dict
            Dictionary containing (product:quantity)
        catalogue : dict
            Dictionary containing (product:price)

        Raises
        ------
        NotImplementedError
            If the basket or Catalogue is not loaded.
        """
        subtotal = 0.0
        if (
            not isinstance(basket, dict)
            or not isinstance(catalogue, dict)
            or len(catalogue) == 0
        ):
            raise NotImplementedError("Catalogue and basket must be loaded.")

        if len(basket) == 0:
            self.subtotal = 0.0
            return


        for p, q in basket.items():
            if p in catalogue:
                subtotal += catalogue[p] * q
        self.subtotal = helpers.roundup(subtotal)

    def calculate_discount(self, basket, catalogue, offers):
        """Calculates the discount value

        Parameters
        ----------
        basket : dict
            Dictionary containing (product:quantity)
        catalogue : dict
            Dictionary containing (product:price)
        offers : dict
            Dictionary containing (product:[descriptors])

        Raises
        ------
        NotImplementedError
            If the Basket, Catalogue or Offers is not loaded.
        """

        discount = 0.0
        if (
            not isinstance(basket, dict)
            or not isinstance(catalogue, dict)
            or len(catalogue) == 0
            or not isinstance(offers, dict)
            or len(offers) == 0
        ):
            raise NotImplementedError("Catalog, basket and offers must be loaded.")

        if len(basket) == 0:
            self.discount = 0.0
            return

        for p, q in basket.items():
            if p in offers or p.split(" ")[0] in offers:
                offer = offers[p]

                if "discount" in offer:
                    # if [N, 'discount']
                    percentage = int(offer[0]) / 100
                    if p in catalogue:
                        discount += percentage * (catalogue[p] * q)

                # TODO: Future implementation of "cheapest"
                # if "cheapest" in offer:
                #     # ['cheapest', N]
                #     to_buy = int(offer[1])

                if "buy" in offer:
                    # ['buy', N, 'get', n, 'free']
                    to_buy = int(offer[1])
                    to_get = int(offer[3])
                    for_free = q // (to_buy + to_get) # Obtain quotient
                    if p in catalogue:
                        discount += catalogue[p] * for_free

        self.discount = helpers.roundup(discount)

    def calculate_total(self, basket, catalogue, offers):
        """Calculates the total value

        Parameters
        ----------
        basket : dict
            Dictionary containing (product:quantity)
        catalogue : dict
            Dictionary containing (product:price)
        offers : dict
            Dictionary containing (product:[descriptors])
        """

        self.calculate_subtotal(basket, catalogue)
        self.calculate_discount(basket, catalogue, offers)
        total = self.subtotal - self.discount

        # Adjust
        self.total = helpers.roundup(total) if total >= 0.0 else 0.0

    def print_totals(self):
        """Prints the values of all calculations"""

        print(u"Subtotal: \xA3%.2f" % self.subtotal)
        print(u"Discount: \xA3%.2f" % self.discount)
        print(u"Total: \xA3%.2f" % self.total)
