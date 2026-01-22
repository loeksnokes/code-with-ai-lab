# Root Solver - Task Summary

Overview
- Exercise to use GitHub Copilot to explore a mathematics question on matrices.

Task
- We are going to try to find a 3x3 matrix with determinant 1 having only non-negative integer entries, but which is not a positive product of non-negative elementary matrices.

## Example Matrices

### Example 1: Identity Matrix (determinant = 1)
```
[[1, 0, 0],
 [0, 1, 0],
 [0, 0, 1]]
```

### Example 2: Simple Matrix (determinant = 1)
```
[[1, 0, 0],
 [0, 1, 0],
 [0, 0, 1]]
```

### Example 3: Upper Triangular (determinant = 1)
```
[[1, 2, 3],
 [0, 1, 4],
 [0, 0, 1]]
```

### Example 4: Candidate Matrix (determinant = 1)
```
[[1, 1, 0],
 [0, 1, 1],
 [1, 0, 1]]
```

### Example 5: Another Candidate (determinant = 1)
```
[[2, 1, 0],
 [1, 1, 0],
 [0, 1, 1]]
```

## Notes
- All entries must be non-negative integers
- The determinant must equal 1
- Test whether the matrix can be expressed as a positive product of elementary matrices
 