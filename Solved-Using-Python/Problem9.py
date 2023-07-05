# Problem Statement: Check if a given string is a palindrome using recursion.

def is_palindrome(s, i):
    """
    This function recursively checks if a given string is a palindrome.

    Args:
    - s: The input string to check for palindrome.
    - i: The current index being compared in the recursion.

    Returns:
    - True if the string is a palindrome.
    - False if the string is not a palindrome.

    """
    n = len(s)
    if i >= n // 2:
        # Base case: If the current index is greater than or equal to half the length of the string,
        # we have compared all corresponding characters and the string is a palindrome.
        return True
    
    if s[i] != s[n - i - 1]:
        # If the characters at the current index and its corresponding index from the end are not equal,
        # the string is not a palindrome.
        return False
    
    # Recursively call the function with the next index to continue comparing the remaining characters.
    return is_palindrome(s, i + 1)

# Test the function with a sample string.
string = "madam"
result = is_palindrome(string, 0)
print(result)
