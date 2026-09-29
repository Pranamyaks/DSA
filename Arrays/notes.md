PHASE 2 — ARRAYS IN PYTHON
===========================

1. ARRAY
--------

An array is a data structure used to store multiple elements in a sequence.

In Python, we generally use a list as an array.

Example:

arr = [10, 20, 30, 40, 50]

Index:

Index:    0    1    2    3    4
Value:   10   20   30   40   50

Important points:
- Index starts from 0.
- Elements can be accessed using an index.
- Python lists are mutable.
- Elements can be updated.
- len(arr) gives the number of elements.

Example:

arr = [10, 20, 30, 40, 50]

print(arr[0])     # 10
print(arr[2])     # 30

Negative indexing:

Index:   -5   -4   -3   -2   -1
Value:   10   20   30   40   50

arr[-1] gives 50.


2. TRAVERSAL
------------

Traversal means visiting each element of an array one by one.

Example:

arr = [10, 20, 30, 40, 50]

Traversal:

10 → 20 → 30 → 40 → 50


Method 1: Traversal using elements

for x in arr:
    print(x)

Here:
- x represents the current element.


Method 2: Traversal using index

for i in range(len(arr)):
    print(arr[i])

Here:
- i = index
- arr[i] = element at that index


Time Complexity:
O(n)

Space Complexity:
O(1)


3. INSERTION
------------

Insertion means adding a new element to an array.


Insert at the end:

arr.append(60)

Example:

arr = [10, 20, 30]

arr.append(40)

Result:

[10, 20, 30, 40]


Insert at a particular index:

arr.insert(2, 99)

Example:

arr = [10, 20, 30, 40]

arr.insert(2, 99)

Result:

[10, 20, 99, 30, 40]


When an element is inserted in the middle, elements after
that position may need to shift to the right.

Example:

Before:

10  20  30  40
        ↑
      index 2

After inserting 99:

10  20  99  30  40


Time Complexity:

Insertion at the end:
O(1) average

Insertion at beginning/middle:
O(n)


4. DELETION
-----------

Deletion means removing an element from an array.


Delete using index:

del arr[2]

Example:

arr = [10, 20, 30, 40]

del arr[2]

Result:

[10, 20, 40]


Using pop():

arr.pop(2)

This removes the element at index 2.


Remove the last element:

arr.pop()


Delete by value:

arr.remove(30)

This removes the first occurrence of 30.


Time Complexity:

Delete from the end:
O(1)

Delete from beginning/middle:
O(n)


5. SEARCHING
------------

Searching means finding whether a particular element exists
in an array.

The basic searching technique for an unsorted array is
Linear Search.


Example:

arr = [10, 20, 30, 40, 50]

target = 30


Linear Search:

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index", i)


Basic pattern:

Traverse
   ↓
Check condition
   ↓
Element found?


Time Complexity:

Best Case:
O(1)

Worst Case:
O(n)

Space Complexity:
O(1)


6. UPDATING
-----------

Updating means changing the value of an existing element.

Example:

arr = [10, 20, 30, 40]

arr[2] = 100

Result:

[10, 20, 100, 40]


General syntax:

arr[index] = new_value


Example:

arr[0] = 500


Time Complexity:

O(1)


7. MINIMUM
----------

Minimum means finding the smallest element in an array.

Example:

arr = [10, 5, 30, 2, 40]

Minimum = 2


Logic:

minimum = arr[0]

for x in arr:
    if x < minimum:
        minimum = x


We initially assume that the first element is the minimum.

Then compare every other element with the current minimum.

If a smaller element is found, update minimum.


Time Complexity:
O(n)

Space Complexity:
O(1)


8. MAXIMUM
----------

Maximum means finding the largest element in an array.

Example:

arr = [10, 5, 30, 2, 40]

Maximum = 40


Logic:

maximum = arr[0]

for x in arr:
    if x > maximum:
        maximum = x


We initially assume that the first element is the maximum.

Then compare every other element with the current maximum.

If a larger element is found, update maximum.


Time Complexity:
O(n)

Space Complexity:
O(1)


9. REVERSAL
-----------

Reversal means arranging the elements in the opposite order.

Example:

Before:

[10, 20, 30, 40, 50]

After:

[50, 40, 30, 20, 10]


Python method:

arr.reverse()


DSA approach: Two-Pointer Technique

Start with two pointers:

