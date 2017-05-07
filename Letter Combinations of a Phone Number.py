from functools import reduce


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {
            "1": "*",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": " "
        }

        if digits == "":
            return []
        return reduce(lambda cur, digit: [x + y for x in cur for y in mapping[digit]], digits, [""])