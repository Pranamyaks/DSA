1. Time Complexity
Time complexity tells us how the running time of an algorithm grows when the input size n increases.
It does not mean the exact time in seconds.

2. Space Complexity
Space complexity tells us how much extra memory an algorithm needs as the input size increases.

Common Time Complexities
O(1) → Constant
Example: Accessing arr[0]
O(log n) → Logarithmic
Example: Binary Search
O(n) → Linear
Example: One loop through an array
O(n log n) → Linearithmic
Example: Merge Sort
O(n²) → Quadratic
Example: Two nested loops
O(n³) → Cubic
Example: Three nested loops
O(2ⁿ) → Exponential
Example: Some recursive problems
O(n!) → Factorial
Example: Generating all permutations

Common Space Complexities
O(1) → Constant extra memory
O(n) → Extra memory grows with input size
O(n²) → Extra memory grows quadratically

Important Rules
Ignore constants: O(2n) → O(n)
Keep the highest-growing term: O(n² + n) → O(n²)
Sequential loops are added: O(n) + O(n) → O(n)
Nested loops are multiplied: O(n) × O(n) → O(n²)

Quick Remember
Time Complexity → How much time?
Space Complexity → How much extra memory?
Smaller complexity = generally better performance.
