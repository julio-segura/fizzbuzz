print("""Welcome to FizzBuzz. This program prints "fizz" if the number you enter is divisible by 3, "buzz" if the number you enter is divisible by 5,
and "fizzbuzz" if the number you enter is divisible by both.""")

# user enters a number between 1 and 100
end = input("Please, enter a number between 1 and 100 to start the game: ")
end = int(end)

# program starts to count to that number (prints them in the Terminal)
for num in range(1, end+1):
# in case the number is divisible with 3, it prints "fizz"
    if num % 3 == 0:
        print("fizz")
# if the number is divisible with 5, it prints "buzz"
    elif num % 5 == 0:
        print("buzz")
# if it's divisible with both 3 and 5, it prints "fizzbuzz"
    elif num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    else:
        print(num)
