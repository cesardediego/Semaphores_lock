from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value, Array
from multiprocessing import Lock
import time
import random
N = 8

def task(common, tid, lock):
    a=0
    for i in range(10):
        print(f'{tid}-{i}:Non-critical Section',flush = True)
        a += 1
        time.sleep(random.random())
        print(f'{tid}-{i}:End of non-critical Section',flush = True)
        lock.acquire()
        ##############################################
        print(f'{tid}-{i}:Critical section',flush = True)
        v = common.value +1
        time.sleep(random.random())
        print(f'{tid}-{i}:Inside critical Section',flush = True)
        common.value = v
        print(f'{tid}-{i}:End of critical Section',flush = True)
        ##############################################
        lock.release()

def main():
    lock = Lock()
    lp = []
    common = Value('i',0)
    for tid in range(N):
        lp.append(Process(target=task, args=(common,tid,lock)))
    print(f"Valor inicial del contador {common.value} ", flush = True)    
    for p in lp:
        p.start()
        
    for p in lp:
        p.join()
    print(f"Valor final del contador {common.value}",flush = True)
    print("fin")  

if __name__ == "__main__":
    main()