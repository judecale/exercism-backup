def is_armstrong_number(number):
    original = number
    number = abs(number)
    power = len(str(number))
    
    def sum_digits_power(num, power):
        if num == 0:
            return 0
        return (num % 10) ** power + sum_digits_power(num // 10, power)
    return sum_digits_power(number, power) == original