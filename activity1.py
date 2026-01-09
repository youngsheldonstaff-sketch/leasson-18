try:
    n = int(input("enter a number: "))
    print("you entered:", n)   
#using value error 
except ValueError as ex:
    print("invalid input, try again")
    print(ex)
    