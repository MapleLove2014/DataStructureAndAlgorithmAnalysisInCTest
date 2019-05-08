# O(n) complexity Josephus problem algorithm explained

1. First we assume **M** passes and **N** people starting from the first person with index 0.

    >  0, 1, 2, ---, M-1, M, M+1, ---, N-1

2. After **M** passes, the one at index **M** gets removed. And the game continues starting at index **M+1**. The **N-1** people form a new circle which can be treated as the same problem with **N-1** people compared with the first round.

    > M+1, ---, N-1, 0, 1, 2, ---, M-1

3. This round, the person at **M+1 + M** will be removed, and the survivor just after him is **M+1 + M + 1** who will be the first person of the circle in the new problem with **N-2** people.

4. Now we suppose **N-2=1**, then the final survivor would be the person at **0**. So what is the position of the survivor of the first circle ?

5. Since the final survivor's position is **F(M,N-1)=(M+1) % (N-1)** in the previous round, we can get the position of the survivor in the first round which is **(M+1 + F(M,N-1)) % N**, and we solve the problem.

6. **M+1** is the survivor after the one gets removed at current round, who is also the first in the next round. **M+1** is like a **base** position, and the survivor position in the next round is the **offset** from the **base**. We keep doing this recursively until only one people remains. 

7. From the bottom with one people, we keep adding the offset to the base to get the final survivor's position at the first round.