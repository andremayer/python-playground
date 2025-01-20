from functools import reduce

def main():
    celsius_temps = [0, 20, 30, 40]
    fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
    print("Celsius to Fahrenheit:", fahrenheit_temps)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
    print("Odd numbers:", odd_numbers)

    product_of_numbers = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
    print("Product of numbers:", product_of_numbers)

    print("Running tests...")
    run_tests()
    print("All tests passed!")

def run_tests():
    assert list(map(lambda c: (c * 9/5) + 32, [0, 20, 30])) == [32.0, 68.0, 86.0]

    assert list(filter(lambda x: x % 2 != 0, [1, 2, 3, 4, 5])) == [1, 3, 5]

    assert reduce(lambda x, y: x * y, [1, 2, 3, 4]) == 24

if __name__ == "__main__":
    main()
