class MyCalendar {
    List<int[]> cal ; 
    
    
    public MyCalendar() {
        cal = new ArrayList() ; 
        
    }
    
    public boolean book(int s, int e) {
        
        for(int[] se: cal){
            if(se[0] < e && s < se[1] ) return false ; 
        }
        cal.add(new int[]{s ,e }) ;
        return true ; 
        
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */