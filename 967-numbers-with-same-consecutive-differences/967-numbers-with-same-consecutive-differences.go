func numsSameConsecDiff(n int, k int) []int {
    

        cur := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
        for i := 0; i < n - 1; i++ {
            sd := []int{}
            for _, v := range cur {
                n := v % 10
                if n + k < 10 { sd = append(sd, v * 10 + n + k) }
                if n >= k && k > 0 { sd = append(sd, v * 10 + n - k) }
            }
            cur = sd
        }
        return cur

}