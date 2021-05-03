# 假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。每个 people[i] = [hi, ki] 表示第 i 
# 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。 
# 
#  请你重新构造并返回输入数组 people 所表示的队列。返回的队列应该格式化为数组 queue ，其中 queue[j] = [hj, kj] 是队列中第
#  j 个人的属性（queue[0] 是排在队列前面的人）。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# 输出：[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
# 解释：
# 编号为 0 的人身高为 5 ，没有身高更高或者相同的人排在他前面。
# 编号为 1 的人身高为 7 ，没有身高更高或者相同的人排在他前面。
# 编号为 2 的人身高为 5 ，有 2 个身高更高或者相同的人排在他前面，即编号为 0 和 1 的人。
# 编号为 3 的人身高为 6 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
# 编号为 4 的人身高为 4 ，有 4 个身高更高或者相同的人排在他前面，即编号为 0、1、2、3 的人。
# 编号为 5 的人身高为 7 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
# 因此 [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] 是重新构造后的队列。
#  
# 
#  示例 2： 
# 
#  
# 输入：people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
# 输出：[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= people.length <= 2000 
#  0 <= hi <= 106 
#  0 <= ki < people.length 
#  题目数据确保队列可以被重建 
#  
#  Related Topics 贪心算法 
#  👍 859 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """从高到底
        核心思想：高个子先站好位，矮个子插入到K位置上，前面肯定有K个高个子，矮个子再插到前面也满足K的要求
        当我们放入第 i 个人时，只需要将其插入队列中，使得他的前面恰好有 k_i 个人即可。
        """
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = list()
        for person in people:
            # ans[person[1]:person[1]] = [person]
            ans.insert(person[1], person)
        return ans

    def reconstructQueue1(self, people: List[List[int]]) -> List[List[int]]:
        """从低到高
        如果我们在初始时建立一个包含 n 个位置的空队列，而我们每次将一个人放入队列中时，
        会将一个「空」位置变成「满」位置，那么当我们放入第 i 个人时，
        我们需要给他安排一个「空」位置，并且这个「空」位置前面恰好还有 k_i 个「空」位置，用来安排给后面身高更高的人。
        也就是说，第 i 个人的位置，就是队列中从左往右数第 k_i+1 个「空」位置。
        """
        people.sort(key=lambda x: (x[0], -x[1]))
        n = len(people)
        ans = [[] for _ in range(n)]
        for person in people:
            spaces = person[1] + 1
            #  k_i+1 个「空」位置
            for i in range(n):
                if not ans[i]:
                    spaces -= 1
                    if spaces == 0:
                        ans[i] = person
                        break
        return ans
# leetcode submit region end(Prohibit modification and deletion)
