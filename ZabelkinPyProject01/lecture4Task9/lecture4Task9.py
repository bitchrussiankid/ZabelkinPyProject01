nums = [1, 2, 2, 2, 2, 2, 2, 4]
target = 5

a = len(nums)
b = 0
c = 1
breakFlag = False

while b < a:
    for c in range(a):
         if nums[b] + nums[c] == target:
            print(nums[b], nums[c])
            breakFlag = True
    if breakFlag == True: break
    b += 1