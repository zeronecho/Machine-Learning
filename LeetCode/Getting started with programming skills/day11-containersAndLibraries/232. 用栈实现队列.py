# https://leetcode.cn/problems/implement-queue-using-stacks/?envType=study-plan&id=programming-skills-beginner&plan=programming-skills&plan_progress=x5t930sg

# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：
#
# 实现 MyQueue 类：
#
# void push(int x) 将元素 x 推到队列的末尾
# int pop() 从队列的开头移除并返回元素
# int peek() 返回队列开头的元素
# boolean empty() 如果队列为空，返回 true ；否则，返回 false
# 说明：
#
# 你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。

class MyQueue:
    def __init__(self):
        self.in_stack = []   # 输入栈
        self.out_stack = []  # 输出栈

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if not self.out_stack:
            self.move_elements()
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            self.move_elements()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def move_elements(self) -> None:
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

# 在这个实现中，我们使用两个栈，一个输入栈 in_stack 和一个输出栈 out_stack。
# 当需要弹出或查看队头元素时，如果输出栈为空，则将输入栈的所有元素弹出并压入输出栈，使得最先进入队列的元素位于输出栈的栈顶。
# 这样，我们就可以使用输出栈的栈顶元素来实现 pop 和 peek 操作，而输入栈和输出栈的状态变化也保证了先入先出的顺序。