[10, 20, 30, 40, 50]
 ↑                 ↑
left              right


Swap the elements.

[50, 20, 30, 40, 10]


Move the pointers towards the center.

[50, 20, 30, 40, 10]
     ↑       ↑
    left   right


Continue until:

left >= right


Basic logic:

left = 0
right = len(arr) - 1

while left < right:

    swap arr[left] and arr[right]

    left moves right
    right moves left


Time Complexity:
O(n)

Space Complexity:
O(1)


10. FREQUENCY
-------------

Frequency means the number of times an element occurs
in an array.

Example:

arr = [1, 2, 2, 3, 1, 2]

Frequency:

1 → 2
2 → 3
3 → 1


A dictionary is commonly used.

frequency = {}

for x in arr:

    if x in frequency:
        frequency[x] += 1
    else:
        frequency[x] = 1


Result:

{1: 2, 2: 3, 3: 1}


Basic idea:

Element
   ↓
Already exists in dictionary?
   ↓
Yes → increase count
No  → create count = 1


Time Complexity:
O(n) average

Space Complexity:
O(n) in the worst case


11. PREFIX SUM
--------------

Prefix sum stores the cumulative sum of elements
from the beginning of the array.

Example:

arr = [2, 4, 3, 5, 1]


Prefix calculation:

2

2 + 4 = 6

2 + 4 + 3 = 9

2 + 4 + 3 + 5 = 14

2 + 4 + 3 + 5 + 1 = 15


Prefix array:

[2, 6, 9, 14, 15]


Formula:

prefix[i] = prefix[i - 1] + arr[i]


For the first element:

prefix[0] = arr[0]


Why prefix sum is useful:

It allows us to calculate the sum of a range efficiently.

Example:

arr = [2, 4, 3, 5, 1]

Sum from index 1 to 3:

4 + 3 + 5 = 12


Using prefix:

prefix[3] - prefix[0]

14 - 2 = 12


General formula:

range_sum = prefix[r] - prefix[l - 1]

when l > 0.


Time Complexity for creating prefix array:
O(n)

Time Complexity for a range-sum query:
O(1)

Space Complexity:
O(n) if a separate prefix array is created.


12. SUBARRAYS
-------------

A subarray is a contiguous part of an array.

Example:

arr = [1, 2, 3]


Valid subarrays:

[1]
[2]
[3]
[1, 2]
[2, 3]
[1, 2, 3]


[1, 3] is NOT a subarray because the elements
are not contiguous.


Important:

SUBARRAY = CONTIGUOUS ELEMENTS


Example:

[1, 2, 3, 4]


Starting from 1:

[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]


Starting from 2:

[2]
[2, 3]
[2, 3, 4]


Starting from 3:

[3]
[3, 4]


Starting from 4:

[4]


Number of subarrays:

For an array containing n elements:

Number of subarrays = n(n + 1) / 2


Example:

n = 4

Number of subarrays:

4 × 5 / 2 = 10


SUBARRAY vs SUBSEQUENCE
-----------------------

Subarray:
Elements must be contiguous.

Example:

[1, 2, 3]

[2, 3] → Subarray


Subsequence:
Elements do not necessarily need to be contiguous.

Example:

[1, 2, 3]

[1, 3] → Subsequence


13. TIME COMPLEXITY SUMMARY
---------------------------

Operation                    Time Complexity

Access by index              O(1)

Update by index              O(1)

Traversal                    O(n)

Linear Search                O(n)

Insertion at end             O(1) average

Insertion at beginning       O(n)

Insertion in middle          O(n)

Deletion at end              O(1)

Deletion at beginning        O(n)

Deletion in middle           O(n)

Find Minimum                 O(n)

Find Maximum                 O(n)

Reverse                      O(n)

Frequency                    O(n) average

Create Prefix Sum            O(n)


KEY CONCEPTS TO REMEMBER
------------------------

1. Traversal
   → Visit every element.

2. Insertion
   → Add an element.

3. Deletion
   → Remove an element.

4. Searching
   → Find an element.

5. Updating
   → Change an existing element.

6. Minimum / Maximum
   → Find the smallest / largest element.

7. Reversal
   → Reverse the order of elements.

8. Frequency
   → Count how many times elements occur.

9. Prefix Sum
   → Store cumulative sums.

10. Subarray
    → A contiguous portion of an array.
