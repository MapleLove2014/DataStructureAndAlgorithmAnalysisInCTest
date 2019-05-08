# Shuffle Algorithm

1. [Fisher–Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle) to generate a random permutation equally likely. This method can be divided into 4 steps as follows suppose we have a collection with N numbers:

    - pick a position i randomly in the unshuffled collection
    - put this number at position i to the new collection
    - delete the number at position i in old collection
    - then repeat step 1 to 3 to generate a random permutation finally
    
    > The probability must be **1/n!** to make sure we generate the random permutation **equally likely**

2. the modern algorithm named after  Donald E. Knuth called Knuth Shuffle

    - version 1
        ```python
        for i from n-1 downto 1
            j = random(0, i) inclusively
            swap data[i] and data[j]
        ```
    - version 2 the same as 1
        ```python
        for i from 0 to n-2
            j = random(i, n-1) inclusively
            swap data[i] and data[j]
        ```

    > the analysis is very simple, since the probability of picking an unshuffled number at round **i** is **1/n-i**, the final permutation is randomly generated at probability **1/n!**

3. some other variants

    - version 1
        ```python
        for i from 0 to n-1
            j = random(0, i) inclusively
            if j not equals to i
                data[i] = data[j] 
            data[j] = source[i]
        ```

    - version 2 which is the same as version 1 except the start index i chooses is 1 from data structure and algorithm analysis in c 
        ```python
        for i from 1 to n-2
            j = random(0, i) inclusively
            swap data[i] and data[j]
        ```

    > analysis : suppose the collection we have is **{A B C D E}**, then nothing changes after first loop with the probability **1** to place A in position 0. We continue looking at the next run which will generate **{A B}** and **{B A}** with the same probability **1/2**. If we continue doing this, we would get **{A B C} {A C B} {C B A} {B A C} {B C A} {C A B}** at probability **1/3**. So the probability of the sequence we get finally is **1/n!** which makes all the permutations equally likelly. 