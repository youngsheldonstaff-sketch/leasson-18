try:
    n,m = eval(input("enter two numbers separated by a comma: "))
    result = n/m
    print(f"{n} divided by {m} is {result}")

except ZeroDivisionError: 
    print("Error: cannot divide by zero.")
except SyntaxError:
    print("Error: invalid input format. please enter numbers seperated by a comma.")
except:
    print("wrong number ")
else:
    print("no exceptions")
finally:
    print("this will execute no matter what")
