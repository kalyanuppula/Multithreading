#Multithreading in Python

#Example - 1 [ Without involving threads ]
'''
def fun1():
    print("Function 1")
def fun2():
    print("function 2")
fun1()
fun2()
'''
#Example - 2 [ With Threads ]
'''
import threading
def fun1():
    print("Function 1")
def fun2():
    print("Function 2")
t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)
t1.start()
t2.start()
'''

#Note: We have to use the multithreading concept when the
#function are not having relationships with each other

#Example - 4 [ User Defined Threads ]
'''
import threading
class Login_Thread(threading.Thread):
    def run(self):
        print("Login.....")
class Register_Thread(threading.Thread):
    def run(self):
        print("Register.....")
t1 = Login_Thread()
t2 = Register_Thread()
t1.start()
t2.start()
'''

#Example - 5.1 [ Threading ]
'''
from threading import Thread
def fun1():
    print("Function 1")
def fun2():
    print("Function 2")
t1 = Thread(target=fun1)
t2 = Thread(target=fun2)

t1.start()
t2.start()
'''
#Example - 5.2 [ Threading ]
'''
from threading import Thread
def fun1():
    print("Function 1")
def fun2():
    print("Function 2")
t1 = Thread(target=fun1)
t2 = Thread(target=fun2)

t2.start()
t1.start()
'''
#Example - 6
'''
from threading import Thread
def fun1():
    for i in range(5):
        print("Python")
def fun2():
    for j in range(5):
        print("Program")

t1 = Thread(target=fun1)
t2 = Thread(target=fun2)

t1.start()
t2.start()
'''
#Example - 7 [ Time Module ] [ Waiting State ]
'''
from threading import Thread
import time
def fun1():
    time.sleep(2)
    print("Hello world")
def fun2():
    print("Hello Python")
t1 = Thread(target=fun1)
t2 = Thread(target=fun2)

t1.start()
t2.start()
'''

#Example - 8 [ Using join() ]
'''
from threading import Thread
import time
def fun1():
    time.sleep(2)
    print("Hello world")
def fun2():
    print("Hello Python")
t1 = Thread(target = fun1)
t2 = Thread(target = fun2)
t1.start()
t1.join()
t2.start()
t2.join()
'''
#Note: join() is used to complete the operation of the thread
#before implementing the next thread
    

#Example - 9 [ Race Condition ]
'''
from threading import Thread
counter = 0
def fun1():
    global counter
    for i in range(1000000):
        counter = counter + 1
def fun2():
    global counter
    for j in range(1000000):
        counter = counter + 1
t1 = Thread(target=fun1)
t2 = Thread(target=fun2)
t1.start()
t2.start()
print(counter)
'''
#Example - 10 [ Race condition ] [ Join() ]
from threading import Thread
counter = 0
def fun1():
    global counter
    for i in range(1000000):
        counter = counter + 1
def fun2():
    global counter
    for j in range(1000000):
        counter = counter + 1
t1 = Thread(target=fun1)
t2 = Thread(target=fun2)
t1.start()
t1.join()
t2.start()
t2.join()
print(counter) #2000000
