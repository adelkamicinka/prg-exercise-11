def main():
    print("Hello from prg-exercise-11!")


if __name__ == "__main__":
    main()

import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

values = random_numbers(10)
print(values)
small = random_numbers(5, low=0, high=20)

