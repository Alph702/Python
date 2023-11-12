def longest_palindromic_substring(s):
    """Finds the longest palindromic substring in the given string.

    Args:
        s: A string.

    Returns:
        The longest palindromic substring in the given string.
    """

    n = len(s)
    p = [[0 for _ in range(n)] for _ in range(n)]

    max_len = 0
    max_end = 0
    for i in range(n):
        for j in range(i, n):
            if i == j:
                p[i][j] = 1
            elif s[i] == s[j] and i + 1 == j:
                p[i][j] = 2
            elif s[i] == s[j] and p[i + 1][j - 1] > 0:
                p[i][j] = p[i + 1][j - 1] + 2
            else:
                p[i][j] = 0

            if p[i][j] > max_len:
                max_len = p[i][j]
                max_end = j

    start = max_end - max_len + 1
    return s[start:start + max_len]


if __name__ == "__main__":
    s = "babad"
    longest_palindrome = longest_palindromic_substring(s)
    print(longest_palindrome)
