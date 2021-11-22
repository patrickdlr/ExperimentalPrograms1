import time
import schedule 

def function_2():
    print('function 2 started...')
    # for a in range(5):
    #     print('B')
    #     time.sleep(1)

    schedule.every(5).seconds.do(print, 'A2')
    schedule.every(5).seconds.do(print, 'A2')
    schedule.every(5).seconds.do(print, '\n')