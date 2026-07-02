class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = ListNode()
        valor_actual = x
        extra = 0

        while l1 or l2 or extra:
            valor_1 = l1.val if l1 else 0
            valor_2 = l2.val if l2 else 0

            suma = valor_1 + valor_2 + extra
            extra = suma // 10
            digito_actual = suma % 10

            valor_actual.next = ListNode(digito_actual)
            valor_actual = valor_actual.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return x.next
            
