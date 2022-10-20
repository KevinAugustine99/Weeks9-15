"""
File : priority_queue.py
Assignment : HW #11
Language : python3
Author : Kevin Augustine < kea4437@rit.edu >
"""
from node import *

@dataclass
class PriorityQueue:
    front: Union[None,Node]
    back: Union[None, Node]
    __slots__ = "size","front","back"

def make_priority_queue():
    """make_priority_queue creates and returns an empty priority queue
    """
    return PriorityQueue(None,None)

def enqueue(queue,element):
    """enqueue takes a task and puts it in the priority queue in order of priority
        queue: the priority queue
        element: the task being added into the priority queue
    """
    new_node = Node(element,None)
    if is_empty(queue):
        #If the priority queue is empty, then both the front and the back of the priority queue is the Task
        queue.front = new_node
        queue.back = new_node
    elif element.priority > queue.front.value.priority:
        #If the task's priority is higher than all of the other priorities, then it gets appended to the front of the priority queue
        new_node.next = queue.front
        queue.front = new_node
    elif element.priority <= queue.back.value.priority:
        #If the task's priority is lower than all of the other priorities, then it gets appended to the back of the priority queue
        queue.back.next = new_node
        queue.back = new_node
    else:
        #If the task's priority is in between the front's priority and the back's priority, then it gets appended to the middle of the priority queue in the right spot of decreasing priority
        queue.front.next = insert_element_node(element,queue.front.next)

def insert_element_node(element,node):
    """insert_element_node inserts the Task in the right spot in the rest of the node
        element: the Task being inserted into the node
        node: the node that the program is inserting the task into
    """
    if element.priority > node.value.priority:
        #If the element is in the right spot (the priority is higher than the value's priority), then it creates and returns a Node with the value being the element and the rest of the node being the node itself
        return Node(element,node)
    else:
        #If the element isn't in the right spot, then it creates and returns a Node with the value being the node's value, and the rest recursively calling itself with the element staying the same but the new node is the rest of the node
        return Node(node.value,insert_element_node(element,node.next))

def dequeue(queue):
    """dequeue takes the Task with the highest element out of the priority queue
        queue: the priority queue
    """
    if is_empty(queue):
        #If the priority queue is empty then raise exception
        raise IndexError('dequeue on empty queue')

    queue.front = queue.front.next    

    if is_empty(queue):
        #If the priority queue after taking the Task out then set the back to None
        queue.back = None

def front(queue):
    """front returns the Task with the highest priority
        queue: the priority queue
    """
    if is_empty(queue):
        #If the priority queue is empty then raise exception
        raise IndexError('front on empty queue')
    return queue.front.value

def back(queue):
    """back returns the Task with the lowest priority
        queue: the priority queue
    """
    if is_empty(queue):
        #If the priority queue is empty then raise exception
            raise IndexError('front on empty queue')
    return queue.back.value

def is_empty(queue):
    """is_empty returns True if the priority queue is empty. If not then return False.
        queue: the priority queue
    """
    return queue.front == None

