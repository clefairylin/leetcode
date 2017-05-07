# -*- coding: utf-8 -*-
import re


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row_1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        row_2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        row_3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        result = []

        for word in words:
            mark = True
            if word[0].lower() in row_1:
                row = row_1
            elif word[0].lower() in row_2:
                row = row_2
            else:
                row = row_3
            for cha in word:
                if cha.lower() not in row:
                    mark = False
                    break
            if mark is True:
                result.append(word)
        return result
