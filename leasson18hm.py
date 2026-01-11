try:
    age = int(input("Enter your age: "))
    
    
    if age < 0:
        print("Error: Age cannot be negative!")
    elif age > 120:
        print("Error: Age seems unrealistic!")
    else:
        print(f"Age {age} is valid.")
        
        
        if age % 2 == 0:
            print(f"{age} is an even number.")
        else:
            print(f"{age} is an odd number.")
            
except ValueError:
    print("Error: Please enter a valid number!")