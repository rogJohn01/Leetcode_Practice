type MyCircularQueue struct {
	
	sl  []int 
	front int 
	rear int 
	size int 
}

func Constructor(k int) MyCircularQueue {
	return MyCircularQueue {
		size : k , 
		sl : make([]int , k) , 
		front : 0 , 
		rear : -1 , 
	}
}


func (q *MyCircularQueue) EnQueue(value int) bool {

	if q.IsFull() {
		return false }
	
	q.rear ++ 
	q.sl[q.rear % q.size] = value 
	return true 
	
}


func (q *MyCircularQueue) DeQueue() bool {
	if q.IsEmpty(){
		return false 
	}
	q.front ++ 
	return true 

}


func (q *MyCircularQueue) Front() int {
	if q.IsEmpty() {
		return -1 
	}
	return q.sl[q.front % q.size] 

}


func (q *MyCircularQueue) Rear() int {
	if q.IsEmpty() {
		return -1 
	}
	return q.sl[q.rear % q.size] 

}


func (q *MyCircularQueue) IsEmpty() bool {
	return q.rear < q.front 
}


func (q *MyCircularQueue) IsFull() bool {
	return q.rear - q.front == q.size -1 
}


/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * obj := Constructor(k);
 * param_1 := obj.EnQueue(value);
 * param_2 := obj.DeQueue();
 * param_3 := obj.Front();
 * param_4 := obj.Rear();
 * param_5 := obj.IsEmpty();
 * param_6 := obj.IsFull();
 */