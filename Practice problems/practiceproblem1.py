# practiceproblem1.py

# -------------------------------
# Problem 1 – Count Consonants
# -------------------------------
def count_consonants(s: str) -> int:
    """
    Returns the number of consonants in the string s.
    """
    z = 0
    for x in s:
        if x not in "aeiouAEIOU":
            z += 1
    return z


# -------------------------------
# Problem 2 – Sum Positive Integers
# -------------------------------
def sum_positive(lst: list) -> int:
    """
    Returns the sum of all positive integers in lst.
    """
    count = 0
    for x in lst:
        if x >= 0:
            count += x
    return count


# -------------------------------
# Problem 3 – Reverse String Without Vowels
# -------------------------------
def reverse_no_vowels(s: str) -> str:
    """
    Returns the string s reversed and with vowels removed.
    """
    z = ""
    for x in s:
        if x not in "aeiouAEIOU":
            z += x
    return z[::-1]


# -------------------------------
# Problem 4 – Letter Frequency
# -------------------------------
def letter_frequency(s: str) -> dict:
    freq = {}
    for char in s:
        if char in freq:
            freq[char] = freq[char] + 1
        else:
            freq[char] = 1
    return freq


# -------------------------------
# Problem 5 – Filter Odd Numbers
# -------------------------------
def filter_odd(lst: list) -> list:
    new = []
    for x in lst:
        if x % 2 == 1:
            new.append(x)
    return new

