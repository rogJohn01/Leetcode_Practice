
class Solution {
  public int uniquePaths(int m, int n ){
    int[][] area = new int[m][n];
    for ( int i =0 ; i< m ; i++){
      for(int j=0 ; j < n ; j++){
        if (i==0 || j ==0 ) area[i][j] =1;
        else area[i][j] = area[i-1][j] + area[i][j-1];
      }
    }
    return area[m-1][n-1];
  }
}