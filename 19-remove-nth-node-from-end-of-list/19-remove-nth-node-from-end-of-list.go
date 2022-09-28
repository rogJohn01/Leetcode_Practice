/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    

    dum := &ListNode{Next: head} 
    slow , fast := dum , dum 

    for i := 0; i <= n ; i++ { 
        fast = fast.Next 
    }

    for fast != nil {
        fast = fast.Next 
        slow = slow.Next 
    }

    slow.Next = slow.Next.Next 

    return dum.Next 
    }
