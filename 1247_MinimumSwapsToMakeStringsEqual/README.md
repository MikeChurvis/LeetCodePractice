# 1247. Minimum Swaps to Make Strings Equal

> Difficulty: Medium
> Time to Solve: 

## Problem Statement

You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].

Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

### Examples

**Example 1:**

Input: s1 = "xx", s2 = "yy"
Output: 1
Explanation: Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".

**Example 2:**

Input: s1 = "xy", s2 = "yx"
Output: 2
Explanation: Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
Note that you cannot swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.

**Example 3:**

Input: s1 = "xx", s2 = "xy"
Output: -1
 
### Constraints

1 <= s1.length, s2.length <= 1000
s1, s2 only contain 'x' or 'y'.

## Solution Design

The strings are guaranteed to be of equal length and share the same letters. The checks from problem 1657 are not necessary.

Both words must share the same number of letters. If the count of any letter is not even, no solution exists.

Compare the length of the longest shared substring at each step? Maybe this informs a distance heuristic for a depth-first search.

### Depth-First Search

Distance heuristic:
- Most shared characters.

Mask:
```
        v       v
xxyyxy xyyyxy xyxyxy 
100111 110110 111111
xyxyxy xyxyxx xyxyxy
            ^      ^

 v      v
xxyyxy xyyyxy xxyyxy
100111 100111 111111
xyxyxy xxxyxy xxyyxy
 ^       ^

v   v
xxy yxy xxy
010 010 111
yxx xxx xxy
^     ^

v     v
xxyxy yxyxy 
01110 01110
yxyxx xxyxx
^        ^

If counts are balanced, two swaps are needed.

xxxx yxxx yyxx
0000 1001 1111
yyyy yyyx yyxx 

Swap the first conflicting pair at the head with the first inverse conflicting pair at the tail.

```

2 swaps for strings with equal x-y counts. 
x...y y...y x...y
y...x x...x x...y

1 swap for strings with unequal x-y counts.
y...y x...y
x...x x...y

 neq   eq   
xxxyx yxxyx
yyyxx yyxxx

I feel like this is just a counting problem in disguise.