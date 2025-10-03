# LAST CHANGED : 2025/10/01
# Exercise 2.13 - page 24

first_term = int(input("first term: "))
common_difference = int(input("common difference: "))
n = int(input("n: "))

sequence = ""

for x in range(1, n+1):
    n_term = first_term
    sequence += (str(first_term) + " ")
    first_term += common_difference
    
print("-----------------------------")
print("sequence                 : ", sequence)
print(f"{n}-th number of sequence : ", n_term)
    
    
