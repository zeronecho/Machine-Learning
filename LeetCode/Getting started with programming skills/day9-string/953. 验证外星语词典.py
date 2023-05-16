# 某种外星语也使用英文小写字母，但可能顺序 order 不同。字母表的顺序（order）是一些小写字母的排列。
#
# 给定一组用外星语书写的单词 words，以及其字母表的顺序 order，只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回 false。

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 将字母表的顺序存储在一个字典中
        order_dict = {char: i for i, char in enumerate(order)}

        # 检查相邻的单词是否按字典序排列
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            # 逐个比较两个单词中的字符，直到找到不同的字符
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    # 如果两个单词中的字符在字母表中的顺序不同，根据字母表顺序返回结果
                    if order_dict[word1[j]] > order_dict[word2[j]]:
                        return False
                    break
            else:
                # 如果一个单词是另一个单词的前缀，则根据它们的长度判断它们在字典序中的顺序
                if len(word1) > len(word2):
                    return False

        return True

    # # 官方题解
    # def isAlienSorted(self, words: List[str], order: str) -> bool:
    #     index = {c: i for i, c in enumerate(order)}
    #     return all(s <= t for s, t in pairwise([index[c] for c in word] for word in words))

