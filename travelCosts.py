#ex1
scores = [-10, 15, -3, 20, 0, 8]
result = [score for score in scores if score > 0]

print(result)
#Ex2
numbers = [1, 2, 3, 4, 5, 6]
result = [num ** 2 for num in numbers if num % 2 == 0]
print(result)
#ex3
words = ["cat", "python", "dog", "code", "ai"]
result = [word.upper() for word in words if len(word) > 3]
print(result)

# Ex4
names = ["Alice", "Bob", "Amanda", "Charlie", "Alex"]
result = [name for name in names if name.startswith("A")]
print(result) 

#Problem 1
def count_duplicate_adjacent_numbers(numbers_list):
    ans = []
    for nums in numbers_list:
        count = 0
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                count += 1
                i += 2  
            else:
                i += 1
        ans.append(count)
    return ans

numbers_list = [[1, 1, 1, 1], [1, 2, 3, 4], [5, 5, 6, 6, 6], [9, 9, 9]]
print(count_duplicate_adjacent_numbers(numbers_list))

def count_ab_pairs(words):
    ans = []
    for word in words:
        count = 0
        for i in range(len(word) - 1):
            if word[i] == 'a' and word[i + 1] == 'b':
                count += 1
        ans.append(count)
    return ans
