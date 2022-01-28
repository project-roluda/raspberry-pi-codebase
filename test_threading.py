from threading import Thread
import time

def func1():
    print('Working')
    time.sleep(1.5)

def func2():
    print("Working")
    time.sleep(1)

if __name__ == '__main__':
    s = time.time()
    t1 = Thread(target = func1)
    t2 = Thread(target = func2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()   
    print(time.time()-s)