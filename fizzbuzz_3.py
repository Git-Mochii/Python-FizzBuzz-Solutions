# Fizz Buzz interview question practical
# If number is multiple of 3 and 5 then output: FizzBuzz
# If number is multiple of 3 only then output: Fizz
# If number is multiple of 5 only then output: Buzz 

# Solution 3

num_list = [*range(1, 101)]

fizzbuzz = [

    "FizzBuzz" if num % 3 == 0 and num % 5 == 0 else
    "Fizz" if num % 3 == 0 else
    "Buzz" if num % 5 == 0 else num
    for num in num_list
]

print(fizzbuzz)