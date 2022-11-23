class Solution {
    public boolean isValidSudoku(char[][] board) {
        
        int n = 9;
        int[] row = new int[n] ; 
        int[] col = new int[n] ;
        int[] boxes = new int[n] ;

        for(int r =0 ; r < n ; r++){
            for(int c=0; c < n ; c++){

                if(board[r][c] == '.'){
                    continue ; 
                }
                int v = board[r][c] - '0'; 
                int bit = 1 << (v-1);
                
                if((row[r] & bit) > 0){
                    return false; 
                } row[r] |= bit ; 

                if((col[c] & bit) > 0){
                    return false; 
                } col[c] |= bit ; 

                int ix = (r/3)*3 + c/3 ; 
                if((boxes[ix] & bit) > 0 ){
                    return false; 
                }
                boxes[ix] |= bit; 

            }
        }
        return true ; 
    }
}