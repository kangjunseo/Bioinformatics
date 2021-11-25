# Compute the Number of Times a Pattern Appears in a Text
## Problem
This is the first problem in a collection of "code challenges" to accompany Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.

A k-mer is a string of length k. We define Count(Text, Pattern) as the number of times that a k-mer Pattern appears as a substring of Text. For example,

Count(ACAACTATGCATACTATCGGGAACTATCCT,ACTAT)=3.
We note that Count(CGATATATCCATAG, ATA) is equal to 3 (not 2) since we should account for overlapping occurrences of Pattern in Text.

To compute Count(Text, Pattern), our plan is to “slide a window” down Text, checking whether each k-mer substring of Text matches Pattern. We will therefore refer to the k-mer starting at position i of Text as Text(i, k). Throughout this book, we will often use 0-based indexing, meaning that we count starting at 0 instead of 1. In this case, Text begins at position 0 and ends at position |Text| − 1 (|Text| denotes the number of symbols in Text). For example, if Text = GACCATACTG, then Text(4, 3) = ATA. Note that the last k-mer of Text begins at position |Text| − k, e.g., the last 3-mer of GACCATACTG starts at position 10 − 3 = 7. This discussion results in the following pseudocode for computing Count(Text, Pattern).  

Implement PatternCount
Given: {DNA strings}} Text and Pattern.

Return: Count(Text, Pattern).


```python
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count+=1
    print(count)

Text, Pattern = input().split()
PatternCount(Text, Pattern)
```

    GGTACCTGGAAAATACCTGGTACCTGGTACCTGGAGGCTACCTGGTACCTGGTACCTGGCCAGTTATACCTGGTACCTGGAGTCAGATACCTGGGTACCTGGAGTACCTGGAAATACCTGGCTTACCGTACCTGGAAGTACCTGGTACCTGGTACCTGGTACCTGGAGTACCTGGCTACCTGGAGCGTTATAATTACCTGGTACCTGGCTGAGAACTCACGTTACCTGGTACCTGGAATACCTGGATACCTGGAGTACCTGGTACCTGGTACCTGGGATACCTGGTACCTGGTACCTGGGTACCTGGGTACCTGGTACCTGGAGTACCTGGCAATACCTGGCTACCTGGTACCTGGTACCTGGGGCCATACCTGGAATCACCTACCTGGTACCTGGTTACCTGGGGCTACCTGGAAATACCTGGGTTCGTACCTGGCTTACCTGGTGGCTTACCTGGCTACCTGGCTACCTGGAGTACCTGGGAGGTACCTGGTACCTGGTTGCTGATACCTGGACTACCTGGTGGCGCTACCTGGAGCCATACCTGGACTTACCTGGTCAGCTACCTGGGTTTCTACCTGGTCGCTACCTGGTACCTGGTTTACCTGGTACCTGGATACCTGGTCATTACCTGGGATACCTGGTTACCTGGAGTCGATCTACCTGGTTACCTGGAGTGTACCTGGTTACCTGGCCTACCTGGCGTACCTGGGAGGTACCTGGGTAAGGTACCTGGATACCTGGCCTACCTGGAATACCTGGAGATACCTGGTACCTGGATACCTGGTACCTGGTACCTGGTATACCTGGTACCTGGCTAAGCCGATTGTACCTGGCTCTCTACCTGGTACCTGGATACCTGGATACCTGGTACCTGGTACCTGGTACCTGGCTACCTGGTACCTGGTACCTGGTACCTGGTAGATGTACCTGGCTTACCTGGTCCCTACCTGGCTACCTGGGACCAATATACCGTTACCTGGTACCTGGTACCTGGTTACCTGGTTACCTGGTTTACCTGGTAAGCGCATACCTGG TACCTGGTA
    37



```python

```
