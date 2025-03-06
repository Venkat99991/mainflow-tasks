nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
unique_nums = list(set(nums))  # Remove duplicates
unique_nums.sort(reverse=True)
print(f"Second largest number: {unique_nums[1]}")
