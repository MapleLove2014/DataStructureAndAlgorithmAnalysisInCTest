# Majority Element

## Divide and conquer

 > The majority element is one of the majority elements coming out from two sub problems.

1. It is obvious if the majority elements of two sub sequences agrees that the majority element of the overall sequence is the same.
2. If two majority elements does not agree, then one of the two is the majority element. Why?

    There are two occasions under two sub sequences with the majority elements $M_1$ of $S_1$ and $M_2$ of $S_2$ and the length of sequence is $N$. So:
    
    - If ${M_1}={M_2}$, the majority element of the sequence is $M_1$

    - otherwise $M_1$ or $M_2$.

        $count\space({M_1})\gt{\frac{N}{4}}$
        
        $count\space({M_2})\gt{\frac{N}{4}}$

        Then the element in $S_1$ except $M_1$ with max count less than $\frac{N}{4}$ and the same applies to the $S_2$. If they are the same and the total count would be less than $\frac{N} {2}$ which makes it non majority element.

## Boye-Moore Voting algorithm

The main concept of this algorithm is like team fighting. We have two teams the majority element team with more than n/2 elements and other elements. Obviously the majority element always wins. But we may got an element that is not the majority element. And that is why we need to verify whether it is correct by counting the element.

## Algorithm on the book

- If data length is even, the majority element appearances are greater than the other element by 2 at least. And there will always be two elements left to be together which is the majority element.

- if odd, we can divide it into two parts data except the last element and the last element. The last element won't change the fact if we found the majority element in the first part with length even. But if not, the majority may be the last lement instead.