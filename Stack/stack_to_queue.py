from linkedqueue import LinkedQueue

def stack_to_queue(StackObj):
    """ takes a stack and transformes it to queue"""
    queue = LinkedQueue()
    for el in StackObj:
        queue.add(el)
    return queue
