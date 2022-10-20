"""
CSCI-141 Computer Science 1 Presentation Code
11-StacksQueues
Queues

This is the definition of a Queue structure and its supporting routines.
"""

from node import *

@dataclass
class Queue:
    size: int                       # number of elements in the queue
    front: Union[None, Node]        # the front element in the queue
    back: Union[None, Node]         # the back element in the queue

def mk_empty_queue():
    """
    Create and return a new empty queue.
    :return: a new queue with size initialized to zero and the front and back fields
    initialized to None (empty)
    """
    return Queue(0, None, None)

def enqueue(queue, element):
    """
    Insert a new element into the back of the queue.
    :param queue: the queue
    :param element: the new element
    :return None
    """
    new_node = Node(element, None)

    if empty_queue(queue):
        queue.front = new_node
    else:
        queue.back.next = new_node

    queue.back = new_node
    queue.size = queue.size + 1

def dequeue(queue):
    """
    Remove the front element from the queue.
    :pre: the queue is not empty
    :param: queue: the queue
    :return: None
    """
    if empty_queue(queue):
        raise IndexError('dequeue on empty queue')

    queue.front = queue.front.next
    if empty_queue(queue):
        queue.back = None

    queue.size = queue.size - 1

def front(queue):
    """
    Access and return the first element in the queue without removing it.
    :pre: the queue is not empty
    :param: queue: the queue
    :return front node
    """
    if empty_queue(queue):
        raise IndexError('front on empty queue')

    return queue.front.value

def back(queue):
    """
    Access and return the last element in the queue without removing it.
    :pre: the queue is not empty
    :param: queue: the queue
    :return back node
    """
    if empty_queue(queue):
        raise IndexError('back on empty queue')

    return queue.back.value

def empty_queue(queue):
    """
    Is the queue empty?
    :return whether the queue is empty or not
    """
    return queue.front == None

def size(queue):
    """
    How many elements are currently in the stack?
    :param queue: the queue
    :return: the size of the queue
    """
    return queue.size

def main():
    """ The main routine tests the queue data structure. """
    # begin with an empty queue
    queue_str = mk_empty_queue()
    print('Creating empty queue...')
    print('Queue empty?', True == empty_queue(queue_str))
    print('Queue size is 0?', 0 == queue_str.size)

    # add first element
    print('enqueue A...')
    enqueue(queue_str, 'A')
    print('Queue not empty?', False == empty_queue(queue_str))
    print('Queue size is 1?', 1 == queue_str.size)
    print('front is A?', 'A' == front(queue_str))
    print('back is A?', 'A' == back(queue_str))

    # add second element
    print('enqueue B...')
    enqueue(queue_str, 'B')
    print('front is A?', 'A' == front(queue_str))
    print('back is B?', 'B' == back(queue_str))

    # add third element
    print('enqueue C...')
    enqueue(queue_str, 'C')
    print('Queue size is 3?', 3 == size(queue_str))
    print('front is A?', 'A' == front(queue_str))
    print('back is C?', 'C' == back(queue_str))

    # dequeue front element, A
    print('dequeue...')
    dequeue(queue_str)
    print('Queue not empty?', False == empty_queue(queue_str))
    print('Queue size is 2?', 2 == size(queue_str))
    print('front is B?', 'B' == front(queue_str))
    print('back is C?', 'C' == back(queue_str))

    # add fourth element
    print('enqueue D...')
    enqueue(queue_str, 'D')
    print('front is B?', 'B' == front(queue_str))
    print('back is D?', 'D' == back(queue_str))

    # Empty the queue
    print('Emptying the queue...')
    while not empty_queue(queue_str):
        print('Front of stack:', front(queue_str))
        print('Back of stack:', back(queue_str))
        print('dequeue...')
        dequeue(queue_str)

if __name__ == '__main__':
    main()


q = mk_empty_queue()
enqueue(q, 'A')
enqueue(q, 'B')
enqueue(q, 'C')
