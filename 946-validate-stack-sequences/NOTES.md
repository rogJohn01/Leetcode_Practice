# no sign that pushed is sorted ?
# rules!
1.
popped[0] : determines how much to push at first
1-1. if popped[0] in [4,5]
must need to push until 4
1-2. if popped[0] in [1,2]
ex: popped = [1,2,3,4,5]
popped = [1,2,4,3,5]
popped = [1,2,4,5,3]
popped = [1,2,5,3,4]
then -> popped[1] 4,5
ex2:
pushed[-1] != popped[i]:
return False