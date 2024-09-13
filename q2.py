# Yes, Django signals run in the same thread as the caller by default.

# To run the code in a different thread, we can use the django-rq library.

# code snippet
def user_saved(sender, instance, **kwargs):
    print(f"Signal thread: {threading.current_thread().name}")

def create_user():
    print(f"Caller thread: {threading.current_thread().name}")
    User.objects.create(username="testuser")

# If we run the above code in django the create_user function will be executed in the main thread of the django application. and here
# is the output of the code

# Caller thread: MainThread
# Signal thread: MainThread

# From the above output we can say that the signal is executed in the same thread as the caller by default.
