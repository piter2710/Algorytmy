#EXERCISE 1
def isPalindrome(text: str) -> bool:
    left = 0
    right = len(text) - 1
    
    while left < right:
        if(text[left] == text[right]):
            left+=1
            right-=1
        else:
            return False
    return True
    
print(isPalindrome("AlAa"))

#EXERCISE 2
sorted_list = [1,2,3,4,5]
target = 5

def has_pair_sum(nums,target):
    left,right = 0, len(nums) -1
    
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return True
        elif current_sum > target:
            right-=1
        else:
            left +=1
    return False

print(has_pair_sum(sorted_list,target))

#Exercise 3
arr = [1,2,3,3,4,5,6,3,2,1,3,4,5]
dlugosc = len(arr)
target_to_remove = 3
def remove_occurance(arr,target):
    writer = 0
    for reader in range (len(arr)):
        if arr[reader] != target:
            arr[writer] = arr[reader]
            writer +=1
    return writer

print(remove_occurance(arr,target_to_remove))
