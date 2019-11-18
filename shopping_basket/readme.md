## Documentation

This implementation uses text files to load the necessary information from the basket, catalogue and offers into the program.

### Example files format

The files must follow the same format as the examples below in order for the program to work properly.

#### Basket

* Baked Beans x 4
* Biscuits x 1

#### Catalogue

* Baked Beans: £0.99
* Biscuits: £1.20

#### Offers

* Baked Beans: buy 2 get 1 free
* Sardines: 25% discount

### Running the implementation

The next steps can be executed to run the implementation of the shopping basket

  1.  Put the basket, catalogue and offers text files in the "data" folder or create new ones following the same format as in the examples above.
  2.  In a terminal, locate the main project folder (cx-interview-questions)
  3.  Execute the script using
      ```bash
      python3 shopping_basket_py
      ```
  4.  When running the script, you must send the following necessary parameters
      ```bash
      --basket-filename Location of the basket file in the project
      --catalogue-filename Location of the catalogue file in the project
      --offers-filename Location of the offers file in the project
      ```

#### Example

```bash
python3 shopping_basket.py --basket-filename shopping_basket/data/basket_test_1.txt --catalogue-filename shopping_basket/data/catalogue_full.txt --offers-filename shopping_basket/data/offers_test.txt
```
