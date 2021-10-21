# Given the head of a singly linked list, return true if it is a palindrome.

Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false

def isPalindrome(self, head: ListNode) -> bool:
		# Get the length of the list.
		count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1
		
        is_odd = count % 2 == 1
        
		# reverse first half of the list.
        mid = (count + 1) // 2
        prev, curr = None, head
        while mid > 0:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            mid -= 1
        
        if is_odd:
            prev = prev.next

        while prev:
            if prev.val != curr.val:
                return False
            prev = prev.next
            curr = curr.next
        return True