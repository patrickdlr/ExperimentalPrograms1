import time
import schedule 



def function_1():
    print('function 1 started...')
    # for a in range(5):
    #     print('A')
    #     time.sleep(1)

    schedule.every(5).seconds.do(print, 'A1')
    schedule.every(5).seconds.do(print, 'A1')
    schedule.every(5).seconds.do(print, '\n')


