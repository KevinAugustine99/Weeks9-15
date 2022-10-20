from dataclasses import dataclass
from operator import attrgetter

@dataclass
class Box:
    """Box is an object for boxes with 4 values
        ID: An integer to identify the box
        contents: A list of objects. the objects are the items that go into the box
        capacity: an integer for the total space in the box
        space_left: an integer for the amount of space left in the box
    """
    ID: int
    contents: list
    capacity: int
    space_left: int

@dataclass
class Items:
    """Items is an object for the items with 3 values
        name: a string for the name of the item
        weight: an integer for the weight of the item
        packed: a boolean for whether the item was packed or not
    """
    name: str
    weight: int
    packed: bool

def get_objects(input_file):
    """get_objects reads the input file and returns a list of box objects and a list of item objects
        input_file: the name of the text file to read
        boxes: a list of box objects
        items: a list of items objects
        box: a list of the weights of the boxes in the first line
        count: the ID for the box
        weight_box: each weight for each box
        line: each line in the text file after the first one
        items_list: a list for each line with two values, the first value is the name of the item, and the second value is its weight
    """
    boxes = []
    items = []
    text_file = open(input_file)
    box = text_file.readline().strip().split()
    count = 1
    for weight_box in box:
        #Iterates over each box and makes a box object for each box
        boxes.append(Box(count, [], int(weight_box), int(weight_box)))
        count += 1
    for line in text_file:
        #Iterates over each line after the first one and makes an item object for each item
        items_list = line.strip().split()
        items.append(Items(items_list[0],int(items_list[1]),False))
    text_file.close()
    return (boxes, items)

def print_contents(sorted_boxes, items_left_behind):
    """print_contents prints the boxes and all of its contents
        sorted_boxes: the list of boxes with all of the contents in it, sorted by ID
        items_left_behind: the list of all of the items left behind
        box: each box in sorted_boxes
        item: each item in items_left_behind
    """
    if len(items_left_behind) == 0:
        #If there are no items left behind
        print("All items successfully packed into boxes!")
    else:
        #If there are items left behind
        print("Unable to pack all items!")
    for box in sorted_boxes:
        #Iterates through each box and prints the box and its capacity
        print("Box ",box.ID," of weight capacity ", box.capacity, " contains:", sep ='')
        for item in box.contents:
            #Iterates through each item in the box and prints its name and weight
            print("   ",item.name, " of weight ", item.weight, sep='')
    if len(items_left_behind) != 0:
        #If there are items left behind
        for item in items_left_behind:
            #Iterates through each item left behind and prints its name and weight
            print(item.name, " of weight ", item.weight, " got left behind.", sep='')

def strategy1(boxes, items):
    """strategy1 organizes the items into the boxes using greedy strategy 1 (puts the items in the box with the most amount of space left)
        boxes: a list of box objects
        items: a list of items objects
        sorted_boxes: the list of box objects sorted in decreasing order by space_left
        sorted_items: the list of item objects sorted in decreasing order by weight
        items_left_behind: the list of all of the items left behind
        item: each item object in sorted_items
        box: each box object in sorted_boxes
        sorted_boxes2: the list of box objects sorted in increasing order by ID
    """
    sorted_boxes = sorted(boxes, key=attrgetter('space_left'), reverse = True)
    sorted_items = sorted(items, key=attrgetter('weight'), reverse = True)
    items_left_behind = []
    for item in sorted_items:
        #Iterates through each item in sorted_items
        for box in sorted_boxes:
            #Iterates through each box
            if item.weight <= box.space_left:
                #If the item can fit in the box then it goes into the box
                box.space_left = box.space_left - item.weight
                box.contents.append(item)
                item.packed = True
                break               
        sorted_boxes = sorted(sorted_boxes, key=attrgetter('space_left'), reverse = True)
    sorted_boxes2 = sorted(sorted_boxes, key=attrgetter('ID'))
    if not item.packed:
        #If the item is not packed then it goes into into the items_left_behind list
        items_left_behind.append(item) 

    print("Resuslts from Greedy Strategy 1")
    print_contents(sorted_boxes2, items_left_behind)

def strategy2(boxes,items):
    """strategy2 organizes the items into the boxes using greedy strategy 2 (puts the items in the box with the least amount of space left)
        boxes: a list of box objects
        items: a list of items objects
        sorted_boxes: the list of box objects sorted in increasing order by space_left
        sorted_items: the list of item objects sorted in decreasing order by weight
        items_left_behind: the list of all of the item objects left behind
        item: each item object in sorted_items
        box: each box object in sorted_boxes
        sorted_boxes2: the list of box objects sorted in increasing order by ID
    """
    sorted_boxes = sorted(boxes, key=attrgetter('space_left'))
    sorted_items = sorted(items, key=attrgetter('weight'), reverse = True)
    items_left_behind = []
    
    for item in sorted_items:
        #Iterates through each item in sorted_items
        for box in sorted_boxes:
            #Iterates through each box
            if item.weight <= box.space_left:
                #If the item can fit in the box then it goes into the box
                box.space_left = box.space_left - item.weight
                box.contents.append(item)
                item.packed = True
                break               
        sorted_boxes = sorted(sorted_boxes, key=attrgetter('space_left'))
    sorted_boxes2 = sorted(sorted_boxes, key=attrgetter('ID'))
    if not item.packed:
        #If the item is not packed then it goes into into the items_left_behind list
        items_left_behind.append(item) 

    print("Resuslts from Greedy Strategy 2")
    print_contents(sorted_boxes2, items_left_behind)

def strategy3(boxes,items):
    """strategy3 organizes the items into the boxes using greedy strategy 3 (iterating over each box and fit all the items that can fit in it)
        boxes: a list of box objects
        items: a list of items objects
        sorted_items: the list of item objects sorted in decreasing order by weight
        items_left_behind: the list of all of the item objects left behind
        item: each item object in sorted_items
        box: each box object in boxes
        sorted_boxes2: the list of box objects sorted in increasing order by ID
    """
    sorted_items = sorted(items, key=attrgetter('weight'), reverse = True)
    items_left_behind = []
    for box in boxes:
        #Iterates through each box object
        for item in sorted_items:
            #Iterates through each item in sorted_items
            if item.packed is False:
                #If the item is not already packed
                if item.weight <= box.space_left:
                    #If the item can fit in the box then it goes into the box
                    box.space_left = box.space_left - item.weight
                    box.contents.append(item)
                    item.packed = True
    sorted_boxes2 = sorted(boxes, key=attrgetter('ID'))
    if not item.packed:
        #If the item is not packed then it goes into into the items_left_behind list
        items_left_behind.append(item) 
    print("Resuslts from Greedy Strategy 3")
    print_contents(sorted_boxes2, items_left_behind)

def main():
    text_file = input("Enter data filename: ")
    for func in [strategy1, strategy2, strategy3]:
        #Iterates through each function
        print("\n")    
        (boxes, items) = get_objects(text_file)
        func(boxes, items)

if __name__ == "__main__":
    main()