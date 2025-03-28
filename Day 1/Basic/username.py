def user_name():

    ''' This function asks for username.
    Checks if it is atleat 3 characters.
    If it is 3 characters or more than 3, it greets you!'''

    is_true= True
    while is_true:
         username = input("Enter your Username:")
         if len(username) < 3:
               print("Usename must be atleast 3 characters")
               continue
         else:
                is_true = False
                print(f"\"Hello {username}, How are you?\"")


if __name__ == '__main__':
      user_name()

    
