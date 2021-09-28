# Remove Duplicates from sorted list
# Remove Duplicates from Sorted Array II

def remove_duplicates(nums) -> int:
    if len(nums) == 0:
        return 0
    [nums.remove(i) for i in nums[::] if nums.count(i) > 2]
    return len(nums), nums


sortedlist = [1, 1, 1, 2, 2, 3, 4]

print(remove_duplicates(sortedlist))
