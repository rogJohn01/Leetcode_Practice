```
## 구현 잘함!
def stockPrice(nums, fee):
global cnt
left , right ,cnt  = 0,0,0
while left < len(nums)-1 or right <=len(nums)-1:
print('cnt: ',cnt)
print('left: ',left)
print('right: ',right)
if  nums[right] > nums[left]+fee:
cnt += nums[right] - (nums[left]+fee)
if right == len(nums)-1:
return cnt
left = right+1
right = left
if right == len(nums)-1 and nums[right] < nums[left]+fee:
left +=1
right = left+1
​
else:
right +=1
return cnt
```