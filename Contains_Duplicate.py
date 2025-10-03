LeetCode 217 – Contains Duplicate
# Brute Force Approach

class Solution:
    def containsDuplicate(self, nums):
        for i in range(len(nums)):              # Loop over each element
            for j in range(i + 1, len(nums)):   # Compare with all elements after it
                if nums[i] == nums[j]:          # If any two are equal
                    return True                 # Duplicate found
        return False                            # No duplicates found

Time Complexity 

O(n²) → Because for each element, we check all other elements after it.

  
Problem Explanation
Given an array of integers nums, return True if any value appears at least twice in the array, and False if every element is unique.
Input: nums = [1, 2, 3, 1]
Output: True → because 1 appears more than once.

Input: nums = [1, 2, 3, 4]
Output: False → all elements are unique.
Loop through each element (i).

For each element, loop through all the following elements (j).

If nums[i] == nums[j], then a duplicate is found → return True.

If the loops finish without finding any duplicates → return False.

Practiced using nested loops for pairwise comparisons.

Understood the brute force way of detecting duplicates.

Learned that brute force can be simple but not efficient.

