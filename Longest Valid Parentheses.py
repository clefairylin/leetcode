class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = right = longest_valid = 0
        for i in range(0, len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1
                if right == left:
                    longest_valid = max(longest_valid, 2 * right)
                elif right > left:
                    left = right = 0
        left = right = 0
        for j in range(-1, -len(s)-1, -1):
            if s[j] == ")":
                right += 1
            else:
                left += 1
                if left == right:
                    longest_valid = max(longest_valid, 2 * left)
                elif left > right:
                    left = right = 0
        return longest_valid

        # # by stack
        # longest_valid, stack_list = 0, [-1]
        # for i in range(0, len(s)):
        #     if s[i] == "(":
        #         stack_list.append(i)
        #     else:
        #         stack_list.pop()
        #         if len(stack_list) == 0:
        #             stack_list.append(i)
        #         else:
        #             longest_valid = max(longest_valid, i - stack_list[-1])
        # return longest_valid
