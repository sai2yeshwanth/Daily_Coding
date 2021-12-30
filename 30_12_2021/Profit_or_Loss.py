# The amount at which a product is sold by the seller is known as the Selling Price.
#The amount at which the Seller has Acquired the product is know as the Coust price.

CP = int(input("Enter the Cost Price \n"))
SP = int(input("Enter the Selling Price \n"))

if CP < SP:
    print("Profit")
elif CP > SP:
    print("Loss")
elif CP == SP:
    print("No Profit - No Loss")