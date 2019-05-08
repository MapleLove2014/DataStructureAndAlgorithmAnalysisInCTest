import sys
import numpy

def algorithm1(sequence):
    """
    running time O(N^3)
    """
    max_sum = 0
    for start in range(len(sequence)):
        for end in range(start, len(sequence)):
            sum = 0
            for i in range(start, end + 1):
                sum += sequence[i]
            if sum > max_sum:
                max_sum = sum
    return max_sum

def algorithm2(sequence):
    """
    running time O(N^2)
    """
    max_sum = 0
    for start in range(len(sequence)):
        sum = 0
        for end in range(start, len(sequence)):
            sum += sequence[end]
            if sum > max_sum:
                max_sum = sum
    return max_sum

def algorithm3(sequence):
    """
    running time O(nlogn)
    """
    # base case
    if len(sequence) == 1:
        return 0 if sequence[0] < 0 else sequence[0]
    # divide 
    mid = int(len(sequence) / 2)
    ## calculate the max subsequence of the left 
    left_max = algorithm3(sequence[0:mid])
    ## calculate the max subsequence of the right 
    right_max = algorithm3(sequence[mid:])
    ## calculate the max subsequence of the middle
    mid_max = 0
    left_part = 0
    right_part = 0
    sum = 0
    for i in reversed(range(mid)):
        sum += sequence[i]
        if sum > left_part:
            left_part = sum

    sum = 0
    for j in range(mid, len(sequence)):
        sum += sequence[j]
        if sum > right_part:
            right_part = sum 
    mid_max = left_part + right_part
    
    # conquer
    return sorted([left_max, mid_max, right_max]).pop()

def algorithm4(sequence):
    """
    running time O(n)
    """
    max_sum = 0
    sum = 0
    for i in range(len(sequence)):
        sum += sequence[i]
        # sub sequence pasted contributes nothing to the new max sum if exists
        if sum < 0:
            sum = 0
        elif sum > max_sum:
            max_sum = sum
    return max_sum

def minimum_subsequence(sequence):
    """
    running time O(n)
    Another trick is : minimum_subsequence = - maximumu_subsequence of -sequence.
    The generate point is to find the max absolute maximum subsequence.
    """
    min_sum = 0
    sum = 0
    for seq in sequence:
        sum += seq
        if sum < min_sum:
            min_sum = sum
        elif sum > 0:
            sum = 0
    return min_sum

def minimum_positive_subsequence(sequence):
    pass

def maximum_subsequence_product(sequence):
    pass

def format_print(msg, align='^', placeholder='=', length=100):
    print(('{:' + placeholder + align + str(length) + '}').format(msg))

def main():
    sequence = numpy.random.randint(-100, 100, 500)
    numpy.random.shuffle(sequence)

    format_print('maximum subsequence', placeholder='+')
    format_print('n^3', placeholder='*')
    format_print(algorithm1(sequence))
    format_print('n^2', placeholder='*')
    format_print(algorithm2(sequence))
    format_print('nlogn', placeholder='*')
    format_print(algorithm3(sequence))
    format_print('n', placeholder='*')
    format_print(algorithm4(sequence))

    format_print('minimum subsequence')
    format_print(minimum_subsequence(sequence))
    format_print(-algorithm4([ -seq for seq in sequence]))

if __name__ == '__main__':
    main()