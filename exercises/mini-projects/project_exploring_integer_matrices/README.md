# Root Solver - Task Summary

Overview
- Exercise to use GitHub Copilot to explore a mathematics question on matrices.

Task
- We are going to try to find a 3x3 matrix with determinant 1 having only non-negative integer entries, but which is not a positive product of non-negative elementary matrices and not a permutation matrix.

## Example Matrices

### Example 1: Identity Matrix (determinant = 1)
```
[[1, 0, 0],
 [0, 1, 0],
 [0, 0, 1]]
```

### Example 2: Permutation Matrix (determinant = 1)
```
[[0, 1, 0],
 [0, 0, 1],
 [1, 0, 0]]
```
### Example 3: Simple Elementary Matrix (determinant = 1)
```
[[1, 0, 1],
 [0, 1, 0],
 [0, 0, 1]]
```

### Example 4: Upper Triangular (determinant = 1)
```
[[1, 2, 3],
 [0, 1, 4],
 [0, 0, 1]]
```

### Example 5: Candidate Matrix (determinant = 1)
```
[[1, 1, 0],
 [0, 1, 1],
 [1, 0, 1]]
```

### Example 6: Another Candidate (determinant = 1)
```
[[2, 1, 0],
 [1, 1, 0],
 [0, 1, 1]]
```

## Notes
- All entries must be non-negative integers
- The determinant must equal 1
- Test whether the matrix can be expressed as a positive product of elementary matrices

## Proposed plan
- populate a database of integer matrices
    - build larger and larger matrices (all entries smaller than or equal to k, for some fixed k, incrementing k with each pass, storing the ones which have determinant 1)
- pass through the list of new matrices and check if they admit a row reduction or column reduction resulting in a smaller (top entry) matrix.
- Any matrix which has no column or row reduction satisfies our criteria.