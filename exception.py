try:
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    
    result = numerator / denominator
    print(f"Result: {result}")
    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    
except ValueError:
    print("Error: Invalid input. Please enter valid integers.")
    
finally:
    print("Execution completed.")
