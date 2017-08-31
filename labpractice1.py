Dollar = float(input("What is the amount of US dollars you wish to convert?"))
exchangerate = float(input("What is the current exchange rate?"))
answer = Dollar*exchangerate
print("The amount in the foreign Currency is", "%1.2f"%answer)
