# Find sqrt of a number by binary search algorithm
# if we need to find sqrt of 10 considering only precision or integer value only 3 will be the answer
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] any number less than or equal to 10 can form sqrt
# we pick mid point of above list and check if
# a[mid]* a[mid] == 10  if it is matching that is the answer
# if a[mid] < 10 then we may need to find sqrt in right half of the array
# if a[mid] > 10 then we need to find sqt in other side
# for above list mid element is : 11 // 2 = 5
# 5 * 5 = 25 > 10:
# newendpoint = mid -1 = 4
# s = 0
# newmid = (s+e)//2 = (0 +  4 ) //2 = 2
# 2 * 2 < 10
# integerpoint: 2
# newstartpoint = mid+1 = 2+1 3
# mid = newstartpoint+e = (3 + 4) //2 = 3
# 3 * 3 < 10
integerpoint:3

#newstartpoint = 3+1 = 4
#mid = 4+4//2 = 4
# 4 * 4 = 16
# then it means 4 doesnt work we need to choose above value 3.
# integerpoint is 3



def binary_search_sqrt(l):
    # first generate an array of indices
    a = list(range(l+1))
    #  find mid element and compare it with key
    s = 0
    e = len(a) - 1
    integerpoint = 0
    while s <= e:
        mid = (s + e) // 2
        if a[mid] * a[mid] == l:
            integerpoint = mid
            return a[mid]
        elif a[mid] * a[mid] < l:
            s = mid + 1
            integerpoint = mid
        else:
            e = mid - 1
    # to get 3 digits after decimal
    # add .1 to integerpoint and increment it till sqrt < 10
    # 3.1 = 3.1*3.1 < 10
    # 3.2 = 3.2 * 3.2 > 10
    # 3.1 will be in first place after decimal
    # it goes like this till .... 3.16 < 10 and 3.17 > 10
    # 3.121 = 3.121 * 3.121 < 10
    intpoint = 0.1
    t = integerpoint
    for i in range(3):
        while t * t < l:
            t = t + intpoint
        t = t - intpoint
        intpoint = intpoint/10
    print(t)
print(binary_search_sqrt(10))