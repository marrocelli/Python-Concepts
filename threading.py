# Threading

# A small preface:
# A CPU is made up of a number of processesing cores (back in the day it used to be just one), 
# but now computers can have (4, 8, 16, 32+)
# Essentially, the number of cores a CPU has is the number of things that you computer
# can process at the exact same time (4 cores means your CPU can do 4 operations at the exact same time).
# These computations are low level computations, and depending on the power of your computer, billions of them happen per second.

# A THREAD is essentially one program or one set of operations that needs to happen.
# Threads are assigned a CPU core that will handle its operations and the concept of THREADING is
# essentially how we determine when to run different threads on the same CPU core.
# Threading does not involve running things on multiple cores (that is called multiprocessing).

# Multithreading is the idea of breaking a program or process up into multiple threads of execution.
# The point of threading is that sometimes a thread can be "hanging" or waiting for something
# to happen like (waiting for a user to do something or a network to send a file, etc.), our program doesn't
# need to be idle while it waits. The processor core can go execute operations
# on another thread while the hanging thread..hangs and waits for something to happen.
# This is called concurrent programming.

# Threading is useful for things like online games and chat apps. If you were creating 
# a chat app and had your server and client functionality running on the same thread,
# a user would not be able to do anything while the server is handling messages from other users.
# All other users would have to wait for the other messages to be processed by the server 
# before they can do anything..which would not be a good user experience. Messages should be
# processed whenever the server can get to them, but the user (client) should still be able to do stuff.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

import threading # _thread in Python 2
import time

# To create a thread, you must pass in a target argument which will be the function that we want to run on the thread.
# If you want to pass arguments to that funcion, you must pass those to the args argument as a tuple.
# If you will only be passing in a single argument to the target function, you need to pass it to the tuple with
# a comma: args=(5,) because python will just evaluate a single number wrapped in parenthesis as just that number and not a tuple.
# Note: Do not use parenthesis when passing the target function.

# Creating a function that is going to act as our thread.
def thread_func():
    print("first")
    time.sleep(1)
    print("next")

# creating a thread called x
x = threading.Thread(target=thread_func)

# To run a thread, you must start it
x.start()

# Keep in mind that our current program is already running on a thread of its own, so creating
# this new thread will mean that we now have 2 threads: our main thread and x.

# To get the number of active threads your program is running, you can use the .activeCount() method.
print(f"{threading.activeCount()} threads") # 2

time.sleep(1)
print("done")

# Notice the order that this program prints to the console. First we create the x thread and start it.
# The x thread prints "first" and then it sleeps for one second. While the x thread sleeps, the program
# switches over to the main thread and prints the number of active threads (in this case "2 threads").
# Then, while the main thread sleeps for one second, the x thread runs and prints "next". 
# Finally, since the x thread has finished executing all of its code, we return to the main thread and
# print "done".


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# This program creates two identical threads that each count to a given number n. Between printing each number to 
# the screen the function will sleep for one second. Once all the numbers have been printed, it will return "Done".
def count(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(1)
    print("Done")

for _ in range(2):
    x = threading.Thread(target=count, args=(10,))
    x.start()

# Notice that threads take turns printing the next number to the screen instead of one running through all of
# the numbers and then the other one running through all of its numbers.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Of course, we may want to have a little more control of when certain threads run than just whenever the computer decides.

# If we want to wait for a thread to finish running before doing anything else, we can use the .join command.
# Pretty much what the .join() method is saying is, "Do not continue past this 
# line of code until the thread has finished running." 

nums = []

def count(n):
    for i in range(1, n+1):
        nums.append(i)
        time.sleep(0.01)
    print("Done")


x = threading.Thread(target=count, args=(10,))
x.start()

y = threading.Thread(target=count, args=(10,))
y.start()

# The main thread will not continue until the x and y threads have finished executing.
x.join()
y.join()

print(nums) # [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Here I have moved the location of one of the .join() calls to show how it affects the overall program.
nums = []

def count(n):
    for i in range(1, n+1):
        nums.append(i)
        time.sleep(0.01)
    print("Done")


x = threading.Thread(target=count, args=(10,))
x.start()

# Moving the x.join() here will mean that the main program will not continue until the thread x has finished running.
# This is how you can synchronize threads together to make sure they run in the desired order.
x.join()

y = threading.Thread(target=count, args=(10,))
y.start()

y.join()

# Notice how instead of the threads running at the same time, x runs first, then y.
print(nums) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Using multiple threads can be dangerous when it comes to accessing shared resources, because if you have
# multiple processes accessing and changing a variable at the same time, it is possible that 
# multiple threads will try to update a resource at the same time which can lead to inconsistent results.
# This problem can be addressed using locks. 

# By locking shared resources, you can ensure that both threads are not making changes
# at the same time. When two threads try to update a shared variable at the same time, this
# is called a race condition.

# To show the inconsistencies, I've commented out the lock.acquire() and lock.relase() in both functions.
# Try running the program a few times. You will notice that the answer is different every time even though
# the sum of all of the numbers between 1 and 1000000 should always be the same. When you're ready, go
# ahead and uncomment the lock.acquire() and lock.release() in both functions and run the program a few times.
# You should see that the program consistently returns 500000500000, which is the correct answer.
# This is because the lock prevented both threads from accessing the total variable at the same time and 
# creating a race condition.

total = 0
# Create a Lock instance. Will have a status of unlocked by default
lock = threading.Lock()

def add_first_half(lock):
    """ Adds every integer from 1 to 500,000 """
    global total
    for num in range(500001):
        # lock.acquire() # acquire the lock
        total += num
        # lock.release() # release the lock

def add_second_half(lock):
    """ Adds every integer from 500,001 to 1,000,000 """
    global total
    for num in range(500001, 1000001):
        # lock.acquire() # acquire the lock
        total += num
        # lock.release() # release the lock

x = threading.Thread(target=add_first_half, args=(lock,))
x.start()

y = threading.Thread(target=add_second_half, args=(lock,))
y.start()

x.join()
y.join()

print(total)
