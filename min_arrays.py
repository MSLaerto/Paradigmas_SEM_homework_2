array = [3, 6, 9, 2, 5, 3, 2, 1, 8, 3, 7, 9]
max_num = 10
              
def findSublists(nums, target):
    w, h = 8, 5
    arrays = []
    Massiv_sum = []
    print(f"Подмассивы массива {array} , с суммой меньше или равной {max_num}:")
    for i in range(len(nums)):
        sum_so_far = 0
        for j in range(i, len(nums)):
            sum_so_far += nums[j]
            if sum_so_far <= target:
                print(nums[i:j+1] , end = " ")
                arrays += nums[i:j+1]            
    return Massiv_sum            
findSublists(array, max_num)      