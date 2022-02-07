def fizzBuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
            continue
        if i % 5 == 0 and i % 3 != 0:
            print("Buzz")
            continue
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            continue

        print(i)


if __name__ == "__main__":
    fizzBuzz(15)
