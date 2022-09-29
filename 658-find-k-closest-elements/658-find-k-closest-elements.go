func findClosestElements(arr []int, k int, x int) []int {

    
    abs := func(x int) int{
        if x < 0 {
            return -x
        }
        return x }

    sort.Slice(arr, func(i,j  int) bool {
        if abs(arr[i]-x) == abs(arr[j] -x ) {
            return arr[i] < arr[j] 
        }
        return abs(arr[i]-x ) < abs(arr[j] -x)
    })

    ans := arr[:k] 
    sort.Ints(ans)
    return ans 
    } 
