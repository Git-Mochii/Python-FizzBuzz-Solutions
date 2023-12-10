# Fizz Buzz interview question practical
# If number is multiple of 3 and 5 then output: FizzBuzz
# If number is multiple of 3 only then output: Fizz
# If number is multiple of 5 only then output: Buzz 

# Solution 1

for fizzbuzz in range(1, 101):

    if fizzbuzz  % 3 == 0 and fizzbuzz % 5 == 0:
        print("FizzBuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("Fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("Buzz")
        continue
    else:
        print(fizzbuzz)