def countGoodNumbers(n):
    MOD = 10**9 + 7

    # Count even and prime digits
    even_digits = [0, 2, 4, 6, 8]
    prime_digits = [2, 3, 5, 7]

    # Calculate choices for even and odd indices
    choices_even = pow(5, (n + 1) // 2, MOD)
    choices_odd = pow(4, n // 2, MOD)

    # Calculate total number of good digit strings
    total_choices = (choices_even * choices_odd) % MOD

    return total_choices

# Example
n = 1
output = countGoodNumbers(n)
print(output)
