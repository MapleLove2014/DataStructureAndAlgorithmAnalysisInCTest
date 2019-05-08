from linked_list import LinkedList
from matplotlib import pyplot as plt
from collections import OrderedDict
# UNIT = (1 << 10) - 1
# MASK = UNIT

BITS = 3
UNIT = 1000

def exponent(base, exponents):
    if exponents == 0:
        one = LinkedList()
        one.add_to_last(1)
        return one
    if exponents == 1:
        return base
    if exponents % 2 == 0:
        return exponent(multiply(base, base), exponents >> 1)
    else:
        return multiply(exponent(multiply(base, base), exponents >> 1), base)


def multiply(data1, data2):
    if not data1 or not data2:
        return None
    data3 = LinkedList()
    middle_result = [0] * (len(data1) + len(data2))
    i = 0
    for d1 in data1:
        j = 0
        for d2 in data2:
            product = d1 * d2
            middle_result[i+j] += product
            j += 1
        i += 1

    for i in range(len(middle_result)):
        product = middle_result[i]
        if product < UNIT:
            data3.add_to_last(product)
        else:
            low_value = product % UNIT
            data3.add_to_last(low_value)
            high_value = product // UNIT
            middle_result[i+1] += high_value
    return data3


def transform(value):
    data = LinkedList()
    while True:
        if value < UNIT:
            data.add_to_last(value)
            break
        else:
            low_value = value % UNIT
            data.add_to_last(low_value)
            value = value // UNIT
    return data

def get_str_result(data):
    data = [d for d in data]
    zeros = 0
    for i in range(len(data) - 1, -1, -1):
        if data[i] != 0:
            break
        zeros += 1
    actual_len = len(data) - zeros
    data_str = []
    for i in range(actual_len):
        unit_str = str(data[i])
        data_str.append(unit_str)
        j = len(unit_str)
        if i < actual_len - 1:
            while j < BITS:
                data_str.append('0')
                j += 1
            data_str.append(',')
    return ''.join(map(str, data_str[::-1]))

def test():
    result = exponent(transform(2), 5000)
    str_result = get_str_result(result)
    statistics = {}
    for s in str_result:
        if s == ',':
            continue
        if s not in statistics:
            statistics[s] = 0
        statistics[s] += 1
    
    odict = OrderedDict(sorted(statistics.items(), key=lambda e : int(e[0])))

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = odict.keys()
    sizes = odict.values()

    #explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    fig1.savefig('test.png')

test()