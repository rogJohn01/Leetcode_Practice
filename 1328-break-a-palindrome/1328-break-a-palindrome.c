

char * breakPalindrome(char * pal){
    
    int len = strlen(pal);
    if (len ==1) return ""; 
    for(int i=0 ; i < len/2 ; i++){
        if( pal[i] != 'a' ){
            pal[i] = 'a' ;
            return pal ;
        }  
    }
    pal[len-1] = 'b'; 
    return pal ; 
    
    
}