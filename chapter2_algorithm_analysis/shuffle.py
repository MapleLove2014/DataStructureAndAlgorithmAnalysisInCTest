import random
import time

##################################### 2.7 #####################################

def rand_int(i, j):
    return random.randint(i, j)

def test2_7_1(N):
    A = [0] * N
    for i in range(N):
        while True:
            x = rand_int(0, N-1)
            flag = True
            for j in range(i):
                if A[j] == x:
                    flag = False
                    break
            if flag:
                A[i] = x
                break
    print(','.join(map(str, A[:10])))
 
def test2_7_2(N):
    A = [0] * N
    USED = [False] * N
    for i in range(N):
        while True:
            x = rand_int(0, N-1)
            if not USED[x]:
                A[i] = x
                break
    print(','.join(map(str, A[:10])))
    
def test2_7_3(N):
    A = [i for i in range(N)]

    for i in range(1, N):
        x = rand_int(0, i-1)
        temp = A[i]
        A[i] = A[x]
        A[x] = temp

    print(','.join(map(str, A[:10])))

def evaluate_time(id, Ns):
    eclipses = []
    for N in Ns:
        eclipse = 0
        for i in range(10):
            print('{:*^50}'.format('N:{},round{}'.format(N, i)))
            start = time.time()
            if id == 1:
                test2_7_1(N)
            elif id == 2:
                test2_7_2(N)
            else:
                test2_7_3(N)
            end = time.time()
            running = end - start
            eclipse += running
            print('{:*^50}'.format(running))
        eclipses.append(int(eclipse / 10))
        print('{:-^50}'.format(eclipses[-1]))
    print('{:+^50}'.format(','.join(map(str, eclipses))))
    return eclipses

def test_2_7():
    N1 = [3000, 4000, 5000, 10000]
    N2 = [600000, 1000000, 4000000, 8000000]
    eclipses = []
    eclipses.append(evaluate_time(1, N1))
    eclipses.append(evaluate_time(2, N2))
    eclipses.append(evaluate_time(3, N2))
    for eclipse in eclipses:
        print('running time:{}'.format(','.join(map(str, eclipse))))

def main():
    test_2_7()

if __name__ == '__main__':
    main()