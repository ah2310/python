# LAST CHANGED : 2025/10/01
# Exercise 2.9 - page 23

TVA_CONSTANT  = 17
price_TTC = int(input("Enter your price (taxes included, TTC): "))


price_HTVA = (price_TTC * 100) / (100 + TVA_CONSTANT ) 
print("Price without taxes (HTVA): ", price_HTVA)
