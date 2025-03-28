from random import randint 
def generate_coupon_code(coupon_code_list):
    ''' This function takes N distinct Coupon Numbers and genrates random numbers to get distinct coupon number.
    
    It takes a list of distinct coupon codes from [0,1,2,3,4,5,6,7,8,9] as argument.
    
    It returns a dictionary where keys are coupon codes given by user and the values of each key is count of random choices needed to generate the coupon code.'''
    count_dict = {}
    a = '0'*coupon_code_length
    b = '9'*coupon_code_length
    for i in coupon_code_list:
        is_true = True
        count = 0
        while is_true:
            num = str(randint(int(a),int(b)))
            count += 1
            
            if num == i:
                is_true = False
                count_dict[i] = count
                break
    return count_dict

number_of_coupon_numbers = int(input("Enter the number of distinct coupon codes:"))
coupon_code_length = int(input("Enter the length of the coupon code between 1 and 12:"))
if 0 < coupon_code_length < 13:
    coupon_code_list = []
    print(f"Enter distinct number of coupon codes {number_of_coupon_numbers} times in the length of {coupon_code_length}:")
    i = 1
    while len(coupon_code_list) < number_of_coupon_numbers:
        x = input(f"Enter coupon number {i}: ")
        while len(x) != coupon_code_length:
            print("Coupon code length doesn't match. Please enter a valid code.")
            x = input(f"Enter coupon number {i}: ")
            
        if x in coupon_code_list:
            print("Coupon code already entered! Please enter a unique number.")
        else:
            coupon_code_list.append(x)  
            i += 1

        
else: 
    print("Coupon code length should be only between 1 and 12")
print(coupon_code_list)
print("Number of random choices to generate each coupon number = ", generate_coupon_code(coupon_code_list))


            
            
            

        
        
