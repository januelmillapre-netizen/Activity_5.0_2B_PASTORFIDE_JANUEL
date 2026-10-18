
# test_driver.py

from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def test_stack(stack, name):
    print("\nTesting", name)

    try:
        stack.pop()
    except IndexError as error:
        print("Underflow test:", error)

    if isinstance(stack, ArrayStack):
        for item in [10, 20]:
            stack.push(item)

        try:
            stack.push(30)
        except OverflowError as error:
            print("Overflow test:", error)
    else:
        stack.push(10)
        stack.push(20)

    print("Top:", stack.peek())
    print("Removed:", stack.pop())
    print("State:", stack)


def test_queue(queue, name):
    print("\nTesting", name)

    try:
        queue.dequeue()
    except IndexError as error:
        print("Underflow test:", error)

    if isinstance(queue, ArrayQueue):
        queue.enqueue(10)
        queue.enqueue(20)
        queue.dequeue()
        queue.enqueue(30)
        queue.enqueue(40)

        print("Wrap-around test:", queue)

        try:
            queue.enqueue(50)
        except OverflowError as error:
            print("Overflow test:", error)

    else:
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

    print("Front:", queue.peek_front())
    print("Removed:", queue.dequeue())
    print("State:", queue)


test_stack(ArrayStack(2), "Array Stack")
test_stack(LinkedStack(), "Linked Stack")
test_queue(ArrayQueue(3), "Circular Array Queue")
test_queue(LinkedQueue(), "Linked Queue")
