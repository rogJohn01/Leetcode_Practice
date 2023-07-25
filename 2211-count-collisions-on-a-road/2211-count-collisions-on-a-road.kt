class Solution {
    fun countCollisions(dirs: String): Int {
        var ans = 0
        val st = mutableListOf<Char>()
        for (e in dirs) {
            if (e == 'L' && st.isNotEmpty()) {
                if (st.last() == 'L') continue
                ans++
                while (st.isNotEmpty() && st.last() == 'R') {
                    ans++
                    st.removeAt(st.lastIndex)
                }
                st.add('S')
            }

            if (e == 'S' && st.isNotEmpty()) {
                while (st.isNotEmpty() && st.last() == 'R') {
                    ans++
                    st.removeAt(st.lastIndex)
                }
                st.add('S')
            }

            if (e == 'R') {
                st.add(e)
            } else if (st.isEmpty()) {
                st.add(e)
            }
        }
        return ans
    }
}
