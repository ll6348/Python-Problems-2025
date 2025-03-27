def harmonic_number(number):

    '''This function takes a number as an argument.
    Caluculates the harmonic number of the number.
    Returns the caluculated Harmonic number.'''

    harmonic_number_of_given_number = 0
    for i in range(1,number + 1):
        harmonic_number_of_given_number += 1/i
    return harmonic_number_of_given_number

number = int(input("Enter a number to compute it's harmonic number:"))
print(f'Harmonic number of {number} = ' ,harmonic_number(number))