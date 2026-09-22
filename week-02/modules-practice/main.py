from utils import check_even_odd, is_positive

while True:
    try:
        input_number = int(input("Enter a number: "))
        print(input_number)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        
print("User Input:", input_number)
print(check_even_odd(input_number))
print(is_positive(input_number))