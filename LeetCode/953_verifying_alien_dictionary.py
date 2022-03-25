'''
https://leetcode.com/problems/verifying-an-alien-dictionary/

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match,
and the second string is shorter (in size.)
According to lexicographical rules "apple" > "app",
because 'l' > '∅', where '∅' is defined as the blank
character which is less than any other character.
'''

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {}
        for index, val in enumerate(order):
            order_dict[val] = index

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            for j in range(len(word1)):
                if j >= len(word2) : return False
                if word1[j] != word2[j]:
                    if order_dict[word1[j]] > order_dict[word2[j]] : return False
                    break

        return True
