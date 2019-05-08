import random
import numpy as np
from collections import Counter

def brute_force(data):
    majority = len(data) // 2
    for d in data:
        count = sum(1 for dd in data if dd == d)
        if count > majority:
            return d
    return None

def hash_map(data):
    counter = Counter(data)
    d, count = counter.most_common(1)[0]
    return d if count > len(data) // 2 else None

def sorting(data):
    data.sort()
    mid = data[len(data) // 2]
    return mid if sum(1 for dd in data if dd == mid) else None

def randomization(data):
    while(True):
        candidate = data[random.randint(0, len(data)-1)]
        if sum(1 for dd in data if dd == candidate) > len(data) // 2:
            return candidate

def divide_conquer(data, low, high):
    if high < low:
        return None
    if low == high:
        return data[low]
    if high - low + 1 == 2:
        return data[low] if data[low] == data[high] else None
    mid = low + (high - low + 1) // 2
    m1 = divide_conquer(data, low, mid)
    m2 = divide_conquer(data, mid + 1, high)
    if m1 == m2:
        return m1
    else:
        m1_count = sum(1 for dd in data if dd == m1)
        m2_count = sum(1 for dd in data if dd == m2)
        gold = len(data) // 2
        if m1_count > gold:
            return m1
        elif m2_count > gold:
            return m2
        else:
            return None

def divide_conquer_list(data):
    if len(data) == 1:
        return data[0]
    odd = None
    gold = len(data) // 2
    if len(data) % 2 != 0:
        odd = data.pop()
    new_data = []
    previous = None
    for d in data:
        if previous == None:
            previous = d
        elif d == previous:
            new_data.append(d)
            previous = None
        else:
            previous = None
    major = divide_conquer_list(new_data)
    if odd == None:
        return major
    else:
        if major == None:
            return odd if sum(1 for d in data if odd == d) + 1 > gold else None
        else:
            return major
    

def boye_moore_vote(data):
    count = 0
    element = None
    for d in data:
        if count == 0:
            element = d
        if element == d:
            count += 1
        else:
            count -= 1
    return element if sum(1 for d in data if element == d) > len(data) // 2 else None

def test():
    n = 5005
    majority_element = random.randint(0, 100)
    print(majority_element)
    data = []
    for i in range(n):
        if i < n // 2 - 1:
            data.append(random.randint(0, 100))
        else:
            data.append(majority_element)

    np.random.shuffle(data)
    x = [
        brute_force(data),
        hash_map(data),
        sorting(data),
        randomization(data),
        divide_conquer(data, 0, len(data)-1),
        divide_conquer_list(data),
        boye_moore_vote(data)
    ]
    print(','.join(map(str, x)))

test()