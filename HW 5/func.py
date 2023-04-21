def math_power(num1, num2):
    if num2 == 1:
        return num1

    return num1 * math_power(num1, num2 - 1)

def sum(a, b):
    if b <= 0:
        return a + 0

    return sum(a + 1, b - 1)


    