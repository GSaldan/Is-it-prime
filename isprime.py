number = int(input('Select a number: '))


def is_prime(x):
    for i in range(2, x):

        if (x % i) == 0:
            return f'{x} is not prime'

    return f'{x} is prime'


is_prime(number)
print(is_prime(number))
