def count_sort(data, exp, n, buckets):
    count_arr = [0] * buckets
    output_arr = [0] * n
    for d in data:
        count_arr[ (d // exp) % buckets] += 1
    
    for i in range(1, buckets):
        count_arr[i] += count_arr[i - 1]
    
    for i in range(n-1, -1, -1):
        # make sure the sort is stable
        digit = (data[i] // exp) % buckets
        output_arr[count_arr[digit] - 1] = data[i]
        count_arr[digit] -= 1
    
    for i in range(n):
        data[i] = output_arr[i]

def lsf_radix_sort(data, buckets):
    """Least Significant First radix sort
    """
    exp = 1
    max_data = max(data)
    while True:
        if max_data // exp <= 0:
            break
        count_sort(data, exp, len(data), buckets)
        exp *= buckets

def count_sort_msf(data, start):
    n = len(data)
    if n <= 1:
        return data
    max_len = max([len(d) for d in data])
    if max_len <= start:
        return data

    count_len = ord('z') - ord('A') + 1
    count = [0] * count_len
    result = [''] * n
    result_index = 0
    for d in data:
        if len(d) <= start:
            result[result_index] = d
            result_index += 1
        else:
            count[ord(d[start].swapcase()) - ord('A')] += 1
    count[0] += result_index

    for i in range(1, count_len, 1):
        count[i] += count[i - 1]
    
    for i in range(n-1, -1, -1):
        if len(data[i]) <= start:
            continue
        count_index = ord(data[i][start].swapcase()) - ord('A')
        result[ count[count_index] -1 ] = data[i]
        count[count_index] -= 1
    return result
    

def msf_radix_sort(data, start):
    """Most Significant First radix sort
    """
    if len(data) <= 1 or start >= max(len(d) for d in data):
        return data

    result = count_sort_msf(data, start)

    merged_result = []
    group_char = ''
    group_arr = []

    for d in result:
        if start >= len(d):
            merged_result.append(d)
            continue
        if group_char != d[start]:
            for group_sort in msf_radix_sort(group_arr, start + 1):
                merged_result.append(group_sort)
            group_arr = []
            group_char = d[start]
        group_arr.append(d)    
    
    for group_sort in msf_radix_sort(group_arr, start + 1):
        merged_result.append(group_sort)
    return merged_result

def main():
    data = [1700, 42345, 712345, 920, 802, 243423, 23, 6236]
    lsf_radix_sort(data, 1000)
    print(','.join(map(str, data)))

    data = ['wawk', 'walk', 'hello', 'world', 'this', 'how', 'awake']
    data = msf_radix_sort(data, 0)
    print(','.join(data))

if __name__ == '__main__':
    main()
