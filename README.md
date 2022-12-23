# 2023冬季
该仓库仅用于记录2023年寒假期间备战蓝桥杯python的学习，参考书籍《python数据结构与算法》
## 设计链表
单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。链表的长度不能直接获取，需要遍历存储至size中，不合法的索引是 (<0 or > size)的，链表遍历时，通常会先将p指针指到self.head.
### 链表
「链表 Linked List」是一种线性数据结构，其中每个元素都是单独的对象，各个元素（一般称为结点）之间通过指针连接。由于结点中记录了连接关系，因此链表的存储方式相比于数组更加灵活，系统不必保证内存地址的连续性。
链表的「结点 Node」包含两项数据，一是结点「值 Value」，二是指向下一结点的「指针 Pointer」（或称「引用 Reference」）。

```python
""" 初始化链表 1 -> 3 -> 2 -> 5 -> 4 """
# 初始化各个结点 
n0 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(5)
n4 = ListNode(4)
# 构建引用指向
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
```
## 队列
在循环队列中，当队列为空，可知 $\textit{front}=\textit{rear}$；而当所有队列空间全占满时，也有 $\textit{front}=\textit{rear}$。为了区别这两种情况，假设队列使用的数组有 $\textit{capacity} $个存储空间，则此时规定循环队列最多只能有capacity - 1个队列元素，当循环队列中只剩下一个空存储单元时，则表示队列已满。根据以上可知，队列判空的条件是 $\textit{front}=\textit{rear}$，而队列判满的条件是 front = (rear+ 1)  mod capacity。
对于一个固定大小的数组，只要知道队尾$ \textit{rear}$ 与队首 $\textit{front}$，即可计算出队列当前的长度：
\begin{eqution}
(\textit{rear} - \textit{front} + \textit{capacity}) \bmod \textit{capacity}
\end{eqution}
循环队列的属性如下:

$\textit{elements}$：一个固定大小的数组，用于保存循环队列的元素。
$\textit{capacity}$：循环队列的容量，即队列中最多可以容纳的元素数量。
$\textit{front}$：队列首元素对应的数组的索引。
$\textit{rear}$：队列尾元素对应的索引的下一个索引。
[leetcode—link](https://leetcode.cn/problems/design-circular-queue/solution/she-ji-xun-huan-dui-lie-by-leetcode-solu-1w0a/)
```python
class MyCircularQueue:
    def __init__(self, k: int):
        self.front = self.rear = 0
        self.elements = [0] * (k + 1)

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.elements[self.rear] = value
        self.rear = (self.rear + 1) % len(self.elements)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % len(self.elements)
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.elements[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.elements[(self.rear - 1) % len(self.elements)]

    def isEmpty(self) -> bool:
        return self.rear == self.front

    def isFull(self) -> bool:
        return (self.rear + 1) % len(self.elements) == self.front
```


