from multiprocessing import Process, Value

def increment(counter):
    for _ in range(100000):
        with counter.get_lock():
            counter.value += 1


if __name__ == "__main__":
    counter = Value('i', 0)
    processess = [Process(target=increment, args=(counter, )) for _ in range(4)]
    [p.start() for p in processess]
    [p.join() for p in processess]

    print("Final counter value: ",counter.value )