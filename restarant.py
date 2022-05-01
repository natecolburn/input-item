#programmer:          Nathan Colburn
#program Name:        Total price of food
#Date written:        10/3/18
'''This program askes you to enter the price of the food, adds the tax and tip
and gives you the total price'''
#==================================================================================

#variables
salesTax = 0.0;
tax = 0.07;
tip = 0.20;
totalPrice = 0.00;
totalSalesAmount = 0.0;

#==================================================================================
#input statements

item = str(input("Enter name of item "));
foodPrice = float(input("Enter price of food "));


#==================================================================================
#calculations
totalPrice = foodPrice;
salesTax = totalPrice * tax;
tip = totalPrice * tip
totalPrice = totalPrice  + tip + tax;


#==================================================================================
#outputs
print();
print("-" * 60)
print("Item Name:    " + item);
print("Price:        " + "$" + format(foodPrice, "7.2f"));
print("Sales Tax:    " + "$" + format(salesTax, "7.2f"));
print("Tip:          " + "$" + format(tip, "7.2f"));
print("Total Amount: " + "$" + format(totalPrice, "7.2f"));