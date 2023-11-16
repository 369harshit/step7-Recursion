def addOperators(num, target):
    def backtrack(start, expression, current_val, last_val):
        if start == len(num):
            if current_val == target:
                result.append(expression)
            return

        for end in range(start + 1, len(num) + 1):
            current_str = num[start:end]
            current_num = int(current_str)

            if start == 0:
                backtrack(end, current_str, current_num, current_num)
            else:
                backtrack(end, expression + '+' + current_str, current_val + current_num, current_num)
                backtrack(end, expression + '-' + current_str, current_val - current_num, -current_num)
                backtrack(end, expression + '*' + current_str, current_val - last_val + last_val * current_num, last_val * current_num)

            if current_num == 0:
                break

    result = []
    backtrack(0, '', 0, 0)
    return result

# Example usage:
num = "123"
target = 6
print(addOperators(num, target))
