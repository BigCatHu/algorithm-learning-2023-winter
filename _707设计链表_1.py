class MyLinkedList:

    def __init__(self):
        self.head=ListNode(0)
        # p = self.head

    # 获取链表中第 index 个节点的值
    def get(self, index: int) -> int:
        # 索引为负无效
        if index < 0:
            return -1
        p = self.head
        for i in range(index+1):
            # 超出链表长度无效
            if p.next is None:
                return -1
            else:
                p = p.next
        return p.val

    # 在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node

    # 将值为 val 的节点追加到链表的最后一个元素。
    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = node


    def addAtIndex(self, index: int, val: int) -> None:
        node = ListNode(val)
        p = self.head
        if index < 0:
            node.next = self.head.next
            self.head.next = node
        else:
            for i in range(0,index):
                if p.next is None:
                    p.next = node
                p=p.next
            node.next=p.next
            p.next=node

    def deleteAtIndex(self, index: int) -> None:
        p=self.head
        if index<0:
            return
        for i in range(index):           
            p=p.next
            if p.next == None and i < index-1:
                return
        if p.next is not None:
            p.next=p.next.next
            
class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
