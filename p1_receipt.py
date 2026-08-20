#USER'S INFORMATION

customer_name = input("Customer name: ")
Contact = input("Contact no: ")
Address = input("Address: ")

print("")

#PRODUCT 1

product1 = input("Product Name: ")
price1 = int(input("Price: "))
quantity1 = int(input("Quantity: "))
amount1 = price1 * quantity1

print("")

#PRODUCT 2

product2 = input("Product Name: ")
price2 = int(input("Price: "))
quantity2 = int(input("Quantity: "))
amount2 = price2 * quantity2

print("")

#PRODUCT 3

product3 = input("Product Name: ")
price3 = int(input("Price: "))
quantity3 = int(input("Quantity: "))
amount3 = price3 * quantity3

print("")

#TOTAL AMOUNT

discount = float(input("Enter Discount: "))

subtotal = amount1 + amount2 + amount3
discounted = subtotal * (discount / 100)
Total = subtotal - discounted

print("")

#RECEIPT

print("========================================")
print("           STORE RECEIPT")
print("========================================")

print("Name: ", customer_name)
print("Contact no: ", Contact)
print("Address: ", Address)

print("")
print("----------------------------------------")
print("Product   Price   Quantity   Amount")
print("-----------------------------------------")

print(product1, ":", price1, quantity1, amount1)
print(product2, ":", price2, quantity2, amount2)
print(product3, ":", price3, quantity3, amount3)

print("")
print("----------------------------------------")
print("Subtotal: ", subtotal)
print("Discount: ", discounted)

print("")
print("----------------------------------------")
print("Total Price: ", Total)

print("")
print("========================================")
print("Thank you for your purchase!")
print("Please come again!")
print("========================================")