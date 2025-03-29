def find_duplicates(nums):
    from collections import Counter
    counts = Counter(nums)
    return [key for key, value in counts.items() if value > 1]

nums = [1, 2, 3, 1, 2, 4]
print(find_duplicates(nums))
