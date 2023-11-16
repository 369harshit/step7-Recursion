def sort_stack(stack):
    if not stack:
        return stack

    # Pop the top element from the original stack
    temp = stack.pop()

    # Recursively sort the remaining elements in the original stack
    sort_stack(stack)

    # Insert the popped element in the correct position in the original stack
    insert_in_sorted_order(stack, temp)

def insert_in_sorted_order(stack, element):
    # Base case: If the stack is empty or the element is smaller than the top element
    if not stack or element > stack[-1]:
        stack.append(element)
    else:
        # Pop elements from the stack until we find the correct position for the element
        temp = stack.pop()
        insert_in_sorted_order(stack, element)
        stack.append(temp)

# Example usage:
stack = [5, 2, 9, 1, 5, 6]
sort_stack(stack)
print(stack)  # Output: [1, 2, 5, 5, 6, 9]
