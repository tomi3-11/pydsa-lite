# Complexity analysis

Complexity describes how resource use grows as input size grows. It is not a stopwatch measurement.

## Common growth rates

| Complexity | Name | Typical example |
|---|---|---|
| O(1) | Constant | Access a list element by index |
| O(log n) | Logarithmic | Binary search in a sorted sequence |
| O(n) | Linear | Scan a list once |
| O(n log n) | Linearithmic | Efficient comparison sorting |
| O(n²) | Quadratic | Compare every pair |
| O(2ⁿ) | Exponential | Enumerate all subsets |
| O(n!) | Factorial | Enumerate all permutations |

## How to analyze code

Count how often the meaningful operations execute as input size grows.

A single loop over n values is O(n). Two nested loops that each range over n values are O(n²). Consecutive loops add their costs; the dominant term determines the asymptotic bound.

## Time and space are different

A solution can use O(n) time and O(1) auxiliary space, or O(n) time and O(n) extra space. State which memory is part of the input and which memory the algorithm allocates.

## Python details matter

- list[index] is O(1), while searching with value in some_list is O(n).
- dict and set membership are O(1) on average, with O(n) worst-case behavior.
- list.append() is amortized O(1); an individual resize can cost O(n).
- deque.append() and deque.popleft() are approximately O(1).
- heapq.heappush() and heapq.heappop() are O(log n).

These are typical complexity guarantees, not promises about exact runtime. Always consider input size, operation mix, and memory constraints.

## Playground experiment

Try comparing membership in a list and a set in the playground. Increase the input size and observe how the code behaves. Timing results vary by browser and machine, so use them as an experiment rather than a proof.