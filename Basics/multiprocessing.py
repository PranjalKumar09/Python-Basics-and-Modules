from multiprocessing import Process, cpu_count


""" processing a multi 
running tasks in parralel on differnt cpu cores by passses GIL sed (multiprocessing) better for cpu boundmtask (heavy cpu usage)

multithreading = better for io bound tasks (waiting around)
"""
 
def counter(num):
    count = 0
    while count < num:
        count += 1

def main(): 
    a = Process(target=counter, args = (10000))
    a.start()
    a.join()
    print(time.perf_counter() , "sec")

if __name__ == "__main__":
    main()
 
 
 