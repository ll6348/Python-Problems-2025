import time
def stop_watch():
    '''This function measures the time that elapses between the start and end inputs. 

    It takes firts input start and caluculates the time using time.time() function. 
    If user give some thing else instesd of start in any case. It says "You have to enter start to start the stop watch" and asks to give start as an input again
    It takes second input as end and caluculates the  end time using time.time() function.
    If user give some thing else instesd of end in any case. It says "You have to enter start to start the stop watch" and asks to give end as an input again

    It returns the elapsed time by subracting start time from end time.
'''
    is_true_for_start = True
    while is_true_for_start:
        start = input("Enter Start to start the stop watch:")
        if start.lower() == 'start':
            start_time = time.time()
            is_true_for_start = False
            is_true_for_end = True
            while is_true_for_end:
                end = input("Enter end to end the stop watch: ")
                if end.lower() == 'end':
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    is_true_for_end = False
                else:
                    print('you have to enter end to end the stop watch')
        else:
            print("You have to enter start to start the stop watch")

    return elapsed_time
print(stop_watch())

    