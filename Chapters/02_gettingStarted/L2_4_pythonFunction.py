# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 02:09:20 2019

@author: manma
@project:

@purpose: Demonstration of a Python Function
"""

# import standard packages
import numpy as np


def incomeAndExpenses(data):
    """
    Find the sum of the positive numbers, and the sum of
    the negative ones
    """
    income = np.sum(data[data > 0])
    expenses = np.sum(data[data < 0])

    return (income, expenses)


if __name__ == '__main__':
    testData = np.random.randint(-100, 100, size=100)

    # If only real banks would be so nice ;)
    if testData[0] < 0:
        print('Your first transaction was a loss and will be dropped')
        testData = np.delete(testData, 0)

    else:
        print('Congratulations. Your first transaction was a gain!')

    (myIncome, myExpenses) = incomeAndExpenses(testData)
    print('You have earned {0:5.2f} USD, and spent {1:5.2f} USD'
          .format(myIncome, -myExpenses))
