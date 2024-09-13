# By default, Django signals are executed synchronously, which means that the signal handler runs in the same thread and transaction as 
# the calling code, blocking further execution.


def user_saved(sender, instance, **arg):
    print("Signal received")
    time.sleep(5)  # Simulating long task
    print("Signal finished")

def create_user():
    print("Before user creation")
    User.objects.create(username="testuser")
    print("After user creation")


#If we run the above code in django the create_user function, it will take 5 seconds to complete. and give us a output like this
# Before user creation
# THen it will call the user_saved functiona and then give the below tow lines of output where the difference between the 1st signal received 
# message and 2nd signal received is 5 sec
# Signal received
# Signal finished
# Then this below line of the output will be printed which will be the output of the create_user function
# After user creation. From this above output we can say that the signal is executed synchronously.
