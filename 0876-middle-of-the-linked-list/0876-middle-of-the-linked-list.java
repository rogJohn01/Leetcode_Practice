/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        
        int cnt =0; 
        ListNode node = head ;
        while(head != null){
            head = head.next ;
            cnt ++; 
        }

        int div = cnt /2+1 ; 
        while(div >1){
            node = node.next; 
            div--; 
        }
        return node; 
    }
}