class Solution {
    public int countCollisions(String dir) {
        
        
        	int left = 0 , right = dir.length()-1;

	while (left < dir.length() && dir.charAt(left) =='L'){
		left ++; 
	}
	while (right >=0 && dir.charAt(right) =='R'){
		right --;
	}

	int cnt =0;
	for (int i=left ; i <=right; i++){
		if (dir.charAt(i) != 'S') {
			cnt ++;
		}
	}
	return cnt; 
    }
}