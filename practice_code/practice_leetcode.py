"""
    Leetcode题
"""
class Solution(object):
    """
    两数之和
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
    示例:
    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """遍历列表同时查字典"""
        dct = {}
        for i, n in enumerate(nums): 
            if target - n in dct:
                return [dct[target - n], i]
            dct[n] = i

    """
    给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

    示例 1:
    输入: 123
    输出: 321
    示例 2:
    输入: -123
    输出: -321
    示例 3:
    输入: 120
    输出: 21
    注意:
    假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
    """
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        x = str(x)  # 数字转为字符串
        # 判断是否以0结尾，若是则删除0
        while x.endswith('0'):
            x = ''.join(x[:-1])
        # 若含有负号则
        if '-' in x:
            x = int('-'+(''.join(reversed(x[1:]))))
        else:
            x = int((''.join(reversed(x))))
        # 判断是否为有效数字
        if x>=(-2**31) and x<=(2**31-1):
            return x
        else:
            return 0
        


if __name__ == '__main__':
    question = Solution()
    print(question.twoSum([3,2,4],6))
    print(question.reverse(1534236469))
    