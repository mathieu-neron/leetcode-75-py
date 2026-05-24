# LeetCode 75 — Python

Parallel companion to `leetcode-75-go`. One folder per problem.

## Setup

```pwsh
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```pwsh
# Single problem
pytest 01_merge_strings_alternately -v

# Everything
pytest -v
```

## Layout

- `NN_snake_name/solution.py` — `class Solution:` with LeetCode-style method
- `NN_snake_name/test_solution.py` — `pytest.mark.parametrize` cases
- `conftest.py` lets each problem `from solution import Solution` without packaging boilerplate

## Progress

- [x] 01 Merge Strings Alternately (1768)
- [ ] 02 Greatest Common Divisor of Strings (1071)
- [ ] 03 Kids With the Greatest Number of Candies (1431)
- [ ] 04 Can Place Flowers (605)
- [ ] 05 Reverse Vowels of a String (345)
- [ ] ... fill in the rest from https://leetcode.com/studyplan/leetcode-75/

## Python idioms worth front-loading

- `collections.deque` for O(1) popleft (use over `list.pop(0)` which is O(n))
- `heapq` is a min-heap — negate values for max-heap
- `collections.defaultdict(list)` / `Counter` for grouping and tallying
- `bisect.bisect_left` / `bisect_right` for sorted insertion / binary search
- `@functools.cache` for top-down memoization (one line beats manual dict)
- Tuple unpacking: `a, b = b, a + b`, `for i, x in enumerate(arr):`
- Build strings with `"".join(parts)`, not `+=` in a loop
