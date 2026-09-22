def check_even_odd(number):
        if number % 2 == 0:
            return f"{number} is even"
        else:
            return f"{number} is odd"

def is_positive(number):
    if number > 0:
        return f"{number} is positive"
    elif number < 0:
        return f"{number} is negative"
    else:
        return f"{number} is zero"