import random
def percentage_of_heads_and_tails(number_of_coin_flips):
    '''This function takes the argument of number of coin flips.
    It randomly chooses '0' or '1' using random module for the each coin flip and sums it all. 
    The sum is divided by number of coin flips to calculate the percentage.
    If the percentage is less than 0.5 it reutrns "Tails" else returns "Heads"
    '''
    my_list = [0,1]
    sum = 0
    for i in range(number_of_coin_flips):
        sum += random.choice(my_list)
    return sum/number_of_coin_flips

is_true= True
while is_true:
    number_of_coin_flips = int(input("Enter the number of coin flips:"))
    if number_of_coin_flips < 0 :
        print("Enter positive number")
        continue
    else:
        is_true = False
        percentage = percentage_of_heads_and_tails(number_of_coin_flips)
        if percentage < 0.5:
            print("Tails")
        elif percentage > 0.5:
            print("Heads")
        else:
            print("some error")

