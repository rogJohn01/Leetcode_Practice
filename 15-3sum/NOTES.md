​
use two pointer !
1. first sort
2. use two pointer
3.  subtrack the last one from first, second !
​
​
```
else:
ret.append([nums[i], nums[left], nums[right]])
left +=1
right -=1
```
if only left +=1, then it surpasses target k. If only right -=1, then it is less than k and has to move left +=1,. So, in conclusion, being adequate and efficient it is good to move both.
​
```
while left < right and nums[left] == nums[left-1]:
​
```
​
why ? if  nums[left] == nums[left-1], then  <find = target - nums[left] > the find value becomes the same. So, the end result that appends to the answer becomes same with the previous one.