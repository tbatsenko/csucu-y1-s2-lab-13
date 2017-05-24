from linkedstack import LinkedStack


def stack_to_queue(QueueObj):
    """ takes a queue and transformes it to stack"""
    stk = LinkedQueue()
    for el in QueueObj:
        stk.add(el)
    return stk
