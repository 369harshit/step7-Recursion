def find_combinations(k, n):
    result = []
    def backtrack(start, k, n, path):
        if k == 0 and n == 0:
            result.append(path)
            return
        for i in range(start, 10):
            if i > n:
                break
            backtrack(i+1, k-1, n-i, path + [i])

    backtrack(1, k, n, [])
    return result

# Example usage
k = 3
n = 7
output = find_combinations(k, n)
print(output)
