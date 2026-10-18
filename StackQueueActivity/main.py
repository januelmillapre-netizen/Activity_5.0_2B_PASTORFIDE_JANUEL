
# main.py

from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


# Application 1: Check balanced parentheses
def check_balanced(expression):
    stack = []
    matching = {")": "(", "]": "[", "}": "{"}

    for character in expression:
        if character in "([{":
            stack.append(character)

        elif character in ")]}":
            if len(stack) == 0:
                return False

            if stack.pop() != matching[character]:
                return False

    return len(stack) == 0


# Application 2: Simulate a print queue
def print_queue():
    jobs = []
    next_id = 1

    while True:
        print("\n1. Add print job")
        print("2. Print next job")
        print("3. View waiting jobs")
        print("0. Return to main menu")

        choice = input("Choose: ")

        if choice == "1":
            try:
                pages = int(input("Number of pages: "))

                if pages <= 0:
                    print("Pages must be greater than zero.")
                    continue

                job = {"id": next_id, "pages": pages}
                jobs.append(job)
                print("Job added:", job)
                next_id += 1

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            if len(jobs) == 0:
                print("Print queue underflow: no jobs waiting.")
            else:
                job = jobs.pop(0)
                print("Printing job", job["id"],
                      "-", job["pages"], "pages")

                if len(jobs) > 0:
                    print("Next job in waiting order:", jobs[0]["id"])
                else:
                    print("No more jobs waiting.")

        elif choice == "3":
            print("Waiting jobs:", jobs)

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


# Select a data structure
def select_structure(choice):
    if choice == "1":
        return ArrayStack(3)
    elif choice == "2":
        return LinkedStack()
    elif choice == "3":
        return ArrayQueue(3)
    elif choice == "4":
        return LinkedQueue()
    else:
        return None


# Main menu
def main():
    while True:
        print("\n===== STACK AND QUEUE MENU =====")
        print("1. Array Stack")
        print("2. Linked Stack")
        print("3. Circular Array Queue")
        print("4. Linked Queue")
        print("5. Check Balanced Parentheses")
        print("6. Print Queue Application")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "0":
            print("Program ended.")
            break

        elif choice == "5":
            expression = input("Enter parentheses: ")
            if check_balanced(expression):
                print("The parentheses are balanced.")
            else:
                print("The parentheses are NOT balanced.")
            continue

        elif choice == "6":
            print_queue()
            continue

        structure = select_structure(choice)

        if structure is None:
            print("Invalid choice.")
            continue

        while True:
            print("\nCurrent structure:", structure)

            if choice in ("1", "2"):
                print("1. Push")
                print("2. Pop")
                print("3. Peek")
            else:
                print("1. Enqueue")
                print("2. Dequeue")
                print("3. Peek front")

            print("4. Check empty")
            print("5. Check full")
            print("0. Return to main menu")

            operation = input("Choose an operation: ")

            try:
                if operation == "0":
                    break

                elif operation == "1":
                    item = input("Enter item: ")

                    if choice in ("1", "3"):
                        # Use numbers for the array implementations
                        item = int(item)

                    if choice in ("1", "2"):
                        structure.push(item)
                    else:
                        structure.enqueue(item)

                elif operation == "2":
                    if choice in ("1", "2"):
                        print("Removed:", structure.pop())
                    else:
                        print("Removed:", structure.dequeue())

                elif operation == "3":
                    if choice in ("1", "2"):
                        print("Top item:", structure.peek())
                    else:
                        print("Front item:", structure.peek_front())

                elif operation == "4":
                    print("Is empty:", structure.is_empty())

                elif operation == "5":
                    print("Is full:", structure.is_full())

                else:
                    print("Invalid operation.")

            except (IndexError, OverflowError, ValueError) as error:
                print("Error:", error)

            print("Structure after operation:", structure)


if __name__ == "__main__":
    main()
