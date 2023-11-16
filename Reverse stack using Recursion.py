class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

def reverse_stack(stack):
    if not stack.is_empty():
        # Pop the top element from the original stack
        top = stack.pop()
        # Recursively reverse the rest of the stack
        reverse_stack(stack)
        # Insert the popped element at the bottom of the stack
        insert_at_bottom(stack, top)

def insert_at_bottom(stack, item):
    if stack.is_empty():
        stack.push(item)
    else:
        # Recursively insert the item at the bottom of the stack
        top = stack.pop()
        insert_at_bottom(stack, item)
        stack.push(top)

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Original Stack:", stack.items)
reverse_stack(stack)
print("Reversed Stack:", stack.items)
