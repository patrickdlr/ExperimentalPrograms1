'''*****************************************************
# this program experiments with running 2 functions in parallel (using multiprocessing or threading module) repeatedly (using while loop or schedule module)
*****************************************************'''
import time
from multiprocessing import Process
from threading import Thread
import schedule
import sys

'''*****************************************************
# use sys module to make this program find & import modules from another directory/folder
# insert at 1, 0 is the script path (or '' in REPL)
*****************************************************'''
sys.path.insert(1, r'program_run_multiprocessing_and_schedule_module_together\scripts_folder')

'''*****************************************************
# import functions
*****************************************************'''
from script_A import *
from script_B import * 



'''*****************************************************
# function: runs two target functions normally
*****************************************************'''
def run_batch_of_functions_1():
    start_time = time.time()

    forloop1()
    forloop2()

    print("--- %s seconds ---" % (time.time() - start_time))
    print()

'''*****************************************************
# function: runs two target functions in parallel (using multiprocessing module) with explanations:
*****************************************************'''
def run_batch_of_processes_1():
    start_time = time.time()

    # create separate process for each function 
    # should reinitialize those process variables if starting them multiple time (in while loop or schedule module)
    process_0 = Process(target=schedule_function1_1, args=()) 
    process_1 = Process(target=forloop1)
    process_2 = Process(target=forloop2)

    # starts the processes
    process_1.start() 
    process_2.start()

    # wait till they all finish and close them
    process_1.join()
    process_2.join()

    print("--- %s seconds ---" % (time.time() - start_time))
    print()

'''*****************************************************
# function: runs two target functions in parallel (using threading module):
# explanation needed atm
*****************************************************'''
def run_batch_of_threads_1():
    start_time = time.time()

    thread_1 = Thread(target=forloop1)
    thread_2 = Thread(target=forloop2)
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()

    print("--- %s seconds ---" % (time.time() - start_time))
    print()



if __name__ == '__main__':
    '''*****************************************************
    # way 1: runs target functions (in parallel) repeatedly (using while loop)
    *****************************************************'''
    # while True:
    #     run_batch_of_functions_1()
   
    '''*****************************************************
    # way 2: runs target functions (in parallel) repeatedly (using schedule module)
    *****************************************************'''
    schedule.every(0).seconds.do(run_batch_of_processes_1)
    while True:
        schedule.run_pending()

        
    
