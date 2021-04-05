#!/opt/local/bin/python3
"""
Threads a script

Date: 03/1/2019
Revised: 5/16/2019
Created By: John Richardson


"""
import threading
from queue import Queue

q = Queue()


def createWorkers(list):
    """createWorkers
    inputs the work into the queue

    Parameters: list

    Return
    Queue q
    """
    for worker in list:
        q.put(worker)
    return q


def threader(func):
    """threader
    Helper function fo createThreads to do the work

    Parameters: Function func

    Return
    void
    """
    while True:
        worker = q.get()
        func(worker, listLength=q.qsize())
        q.task_done()


def createThreads(threadCount, func):
    """createThreads
    Creates multiple threads

    Parameters: int threadCount, Function func

    Return
    void
    """
    for x in range(threadCount):
        t = threading.Thread(target=threader, args=(func,))
        t.daemon = True
        t.start()


def useThreader(list, threadCount, func):
    """useThreader
    Wrapper class for the Threader

    Parameters: List list, int threadCount, Function func

    Return
    void
    """
    createWorkers(list)
    createThreads(threadCount, func)
    q.join()
