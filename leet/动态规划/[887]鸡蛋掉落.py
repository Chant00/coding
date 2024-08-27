# 给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。
# 
#  已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。 
# 
#  每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <= n）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎
# ，则可以在之后的操作中 重复使用 这枚鸡蛋。 
# 
#  请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？ 
# 
#  示例 1： 
# 
#  
# 输入：k = 1, n = 2
# 输出：2
# 解释：
# 鸡蛋从 1 楼掉落。如果它碎了，肯定能得出 f = 0 。 
# 否则，鸡蛋从 2 楼掉落。如果它碎了，肯定能得出 f = 1 。 
# 如果它没碎，那么肯定能得出 f = 2 。 
# 因此，在最坏的情况下我们需要移动 2 次以确定 f 是多少。 
#  
# 
#  示例 2： 
# 
#  
# 输入：k = 2, n = 6
# 输出：3
#  
# 
#  示例 3： 
# 
#  
# 输入：k = 3, n = 14
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= 100 
#  1 <= n <= 10⁴ 
#  
# 
#  Related Topics 数学 二分查找 动态规划 👍 1004 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        """李永乐老师讲解写法，逻辑没问题，但是superEggDrop(4, 5000))会超时，所以这里叠加二分法优化
        动态规划+二分 复杂度O(kn2) 降低至 O(knlogn)
        官方题解的方法1相同，只是官解用的带记忆的递归，这里用的循环。
        Mi(n,k) = max(M(i,k-1), M(n-i,k)) + 1
        M(n,k) = min(M1,M2,...Mn)
        """
        #  dp[i][j]表示共i层楼j个鸡蛋时最少要试几次保证能找到临界点
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            # 鸡蛋数量为1时，只能一层层从低到高去试，所以共i次
            dp[i][1] = i
            for j in range(2, k + 1):
                # dp[x-1][j-1]随着h递增，dp[i - x][j]随着x递减，min(max())其实两个函数的就是交点
                # 二分查找，dp[mid-1][j-1] > dp[i - mid][j] 则要找的那个x'就在mid右边，否则在mid左边
                # 最后比较交点左右两侧的两个值就可以，不用遍历计算全部
                l, r = 1, i
                while l + 1 < r:
                    mid = l + (r - l) // 2
                    t1 = dp[mid - 1][j - 1]
                    t2 = dp[i - mid][j]
                    if t1 < t2:
                        l = mid
                    elif t1 > t2:
                        r = mid
                    elif t1 == t2:
                        l = r = mid

                dp[i][j] = min(max(dp[t - 1][j - 1], dp[i - t][j]) + 1 for t in (l, r))
                # 原本要遍历i次全部计算，二分法使得这一层的复杂度从O(n)降低为O(log(n))
                # dp[i][j] = n  # 最大也就n次
                # for x in range(1, i + 1):
                #     Mh = max(dp[x - 1][j - 1], dp[i - x][j]) + 1
                #     dp[i][j] = min(dp[i][j], Mh)
        return dp[n][k]

    def superEggDrop0(self, k: int, n: int) -> int:
        """李永乐老师讲解写法，逻辑没问题，但是superEggDrop(4, 5000))会超时，需要用二分法优化，官方题解的方法1
        暴力法 复杂度O(kn2)
        Mi(n,k) = max(M(i,k-1), M(n-i,k)) + 1
        M(n,k) = min(M1,M2,...Mn)
        """
        #  dp[i][j]表示共i层楼j个鸡蛋时最少要试几次保证能找到临界点
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            # 鸡蛋数量为1时，只能一层层从低到高去试，所以共i次
            dp[i][1] = i
            for j in range(2, k + 1):
                dp[i][j] = n  # 最大也就n次
                for h in range(1, i + 1):
                    Mh = max(dp[h - 1][j - 1], dp[i - h][j]) + 1
                    dp[i][j] = min(dp[i][j], Mh)
        # return dp[i][j]
        return dp[n][k]

    def superEggDrop2(self, k: int, n: int) -> int:
        """官方题解方法3：数学法。时间复杂度：O(kn)
        dp[i][j] 不存储直接的答案，转换思路，存一个中间变量，同时能写出状态转移方程就行。

        反过来想这个问题：如果我们可以做 t 次操作，而且有 k 个鸡蛋，那么我们能找到答案的最高的 n 是多少？
        我们设 f(t,k) 为在上述条件下的 n。如果我们求出了所有的 f(t,k)，那么只需要找出最小的满足 f(t,k)≥n 的 t。

        那么我们如何求出 f(t,k) 呢？我们还是使用动态规划。因为我们需要找出最高的 n，因此我们不必思考到底在哪里扔这个鸡蛋，
        我们只需要扔出一个鸡蛋，看看到底发生了什么：
            如果鸡蛋没有碎，那么对应的是 f(t−1,k)，也就是说在这一层的上方可以有 f(t−1,k) 层；
            如果鸡蛋碎了，那么对应的是 f(t−1,k−1)，也就是说在这一层的下方可以有 f(t−1，k−1) 层。
            状态转移方程：f(t,k)=1+f(t−1,k−1)+f(t−1,k)
            边界条件为：当 t≥1 的时候 f(t,1)=t，当 k≥1 时，f(1,k)=1。
        """
        if n == 1:
            return 1
        f = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, k + 1):
            f[1][i] = 1
        # 这个包含在后面的内层循环里了，所以可以省去
        # for i in range(1, n + 1):
        #     f[i][1] = i
        ans = -1
        for i in range(2, n + 1):
            for j in range(1, k + 1):
                f[i][j] = 1 + f[i - 1][j - 1] + f[i - 1][j]
            if f[i][k] >= n:
                ans = i
                break
        return ans

    def superEggDrop2_1(self, k: int, n: int) -> int:
        """
        f[i][j] j个鸡蛋，i次操作下的最大楼层
        碎：下面有f[t-1][k-1]层
        不碎: 上面有f[t-1][k]层
        f[t][k] = 1 + f[t-1][k] + f[t-1][k-1]
        边界：f[1][j]=1, f[i][1]=i
        边界也可以改为：f[0][j]=0, f[i][0]=0，代码就更简洁
        """
        # if n == 1:
        #     return 1
        f = [[0] * (k + 1) for _ in range(n + 1)]
        # for j in range(1, k + 1):
        #     f[1][j] = 1
        ans = -1
        for i in range(1, n + 1):
            for j in range(1, k + 1):  # 从1开始，这种写法就不用单独处理n==1的情况
                # if i == 1:
                #     f[1][j] = 1
                # else:
                f[i][j] = 1 + f[i - 1][j - 1] + f[i - 1][j]
            if f[i][k] >= n:
                ans = i
                break
        return ans

    def superEggDrop2_2(self, k: int, n: int) -> int:
        """while循环，极简代码"""
        # bad case dp[0][..]=0,dp[..][0]=0, 初始化包含了
        f = [[0] * (k + 1) for _ in range(n + 1)]
        i = 0
        while f[i][k] < n:
            i += 1
            for j in range(1, k + 1):
                f[i][j] = 1 + f[i - 1][j - 1] + f[i - 1][j]
        return i


k1 = 3
n1 = 39
print(Solution().superEggDrop(k1, n1))  # 19
print(Solution().superEggDrop0(k1, n1))  # 19
print(Solution().superEggDrop2(k1, n1))  # 19
print(Solution().superEggDrop2_2(k1, n1))  # 19
# leetcode submit region end(Prohibit modification and deletion)
