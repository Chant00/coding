### 位运算
#### 算法解释
常用技巧

位运算是算法题里比较特殊的一种类型，它们利用二进制位运算的特性进行一些奇妙的优化 和计算。
常用的位运算符号包括：“∧”按位异或、“&”按位与、“|”按位或、“∼”取反、“<<” 算术左移和“>>”算术右移。
以下是一些常见的位运算特性，其中 0s 和 1s 分别表示只由 0 或 1 构成的二进制数字。
```
x ^ 0s = x    x ^ 1s = ~x    x ^ x = 0

x & 0s = 0    x & 1s = x     x & x = x

x | 0s = x    x | 1s = 1s    x | x = x
```
除此之外，n & (n - 1) 可以去除 n 的位级表示中最低的那一位，例如对于二进制表示 11110100 ，减去 1 得到 11110011，
这两个数按位与得到 11110000。n & (-n) 可以得到 n 的位级表示中最低的那一位，
例如对于二进制表示 11110100，取负得到 00001100，这两个数按位与得到 00000100。 
还有更多的并不常用的技巧，若读者感兴趣可以自行研究，这里不再赘述。

练习TODO：

基础难度

268. Missing Number (Easy)

Single Number 的变种题。除了利用二进制，也可以使用高斯求和公式。

693. Binary Number with Alternating Bits (Easy)

利用位运算判断一个数的二进制是否会出现连续的 0 和 1。

476. Number Complement (Easy)

二进制翻转的变种题。

进阶难度

260. Single Number III (Medium)

Single Number 的 follow-up，需要认真思考如何运用位运算求解。

####
快速幂参考：
1. [python整数快速幂和矩阵快速幂](https://blog.csdn.net/bianxia123456/article/details/105167294/)
2. [leetcode 50. Pow(x, n)官方题解](https://leetcode-cn.com/problems/powx-n/solution/powx-n-by-leetcode-solution/)