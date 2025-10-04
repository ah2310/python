dividende = int(input("Dividende: "))

diviseur = int(input("Diviseur: "))

quotient = dividende // diviseur

reste = dividende % diviseur

if diviseur==0:
    print("Dat fonktionneiert sou net")

else:
    print(f"{dividende} = {diviseur} * {quotient} + {reste}")
