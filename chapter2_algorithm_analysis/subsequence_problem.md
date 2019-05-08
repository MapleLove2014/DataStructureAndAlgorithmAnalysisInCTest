# Minimum Positive Subsequence

> This is the answer from stackoverflow [How to find minimum positive contiguous sub sequence in O(n) time?](https://stackoverflow.com/questions/31640902/how-to-find-minimum-positive-contiguous-sub-sequence-in-on-time)

```java
    int[] prefix = new int[A.length];
    prefix[0] = A[0];
    for(int i = 1; i < A.length; i++)
        prefix[i] = A[i] + prefix[i - 1];
    int result = MAX_VALUE;
    BinarySearchTree tree;
    for(int i = 0; i < A.length; i++){
        if(A[i] > 0)
        result = min(result, A[i];
        int v = tree.getMaximumElementLessThan(prefix[i]);
        result = min(result, prefix[i] - v);
        tree.add(prefix[i]);
    }
```

## Ideas I get from the answer

- The **seq[i,j] of seq[n]** is the minimum positive subsequence if and only if the prefix sum (which is prefix in the answer) of j minus i is the **most smallest result** among all the possible of i' and j's when j' > i' and prefix sum of j' is great than i'.

## Some changes to the code in the answer

1. There is no need to consider A[i] in the loop. The reason is if A[i] is the minimum positive subsequence which means the prefix sum of i only grows **a very little bit** to make the prefix sum of i-1 the maximum less than prefix sum of i. At the last three steps, we can still get the result of A[i].

2. We can combine the two parts together when calculating the prefix sums and comparing the minimum positive subsequence.

## My implementation in python

```python
    BinarySearchTree tree
    prefix = [0] * len(sequence)
    min_pos_subseq = sys.maxsize
    for seq in sequence:
        prefix.append(prefix[-1] + seq)
        less_prefix = tree.get_maximum_less_than(prefix[-1])
        if less_prefix:
            min_pos_subseq = min(min_pos_subseq, less_prefix)
    print(min_pos_subseq)
```

## My proof using induction
1. base case: the algorithm is true obviously.

2. induction
    - suppose the algorithm is correct when the size of sequence is n-1, and the corresponding minimum positive subsequence is $M_{i,j}$.
    
    - When we add the nth element to the sequence, the only thing we wanna know is whether the new element is in the new subsequence that is whether the new subsequence end at the new element. Suppose the new subsequence is $M_{p,q}$, now we prove that it is correct.
        
        - if a subsequence end at the new element i.e $q=n$ is less than $M_{i,j}$ , then $M_{p,q}$ is the minimum positive subsequence.

        - the $M_{p,q}=M_{i,j}$ if that subsequence end at the n is not less than $M_{i,j}$ , thus the $M_{p,q}$ is the minimum positive subsequence when it's length is n.

# Maximum subsequence product

> I get this answer from youtube as follows:

```python
    local_max = local_min = global_max = sequence[0]

    for i in range(1, len(sequence)):
        a = local_max * sequence[i]
        b = local_min * sequence[i]

        local_max = max(max(a, b), sequence[i])
        local_min = min(min(a, b), sequence[i])

        global_max = max(global_max, local_max)
```

## My proof using induction

1. base case : the algorithm is true obviously

2. induction
    - suppose the algorithm is correct when the size of the sequence is $n-1$.
    
    - When the size grows to $n$ , we can see that the nth local max comes from the previous local max, local min and the nth element. We could get the global max after comparing the previous global max and the new global max finally.

## Some notes

1. we must try the longest subsequence to find out the max product, since all the numbers are integers

2. if the number is negative, we keep the product by local max and local min depend on the signs of the previous local max and local min.