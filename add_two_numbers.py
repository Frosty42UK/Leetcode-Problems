class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:       
        l3_head = None
        current = None
        carry = 0
        
        while l1 is not None or l2 is not None or carry > 0:
            
            if l1 is not None:
                n1 = l1.val
            else:
                n1 = 0
                
            if l2 is not None:
                n2 = l2.val
            else:
                n2 = 0
                
            total_sum = n1 + n2 + carry # error since l3 is edited again and again (temp variable required) + l1 and l2 lists are not traversed correctly
           
            if total_sum > 9:
                carry = 1
                total_sum %= 10 
            else: 
                carry = 0
                
            # current = current.next # error current.next points to nothing
            if current is None:
                new_node = ListNode(total_sum)
                l3_head = new_node
                current = new_node
            else: 
                new_node = ListNode(total_sum)
                current.next = new_node
                current = current.next
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:    
                l2 = l2.next
                
        return l3_head
    
# 342 + 465 = 807
# 342 - reversed -> 243
# 465 - reversed -> 564

# 1. Create the nodes from tail to head
dummy7 = ListNode(9)            # The tail: 3 -> None
dummy6 = ListNode(9, dummy7)    # The middle: 4 -> 3
dummy5 = ListNode(9, dummy6)            # The tail: 3 -> None
dummy4 = ListNode(9, dummy5)    # The middle: 4 -> 3
dummy3 = ListNode(9, dummy4)            # The tail: 3 -> None
dummy2 = ListNode(9, dummy3)    # The middle: 4 -> 3
l1 = ListNode(9, dummy2)     # The head: 2 -> 4 -> 3

dum4 = ListNode(9)
dum3 = ListNode(9, dum4)
dum2 = ListNode(9, dum3)
l2 = ListNode(9, dum2)
# 9 -> 9 -> 9 -> 9

solver = Solution()
answer = solver.addTwoNumbers(l1, l2)

# 2. Print by traversing the list starting from the head (dummy)
current = answer
while current is not None:
    print(current.val, end = "")
    if current.next is not None:
        print("->", end ="")
    else:
        print("\n")
    current = current.next
    

