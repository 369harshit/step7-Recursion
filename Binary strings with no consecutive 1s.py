def generate_no_consecutive_ones(n):
    def generate_binary_strings(s):
        if len(s) == n:
            result.append(s)
            return
        if s[-1] == '1':
            generate_binary_strings(s + '0')
        else:
            
            generate_binary_strings(s + '0')
            generate_binary_strings(s + '1')

    result = []
    generate_binary_strings('0')
    generate_binary_strings('1')
    return result

# Example usage:
n = 3
result = generate_no_consecutive_ones(n)
print(result)
