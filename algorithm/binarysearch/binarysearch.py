# Binary search algorithm to find an element in a sorted array.
# We can implement binary search algorithm only when list is sorted.
# Let find an element in array

def binary_search(a, key):
    #  find mid element and compare it with key
    s = 0
    e = len(a) - 1
    while s <= e:
        mid = (s + e) // 2
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            s = mid + 1
        else:
            e = mid - 1
    return -1
print(binary_search([1,2,3,4,5], 5))