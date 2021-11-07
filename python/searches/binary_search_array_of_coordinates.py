# takes an array of coordinate tuples and a coordinate tuple
# searches array with a binary search for a matching coordinate tuple
# returns coordinate of location, -1 if fails
def binary_coord_search(arr, coord):
    low=0
    high=len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == coord:
            return mid
        if arr[mid][0] > coord[0]:
            high = mid - 1
            continue
        if arr[mid][0] < coord[0]:
            low = mid + 1
            continue
        if arr[mid][1] > coord[1]:
            high = mid - 1
            continue
        if arr[mid][1] < coord[1]:
            low = mid + 1
            continue

    return -1



# Example code to show how it works

import random

rArr = []

# an array of coordinate tuples of random values
MIN_MAX=1000
for i in range(MIN_MAX):
    rArr.append((random.randint(-MIN_MAX, MIN_MAX),random.randint(-MIN_MAX, MIN_MAX)))

# all binary searches must be order. First order on x coord, then y
rArr=list(sorted(rArr, key=lambda x:(x[0], x[1])))

# Tests that show it works
for i in range(10):
    expected = rArr[random.randint(0,MIN_MAX-1)]
    index = binary_coord_search(rArr, expected)
    print(expected == rArr[index])

# Failing tests
for i in range(MIN_MAX*1000):
    if (i,i) not in rArr: # cuz we know in keyword works. Keyword in is a shitty algorithm, but best for unsorted lists
        print(binary_coord_search(rArr, (i,i)))
        break
