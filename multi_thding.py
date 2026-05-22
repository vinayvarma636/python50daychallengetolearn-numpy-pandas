# multithereading in python
#multi_threading calling funtion threading.Thread(target=my_funtion)
import threading
import time

def watch_movie():
    time.sleep(10)
    print("current watching movies for last 5min i will end in within 10 sec")
def eating():
    time.sleep(3)
    print("oh! i finally finishied movie and now i can eat lets go")
def sleeps():
    time.sleep(5)
    print("oh! i finally finished eatting noe i can sleep")

thread_obj1 = threading.Thread(target=watch_movie)
thread_obj1.start() #we need to start the thread with startfuntion
thread_obj2 = threading.Thread(target=eating)
thread_obj2.start()
thread_obj3 = threading.Thread(target=sleeps)
thread_obj3.start()




