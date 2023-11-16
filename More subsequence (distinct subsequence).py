from itertools import combinations

def count_distinct_subsequences(s):
    subsequences = set()
    for length in range(1, len(s) + 1):
        for combo in combinations(s, length):
            subsequences.add(''.join(combo))
    return len(subsequences)

def more_distinct_subsequences(A, B):
    distinct_subsequences_A = count_distinct_subsequences(A)
    distinct_subsequences_B = count_distinct_subsequences(B)
    
    if distinct_subsequences_A >= distinct_subsequences_B:
        return A
    else:
        return B

# Example usage:
string_A = "ab"
string_B = "dd"
result = more_distinct_subsequences(string_A, string_B)
print(f"The string with more distinct subsequences is: {result}")
