score = float(input("Enter Score: "))
         
try:
    if score < 0 or score > 1:
        raise ValueError('Your grade is outside the range of 0 and 1.') 
    
    if score >= 0.9:
        print("A")

    elif score >= 0.8:
        print("B")

    elif score >= 0.7:
        print("C")

    elif score >= 0.6:
        print("D")

    else:
        print("E")
except ValueError as err:
    print('erro: ', err)