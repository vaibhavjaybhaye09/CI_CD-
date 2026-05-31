# find two numbers in array 

def find_two_no(numbers, target):
    left = 0
    right = len(numbers)-1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return numbers[left], numbers[right]
        elif total < target:
            left = left + 1
        else:
            right = right - 1


numbers =[2,7,11,15]
print(find_two_no(numbers, 9))