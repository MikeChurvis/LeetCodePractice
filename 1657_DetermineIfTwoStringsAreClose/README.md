# 1657. Determine if Two Strings Are Close

> Difficulty: Medium

## Problem Specification

Two strings are considered close if you can attain one from the other using the following operations:

- Operation 1: Swap any two existing characters.
    - For example, abcde -> aecdb
- Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
    - For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

### Examples

**Example 1:**

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

**Example 2:**

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

**Example 3:**

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
 
### Constraints

1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.

## Solution Design

Letter count is conserved. Words of unequal lengths always evaluate to false.

Letter classes are conserved. Words with letters not included in their counterpart always evaluate to false.

This might be a pathfinding problem. 
- I need a "distance" heuristic based on similarity; identical words are maximally similar, and have a distance of 0.
- Memoize explored configurations so that the pathfinder does not retread explored ground.

Case study: dog, god
- Steps: op1 dg
- Op2 is equally valid. It does the same thing.

If distance is the number of steps taken, then this becomes a breadth-first search. This will eventually discover the right answer, but seems highly inefficient. Let's code it, then see if there are ways to improve the heuristic.

### BFS

We are transforming word 1 into word 2. We need a set of operations.

---

I just realized the core of this problem:
- There are letter classes and letter counts.
- Each letter class has a count.
- Operation 2 lets you swap the counts between letter classes.
- Operation 1 guarantees that words with the same letter class counts can be transformed into each other by changing the position of each letter.
- The problem asks only if the words *can* become each other. It does not ask us to enumerate the steps.

Consider Example 3 above: cabbba, abbccc.

cabbba
a, b, c
2, 3, 1

abbccc
a, b, c
1, 2, 3

Operation 1 swaps the position of letters in the word. Operation 2 swaps the position of counts by letter class.

This is not a pathfinding problem. It's a simple comparison.

### Letter Class Counts

1. Accumulate the letter counts.
2. Grab just the counts as an array.
3. Sort the array.
4. If the arrays are the same, return True.
