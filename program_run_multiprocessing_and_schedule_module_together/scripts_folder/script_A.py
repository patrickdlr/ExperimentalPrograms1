import time
import schedule 

def schedule_function1():
    print('function 1 started...')

    schedule.every(5).seconds.do(print, 'A1')
    schedule.every(5).seconds.do(print, 'A1')
    schedule.every(5).seconds.do(print, '\n')

def schedule_function1_1():
    schedule.every(2).seconds.do(forloop1)

def forloop1():
    for a in range(4): 
        print('forloop1')
        time.sleep(0.5)     

def whileloop1():
    #while true seems to not run in parallel with/take over scheduled functions
    while True: 
        print('whileloop1')
        time.sleep(0.5)




