# buyLotsOfFruit.py
# -----------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
To run this script, type

  python buyLotsOfFruit.py

Once you have correctly implemented the buyLotsOfFruit function,
the script should produce the output:

Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
"""
from __future__ import print_function

# Defining a dictionary with fruit prices per pound
fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75,
               'limes': 0.75, 'strawberries': 1.00}


def buyLotsOfFruit(orderList):
    fruit_prices = {
        'apples': 2,
        'pears': 1.75,
        'limes': 0.75,
        'strawberries': 1.00
       
    }

    totalCost = 0.0 		#creating variable total cost as a zero 

    for fruit, numPounds in orderList:			#Iterate through each item in the orderList
         
        price_per_pound = fruit_prices.get(fruit, None)		#for the current fruit price per pound
        if price_per_pound is None:
            return f"Error: {fruit} is not in the price list."	#Print the error message if fruit is not found

        totalCost += price_per_pound * numPounds		#This will add in total after calculating current fruit

    return totalCost						#This will return the total cost of the order

orderList = [('apples', 2),('pears', 3),('limes', 4),]

totalCost = buyLotsOfFruit(orderList) 	#calculate the total cost of the order

print("Total cost: $",totalCost)


# Main Method
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orderList = [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)]
    print('Cost of', orderList, 'is', buyLotsOfFruit(orderList))



