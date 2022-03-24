# Assignment

In the following repository it can be found 2 different folders, each of them related to the proper request.

## Number Printer Exercise

```Write a program in Python or Java that counts backwards from 100 to 1 and prints: “Agile” if the number is divisible by 5, “Software” if the number is divisible by 3, “Testing” if the number is divisible by both, or prints just the number if none of those cases are true.```

- related folder: ```number-printer```

## Test Automation Framework

```Use your preferred test automation tool to automate test case: Go to your favorite e-shop, navigate to some category and add two most expensive items to the shopping cart from this category. Provide code from implementation.```

- related folder: ```test-case```

  The Automation Framework contains one executable test named as ```test_basket_collection_contains_proper_items``` and it is built in order to test the www.aboutyou.com website.
  
  For the test implementation it has been used:
  - Programming Language: ```Python v3.9```
  - Browser: ```Google Chrome v99.0.4844```
  - Web Handler Framework: ```Selenium v4.1.2```

  The project structure is based on 2 main design patterns:
  1. ```Page Object Model``` -> for creating the web page objects 
  2. ```Builder``` -> to build the object while creating the tests

### Setup:
1. Open the project with `PyCharm`.
2. Make sure to create a `virtualenv` specifically for this project.
3. Once you did that, open a new terminal. Activate the virtual environment with `. venv/bin/activate`.
4. Install the requirements using `pip install -r requirements.txt`

### Configuration:

You need to set the following environment variables in order for tests to run successfully:

| Variable name | Mandatory | Default value | 
| --- | --- | ---- |
| BASE_URL | Y | https://www.aboutyou.com?force-global=1&force-language=1 |
| HEADLESS | N | - |

### Run Test:

1. Open a terminal inside `test-case` folder (or open the project in `PyCharm` and access the `Terminal`)
2. Add the mandatory environment variable as: `export BASE_URL='https://www.aboutyou.com?force-global=1&force-language=1'`
3. Execute the tests using the following command: `python -m pytest aboutyou/tests/basket_tests/basket_collection_test.py`
