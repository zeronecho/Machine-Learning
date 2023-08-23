class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sort(head):
    # 递归终止条件：链表为空或只有一个节点
    if not head or not head.next:
        return head

    # 使用快慢指针找到链表的中点
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    # 递归地对两个子链表进行排序
    left = merge_sort(head)
    right = merge_sort(mid)

    # 合并两个有序链表
    return merge(left, right)

def merge(l1, l2):
    dummy = ListNode(0)
    curr = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    # 处理剩余的节点
    if l1:
        curr.next = l1
    if l2:
        curr.next = l2

    return dummy.next

# 创建链表
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

# 排序链表
sorted_head = merge_sort(head)

# 打印排序后的链表
curr = sorted_head
while curr:
    print(curr.val, end=" ")
    curr = curr.next

# 在上面的代码中，我们定义了一个链表节点类 ListNode，包含了值 val 和指向下一个节点的指针 next。然后，我们实现了 merge_sort 函数来对链表进行归并排序。
# 归并排序的主要思想是通过递归将链表拆分成较小的子链表，然后再将这些子链表进行合并。在 merge_sort 函数中，我们首先使用快慢指针找到链表的中点，将链表分为两半。
# 然后递归地对两个子链表调用 merge_sort 函数进行排序。最后，我们调用 merge 函数将两个有序的子链表合并成一个有序链表。
# merge 函数用于合并两个有序链表。我们使用一个哑节点 dummy 和一个当前节点 curr 来构建合并后的链表。
# 我们比较两个链表当前节点的值，选择较小的节点连接到结果链表中，并将对应的指针向后移动。当其中一个链表遍历完后，我们将另一个链表的剩余部分连接到结果链表的末尾。
# 最后，我们创建一个示例链表并调用 merge_sort 函数对链表进行排序。然后遍历排序后的链表并输出结果。
# 这样，我们就通过归并排序算法实现了链表的排序。
