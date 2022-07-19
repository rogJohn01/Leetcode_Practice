class Solution {
    public List<List<Integer>> generate(int nrow) {
    
        
            List<List<Integer>> tri = new ArrayList<List<Integer>>() ; 
            ArrayList<Integer> row = new ArrayList<Integer>() ; 
            for( int r =0; r < nrow ; r++ ){
                row.add(0,1); 
                for(int c=1; c < row.size()-1; c++){
                    row.set( c , row.get(c)+ row.get(c+1)) ;  }
                tri.add(new ArrayList<Integer>(row)) ; 
            }
            return tri ; 


        
        
        
    }
}