def reverse_string(s: str) -> str:
    """Reverses the input string."""
    return s[::-1]

def count_vowels(s: str) -> int:
    """Counts the number of vowels in the input string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
