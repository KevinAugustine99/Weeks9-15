"""
File : tasks.py
Assignment : HW #11
Language : python3
Author : Kevin Augustine < kea4437@rit.edu >
"""
from priority_queue import *

@dataclass
class Task:
    name: str
    priority: int
    __slots__ = "name","priority"

def make_task(name,priority):
    """make_task creates and returns a Task
        name: a string with the name of the Task
        priority: an integer with the priority of the Task
    """
    return Task(name,priority)

def test_1():
    """test_1 tests all of the functions and if they work the way they are suppossed to
        q: the priority queue
    """
    print("Start Test 1:")
    print("Create a empty priority queue:")
    q = make_priority_queue()
    print("Empty queue: ", q)
    print("Test if the priority queue is empty: ", is_empty(q))

    enqueue(q, make_task("E", 4))
    enqueue(q, make_task("A", 7))
    enqueue(q,make_task("B",6))
    enqueue(q,make_task("F",3))
    enqueue(q,make_task("C",6))
    enqueue(q,make_task("D",5))
    print("\n"+"Add six tasks to the priority queue:")
    print("Priority Queue:",q)
    print("Test if the priority queue is empty:",is_empty(q))

    print("\n"+"Highest priority task is", front(q).name, "with priority",
    front(q).priority)

    print("Lowest priority task is", back(q).name, "with priority",
    back(q).priority)

    print("\n"+"Test the dequeue function and front function by iterating through each Task")
    while not is_empty(q):
        print(front(q).name,",",front(q).priority, sep='', end= ' : ')
        print(front(q) == q.front.value)
        dequeue(q)

    print("\n" + "Check if the priority queue is empty after dequeueing the whole priority queue:", is_empty(q))

def test_2():
    """test_2 tests if the dequeue, front and back functions raise exceptions on empty queues
        q: the priority queue
    """

    print("\n"+"Start Test 2:")
    print("Make empty queue:")
    q = make_priority_queue()
    print("Is queue empty?", is_empty(q))
    print("\n"+"Test if dequeue, front, and back functions on empty queues raises exceptions")
    print("Front function:", end=' ')
    try:
        front(q)
        print("False")
    except:
        print("True")
    print("Back function:", end=' ')
    try:
        back(q)
        print("False")
    except:
        print("True")
    print("Dequeue function:", end=' ')
    try:
        dequeue(q)
        print("False")
    except:
        print("True")
    print("\n"+"Add tasks and test if the exception gets raised again:")
    enqueue(q, make_task("t",5))
    print("Is queue empty?", is_empty(q))
    print("\n"+"Test if dequeue, front and back functions on not empty queues raises exceptions")
    print("Front function:", end=' ')

    try:
        front(q)
        print("False")
    except:
        print("True")
    print("Back function:", end=' ')

    try:
        back(q)
        print("False")
    except:
        print("True")
    print("Dequeue function:", end=' ')
    try:
        dequeue(q)
        print("False")
    except:
        print("True")
def main():
    test_1()
    test_2()

if __name__ == "__main__":
    main()
