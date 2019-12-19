"""
Implement an algorithm to determine if a string has all unique characters.What if you cannot use additional data structures?
"""


def isrepeatedcharacter(m):
    """
    We assume string accept only ASCII characters.
    O(n)
    """
    if len(m) > 128:  # Assume string has only ASCII characters
        return False
    char_set = [False] * 128
    for i in m:
        val = ord(i)  # value of the char
        if char_set[val]:  # If already found this character
            return False
        char_set[val] = True
    return True


if __name__ == "__main__":
    print(isrepeatedcharacter('ABCD'))

