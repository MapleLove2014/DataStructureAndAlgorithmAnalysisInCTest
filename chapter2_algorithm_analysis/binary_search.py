import numpy

def binary_search(sequence, target):
    print(','.join(map(str, sequence)))
    if len(sequence) == 1:
        return 0 if sequence[0] == target else -10000
    mid = len(sequence) // 2
    if sequence[mid] == target:
        return mid
    elif sequence[mid] > target:
        return binary_search(sequence[0:mid], target)
    else:
        return mid + 1 + binary_search(sequence[mid+1:], target)

def main():
    sequence = numpy.random.randint(0, 100, 20)
    sequence.sort()
    pos = numpy.random.randint(0, 20)
    print('{:-^100}'.format(pos))
    res = binary_search(sequence, sequence[pos])
    print('{:*^100}'.format(res))

if __name__ == '__main__':
    main()