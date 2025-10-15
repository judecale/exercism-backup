def steps(number, stepx = 0 ):
    if 0 + number <= 0:
        raise ValueError("Only positive integers are allowed")
    if number == 1:
        return stepx
    if number % 2 == 0:
        return steps(number / 2, stepx + 1)
    if number % 2 != 0:
        return steps((number * 3) + 1, stepx + 1)
