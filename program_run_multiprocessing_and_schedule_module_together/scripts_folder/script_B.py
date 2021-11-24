import time
import schedule 

def schedule_function2():
    print('function 2 started...')

    schedule.every(5).seconds.do(print, 'A2')
    schedule.every(5).seconds.do(print, 'A2')
    schedule.every(5).seconds.do(print, '\n')

def schedule_function2_1():
    schedule.every(2).seconds.do(forloop2)

def forloop2():
    for a in range(4): 
        print('forlop2')
        time.sleep(0.5)     