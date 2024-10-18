import itertools

# itertools.product() generates all possible combinations by taking one element from each list


def maximize(K, M, lists):
    """Define maximize function that takes three inputs:
    K - the number of lists.
    M - the modulo value
    lists - list of list, each inner list contains the integers we will choose from."""

    # Generate all possible combinations of one element from each list
    all_combinations = itertools.product(*lists)

    # Initialize the maximum value of S to 0 (S is the sum of squares modulo M)
    max_value = 0

    # Iterate over all combinations
    for combination in all_combinations:
        # Calculate the sum of squares for the current combination
        S = sum(x**2 for x in combination) % M

        # Update the maximum value if the current one is greater
        max_value = max(max_value, S)

    return max_value


def main():
    """Main function to handle input and output"""


# We read two integers, K (number of lists) and M (modulo value)
K, M = map(int, input().split())

# For each list we split the input and ignore the first value
lists = [list(map(int, input().split()[1:])) for _ in range(K)]

# Call the maximize function with the input values
result = maximize(K, M, lists)
print(result)

if __name__ == "__main__":
    main()
