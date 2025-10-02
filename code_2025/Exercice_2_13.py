# LAST CHANGED : 2025/10/01
# Exercise 2.13 - page 24


first_term = int(input("first term: "))
common_difference = int(input("common difference: "))
n = int(input("n: "))



for x in range(1, n+1):
    print("Term [", x, "] : ", first_term)
    result = first_term
    first_term += common_difference
    
   
    
print("-----------------------------")
print("n-th number of sequence: ", result)
    