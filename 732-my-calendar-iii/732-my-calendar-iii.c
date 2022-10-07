


typedef struct {
    int Max; 
    int Cnt; 
    int* Time;
    int* KBook;
    

} MyCalendarThree;


MyCalendarThree* myCalendarThreeCreate() {
        MyCalendarThree* obj = malloc(sizeof(MyCalendarThree));
        obj->Max = 1; 
        obj->Cnt = 0 ; 
        obj->Time = malloc(sizeof(int)*802);
        obj->KBook = malloc(sizeof(int)*802);
        return obj; 
    
}

int myCalendarThreeBook(MyCalendarThree* obj, int start, int end) {
    
    int i = 0; 
    while( i < obj->Cnt && obj->Time[i] <= start){
        i++; 
    }
    int j = obj->Cnt-1; 
    while( j>= 0 && obj->Time[j] >= end ) {
        obj->Time[j+2] = obj->Time[j];
        obj->KBook[j+2] = obj->KBook[j];
        j-- ;
    }
    int tail = j+2 ; 
    obj->Time[tail] = end; 

    while(j>= i) {
        obj->Time[j+1] = obj->Time[j] ;
        obj->KBook[j+1] = obj->KBook[j] +1;
        if( obj->KBook[j+1] > obj->Max) {
            obj->Max = obj->KBook[j+1] ;
        } 
        j-- ; 
    }
    obj->Time[i] = start; 
    if(i==0) {
        obj->KBook[i] = 1; 
    } else { 
        obj->KBook[i] = obj->KBook[i-1] +1; 
        if(obj->KBook[i] > obj->Max){
            obj->Max = obj->KBook[i]; 
        }
    }
    obj->KBook[tail] = obj->KBook[tail-1] -1 ; 
    obj->Cnt +=2 ; 
    return obj->Max; 
}

void myCalendarThreeFree(MyCalendarThree* obj) {
        
        free(obj->KBook); 
        free(obj->Time); 
        free(obj) ; 
}

/**
 * Your MyCalendarThree struct will be instantiated and called as such:
 * MyCalendarThree* obj = myCalendarThreeCreate();
 * int param_1 = myCalendarThreeBook(obj, start, end);
 
 * myCalendarThreeFree(obj);
*/