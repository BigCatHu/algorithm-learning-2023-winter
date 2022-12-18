# https://leetcode.cn/problems/flatten-a-multilevel-doubly-linked-list/solution/bian-ping-hua-duo-ji-shuang-xiang-lian-b-383h/
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

# 原官方解答      
class Solution():
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node: "Node") -> "Node":
            cur = node
            # 记录链表的最后一个节点
            last = None
            while cur:
                nxt = cur.next
                # 如果有子节点，那么首先处理子节点
                if cur.child:
                    # 递归
                    child_last = dfs(cur.child)
                    nxt = cur.next
                    # 将 node 与 child 相连
                    cur.next = cur.child
                    cur.child.prev = cur

                    # 如果 nxt 不为空，就将 last 与 nxt 相连
                    if nxt:
                        child_last.next = nxt
                        nxt.prev = child_last

                    # 将 child 置为空
                    cur.child = None
                    last = child_last
                else:
                    last = cur
                cur = nxt
            return last

        dfs(head)
        return head

#优化版
class Solution():
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def flatten_iter(node: "Node") -> "Node":
            cur = node
            last = None
            stack = []
            while cur or stack:
                if cur:
                    # If there is a child, push the current node and the next node onto the stack
                    if cur.child:
                        if cur.next:
                            stack.append((cur, cur.next))
                        # Replace the current node's child with the current node's next
                        cur.next = cur.child
                        cur.child.prev = cur
                        cur.child = None
                    last = cur
                    cur = cur.next
                else:
                    # Pop the top node and next node from the stack
                    cur, nxt = stack.pop()
                    # Connect the last node with the next node
                    last.next = nxt
                    nxt.prev = last
                    cur = nxt
            return last

        flatten_iter(head)
        return head
