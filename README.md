# LeetCode 75 — Python

Parallel companion to `leetcode-75-go`. One folder per problem grouped under category folders.

## Setup

```pwsh
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```pwsh
# Single problem
pytest two_pointers/01_move_zeroes -v

# One category
pytest two_pointers -v

# Everything
pytest -v
```

Stubs use `pytestmark = pytest.mark.skip(...)` so unimplemented problems don't break the suite. Remove that line in `test_solution.py` once you start a problem.

## Layout

```
<category>/<NN>_<snake_slug>/
  solution.py        # class Solution: ... (or class-based problem stub)
  test_solution.py   # pytest.mark.skip + scratch space for cases
```

`conftest.py` and `pytest.ini` together let every problem's `test_solution.py` do `from solution import Solution` without packaging boilerplate: `--import-mode=importlib` plus a hook that puts each problem's folder at the front of `sys.path` and evicts the cached `solution` module before pytest imports the test file.

Numbering is **per-category** (01..N within each topic), not global across all 75.

Tree / linked-list problems include the `TreeNode` / `ListNode` class at the top of `solution.py` — matches how LeetCode pre-fills the editor.

## Progress (75 problems)

### Array / String
- [x] 01 Merge Strings Alternately (1768)
- [ ] 02 Greatest Common Divisor of Strings (1071)
- [ ] 03 Kids With the Greatest Number of Candies (1431)
- [ ] 04 Can Place Flowers (605)
- [ ] 05 Reverse Vowels of a String (345)
- [ ] 06 Reverse Words in a String (151)
- [ ] 07 Product of Array Except Self (238)
- [ ] 08 Increasing Triplet Subsequence (334)
- [ ] 09 String Compression (443)

### Two Pointers
- [ ] 01 Move Zeroes (283)
- [ ] 02 Is Subsequence (392)
- [ ] 03 Container With Most Water (11)
- [ ] 04 Max Number of K-Sum Pairs (1679)

### Sliding Window
- [ ] 01 Maximum Average Subarray I (643)
- [ ] 02 Maximum Number of Vowels in a Substring of Given Length (1456)
- [ ] 03 Max Consecutive Ones III (1004)
- [ ] 04 Longest Subarray of 1's After Deleting One Element (1493)

### Prefix Sum
- [ ] 01 Find the Highest Altitude (1732)
- [ ] 02 Find Pivot Index (724)

### Hash Map / Set
- [ ] 01 Find the Difference of Two Arrays (2215)
- [ ] 02 Unique Number of Occurrences (1207)
- [ ] 03 Determine if Two Strings Are Close (1657)
- [ ] 04 Equal Row and Column Pairs (2352)

### Stack
- [ ] 01 Removing Stars From a String (2390)
- [ ] 02 Asteroid Collision (735)
- [ ] 03 Decode String (394)

### Queue
- [ ] 01 Number of Recent Calls (933)
- [ ] 02 Dota2 Senate (649)

### Linked List
- [ ] 01 Delete the Middle Node of a Linked List (2095)
- [ ] 02 Odd Even Linked List (328)
- [ ] 03 Reverse Linked List (206)
- [ ] 04 Maximum Twin Sum of a Linked List (2130)

### Binary Tree - DFS
- [ ] 01 Maximum Depth of Binary Tree (104)
- [ ] 02 Leaf-Similar Trees (872)
- [ ] 03 Count Good Nodes in Binary Tree (1448)
- [ ] 04 Path Sum III (437)
- [ ] 05 Longest ZigZag Path in a Binary Tree (1372)
- [ ] 06 Lowest Common Ancestor of a Binary Tree (236)

### Binary Tree - BFS
- [ ] 01 Binary Tree Right Side View (199)
- [ ] 02 Maximum Level Sum of a Binary Tree (1161)

### Binary Search Tree
- [ ] 01 Search in a Binary Search Tree (700)
- [ ] 02 Delete Node in a BST (450)

### Graphs - DFS
- [ ] 01 Keys and Rooms (841)
- [ ] 02 Number of Provinces (547)
- [ ] 03 Reorder Routes to Make All Paths Lead to the City Zero (1466)
- [ ] 04 Evaluate Division (399)

### Graphs - BFS
- [ ] 01 Nearest Exit from Entrance in Maze (1926)
- [ ] 02 Rotting Oranges (994)

### Heap / Priority Queue
- [ ] 01 Kth Largest Element in an Array (215)
- [ ] 02 Smallest Number in Infinite Set (2336)
- [ ] 03 Maximum Subsequence Score (2542)
- [ ] 04 Total Cost to Hire K Workers (2462)

### Binary Search
- [ ] 01 Guess Number Higher or Lower (374)
- [ ] 02 Successful Pairs of Spells and Potions (2300)
- [ ] 03 Find Peak Element (162)
- [ ] 04 Koko Eating Bananas (875)

### Backtracking
- [ ] 01 Letter Combinations of a Phone Number (17)
- [ ] 02 Combination Sum III (216)

### DP - 1D
- [ ] 01 N-th Tribonacci Number (1137)
- [ ] 02 Min Cost Climbing Stairs (746)
- [ ] 03 House Robber (198)
- [ ] 04 Domino and Tromino Tiling (790)

### DP - Multidimensional
- [ ] 01 Unique Paths (62)
- [ ] 02 Longest Common Subsequence (1143)
- [ ] 03 Best Time to Buy and Sell Stock with Transaction Fee (714)
- [ ] 04 Edit Distance (72)

### Bit Manipulation
- [ ] 01 Counting Bits (338)
- [ ] 02 Single Number (136)
- [ ] 03 Minimum Flips to Make a OR b Equal to c (1318)

### Trie
- [ ] 01 Implement Trie (Prefix Tree) (208)
- [ ] 02 Search Suggestions System (1268)

### Intervals
- [ ] 01 Non-overlapping Intervals (435)
- [ ] 02 Minimum Number of Arrows to Burst Balloons (452)

### Monotonic Stack
- [ ] 01 Daily Temperatures (739)
- [ ] 02 Online Stock Span (901)

## Python idioms worth front-loading

- `collections.deque` for O(1) popleft (use over `list.pop(0)` which is O(n))
- `heapq` is a min-heap — negate values for max-heap
- `collections.defaultdict(list)` / `Counter` for grouping and tallying
- `bisect.bisect_left` / `bisect_right` for sorted insertion / binary search
- `@functools.cache` for top-down memoization (one line beats manual dict)
- Tuple unpacking: `a, b = b, a + b`, `for i, x in enumerate(arr):`
- Build strings with `"".join(parts)`, not `+=` in a loop
