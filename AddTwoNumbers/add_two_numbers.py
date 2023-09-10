class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = cur = ListNode(-1)
        carry = 0
        while  l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum_ = l1_val+l2_val+carry
            carry = sum_//10
            remain = sum_%10
            cur.next = ListNode(remain)
            # print(cur)
            cur = cur.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            cur.next = ListNode(carry)
        return start.next