def letterCombinations(digits):
    if not digits:
        return []

    # Define the mapping of digits to letters
    digit_mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def backtrack(index, current_combination):
        # If the current combination is of the same length as digits, add it to the result
        if index == len(digits):
            result.append(current_combination)
            return

        # Get the letters corresponding to the current digit
        current_digit = digits[index]
        letters = digit_mapping[current_digit]

        # Iterate over each letter and recursively generate combinations
        for letter in letters:
            backtrack(index + 1, current_combination + letter)

    result = []
    backtrack(0, '')
    return result

# Example usage
digits = "23"
output = letterCombinations(digits)
print(output)
