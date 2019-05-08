from linked_list import LinkedList, Node
import random

def solve1(m, n):
    testers = LinkedList()
    testers.add_pure_values_to_last(range(1, n+1))
    while len(testers) > 1:
        next_kill = testers.remove(m % len(testers))
        testers.reset_head(next_kill.next)
    return testers.get(0)
    
def solve2(m, n):
    if n == 1:
        return 0
    winner = (m + 1 + solve2(m, n-1)) % n
    return winner

def test():
    count = 100
    while count > 0:
        m = random.randint(1, 1000)
        n = random.randint(1, 1000)
        count -= 1
        s1 = solve1(3, 5)
        s2 = solve2(3, 5) + 1
        print(s1.value == s2)
test()
