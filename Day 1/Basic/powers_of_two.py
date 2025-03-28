def powers_of_two(number_of_two_powers):

    '''This function asks for the number until which, you want the powers of 2.
    And returns a table of powers of 2 until the given number'''

    for i in range(number_of_two_powers + 1):
        power_of_two = 2 ** i
        print(f'2 power {i} = {power_of_two}')

is_true= True
while is_true:
    number_of_two_powers = int(input("Enter a number to get powers of 2 until it:"))
    if number_of_two_powers > 31:
        print("Enter number smaller than 31")
        continue
    else:
        print(powers_of_two(number_of_two_powers))

        