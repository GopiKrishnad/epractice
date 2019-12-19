"""
Given two stings, write a method to decide if one is permutation of other.
"""
# we can solve this problem in two ways sort the string and compare characters or check string
# has identical character count.


def perm(s, t):
    if len(s) != len(t):
        return False
    return ''.join(sorted(s)) == ''.join(sorted(q))


def perm(s, t):
    if len(s) != len(t):
        return False
    char_set = [0] * 128  # Assume all are ASCII characters.
    for i in s:
        char_set[ord(i)] += 1
    for j in t:
        char_set[ord(j)] -= 1
        if char_set[ord(j)] < 0:
            return False
    return True


if __name__ == '__main__':
    assert perm('ABC', 'CAB')
    assert not perm('ABCD', 'CAB')
