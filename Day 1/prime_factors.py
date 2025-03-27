def check_prime(number):
    
    '''This function takes number as an argument.
    It returns true if the number is prime.
    Else returns false'''

    for i in range(2,number):
        if number%i == 0:
            return False
        
    return True
        
def prime_factors(number):

    ''' This function takes number as an argument.
    Returns a list of it's Prime Factors '''

    prime_factor_list = []
    for i in range(2,number):
        if number%i == 0 and check_prime(i):
            prime_factor_list.append(i)
    return prime_factor_list

number = int(input("Enter the number to find it's prime factors:"))
prime_factors_of_number = prime_factors(number)
print(f'Prime factors of {number} = ', prime_factors_of_number)