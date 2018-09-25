"""

This program takes Product type along with it's price and quantity into a empty nested dictionary.
Output contains complete inventory list and the final cost to be paid.

Author : Nihar Mukhiya
Version: 2
Date: 02/09/2018

"""
import sys
import pprint
inventory = {1:{'product', 'price', 'quantity'}}
while(1):
    a = input("want to add a product? y or n: ")
    if(a == 'y'):
        b = int(input("enter the no. of products to be added to inventory: "))
        i = 1
        for i in range(b):
            p = input("enter the type of product: ")
            amt = input("enter the price: ")
            qty = input("enter the quantity: ")
            inventory[i] = {}
            inventory[i]['product'] = p
            inventory[i]['price'] = float(amt)
            inventory[i]['quantity'] = int(qty)
            i+=1
    elif (a == 'n'):
        pprint.pprint(inventory)
        print("\n")
        total = 0
        for j in inventory:
            total += inventory[j]['price'] * inventory[j]['quantity']
        print("\n")
        print("Money to be paid is: ")
        print(total)
        sys.exit()
    elif(a == 'x'):
        sys.exit()
        sys.exit()
    else:
        print("invalid choice!")