# Fizz Buzz interview question practical
# If number is multiple of 3 and 5 then output: FizzBuzz
# If number is multiple of 3 only then output: Fizz
# If number is multiple of 5 only then output: Buzz 

# Solution 2

for i in range(1, 100):

    output = ""
    if i % 3 == 0:
        output = "Fizz"
    elif i % 5 == 0: 
        output = "Buzz"

    print(output or i) 