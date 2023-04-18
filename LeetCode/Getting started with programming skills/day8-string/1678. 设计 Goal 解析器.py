# https://leetcode.cn/problems/goal-parser-interpretation/?envType=study-plan&id=programming-skills-beginner&plan=programming-skills&plan_progress=x5t930sg

# 请你设计一个可以解释字符串 command 的 Goal 解析器 。command 由 "G"、"()" 和/或 "(al)" 按某种顺序组成。
# Goal 解析器会将 "G" 解释为字符串 "G"、"()" 解释为字符串 "o" ，"(al)" 解释为字符串 "al" 。然后，按原顺序将经解释得到的字符串连接成一个字符串。
# 给你字符串 command ，返回 Goal 解析器 对 command 的解释结果。

class Solution:
    def interpret(self, command: str) -> str:
        res = []
        for i, c in enumerate(command):
            if c == 'G':
                res.append(c)
            elif c == '(':
                res.append('o' if command[i + 1] == ')' else 'al')
        return ''.join(res)

