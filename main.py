import time
from threading import Thread
import schedule

###
from script_A import *
from script_B import * 
###



thread_1 = Thread(target=function_1)
thread_2 = Thread(target=function_2)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()


while True:
    schedule.run_pending()

# print("thread finished") - redundant