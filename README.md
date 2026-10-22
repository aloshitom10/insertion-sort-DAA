# Insertion Sort (Python)

## Aim
Implement insertion sort to arrange integers in ascending order and analyze its time and auxiliary space complexities.

## Algorithm (step-by-step)
1. Consider the first element as a sorted portion.
2. Start from the second element (`i = 1`).
3. Store the current element in `key`; set `j = i - 1`.
4. While `j` is valid and `arr[j] > key`, shift `arr[j]` one position right and decrement `j`.
5. Place `key` at `arr[j + 1]`.
6. Repeat until every element has been considered.
7. Output the sorted array.

## Run the program
1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project directory.
4. Run:

   ```bash
   python insertion_sort.py
   ```

   On some systems, use `python3 insertion_sort.py`.

## Sample input and output

**Input**
```text
Enter number of elements: 5
Enter 5 integers separated by spaces: 12 11 13 5 6
```

**Output**
```text
Sorted array: 5 6 11 12 13
```

## Complexity analysis

Let `n` be the number of elements.

| Case | Input condition | Time complexity |
|---|---|---|
| Best | Already sorted | **O(n), Θ(n), Ω(n)** |
| Average | Typical/random order | **O(n²), Θ(n²), Ω(n²)** |
| Worst | Reverse sorted | **O(n²), Θ(n²), Ω(n²)** |

These are tight case-specific bounds. In the best case, the inner condition fails immediately for each outer-loop iteration, giving linear work. In average and worst cases, the algorithm performs a quadratic number of comparisons/shifts (average assuming distinct values in random order).

### Auxiliary space
- **O(1), Θ(1), Ω(1)** auxiliary space: only a fixed number of variables are used.
- The algorithm sorts **in place**. The input array itself is not counted as auxiliary space.

## Notes
- Insertion sort is stable because it shifts only elements strictly greater than `key`.
- It is adaptive and works well for small or nearly sorted arrays.
- It is not efficient for large, randomly ordered arrays due to quadratic average and worst-case time.

## Course outcome
**CO1:** Analyze an algorithm and express time and space complexity using asymptotic notations.
