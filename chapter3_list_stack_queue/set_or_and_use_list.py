import numpy as np
import sys

s1 = np.sort(np.random.random_integers(1, 20, 10))
s2 = np.sort(np.random.random_integers(1, 20, 10))

def OR(s1, s2):
    result = []
    i = 0
    j = 0
    ss1 = None
    ss2 = None
    ss3 = None
    while True:
        if i < len(s1):
            ss1 = s1[i]
        if j < len(s2):
            ss2 = s2[j]

        if len(result) > 0:
            ss3 = result[-1]

        if ss1 < ss2:
            i += 1
            if not ss3 or ss3 < ss1:
                result.append(ss1)
        elif ss1 > ss2:
            j += 1
            if not ss3 or ss3 < ss2:
                result.append(ss2)
        else:
            i += 1
            j += 1
            if not ss3 or ss3 < ss1:
                result.append(ss1)

        if i == len(s1):
            ss1 = sys.maxsize
        if j == len(s2):
            ss2 = sys.maxsize
        if i==len(s1) and j == len(s2):
            break
    print('s1:{}'.format(','.join(map(str, s1))))
    print('s2:{}'.format(','.join(map(str, s2))))
    print('OR result')
    print(','.join(map(str, result)))

def AND(s1, s2):
    result = []
    i = 0
    j = 0
    ss1 = None
    ss2 = None
    ss3 = None
    while True:
        if i < len(s1):
            ss1 = s1[i]
        if j < len(s2):
            ss2 = s2[j]
        if len(result) > 0:
            ss3 = result[-1]

        if ss1 == ss2:
            i += 1
            j += 1
            if not ss3 or ss3 != ss1:
                result.append(ss1)
        elif ss1 < ss2:
            i += 1
        else:
            j += 1
        if i==len(s1) or j == len(s2):
            break
    print('s1:{}'.format(','.join(map(str, s1))))
    print('s2:{}'.format(','.join(map(str, s2))))
    print('AND result')
    print(','.join(map(str, result)))


OR(s1, s2)
AND(s1, s2)