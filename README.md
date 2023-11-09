# Financial Product Interest Rate Calculator written in Python

## Prerequisites:
- Make sure to have the latest stable version of Python installed on your system. 
- Set the PATH configurations for Python so that it can run in any directory if you are using Windows.

[Download Python](https://www.python.org/downloads/)

## Instructions:
1. Download the project.
2. Using your command line or terminal, navigate to the project folder where all the files are located.
3. Enter the command: `python rules_engine.py`
4. Input the values for the credit score, state, and name of the product.

![1](https://github.com/l1legend/Visio-Business-Request/assets/28288764/26538d38-5e06-448a-80f5-e31b10ae3dff)

The rules engine will calculate the interest rate and provide a boolean value regarding whether or not the product is disqualified based on the value for the state. 

## Rules:

Rules can be configured in `rules.json`. The default interest rate can be set here with the initial value of 5.
Additional rules can be added in this file.

## Running Unit Tests:
Enter the command: `python test_rules_engine.py` The unit test engine should run automatically.
