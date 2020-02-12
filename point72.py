import re
import string

class Solution:
    def convert(self, lst):
        return [self.helper(date) for date in lst]

    def helper(self, string):
        month = int(string[5:7])
        if month < 4:
            return string[:4] + 'Q1'
        elif month < 7:
            return string[:4] + 'Q2'
        elif month < 10:
            return string[:4] + 'Q3'
        else:
            return string[:4] + 'Q4'

    def getWord(self, sentence):
        words = re.findall(r'\w+', sentence)
        words = re.sub('[{}]'.format(string.punctuation), '', sentence).split()
        return words

    def mostCount(self, arr, k):
        cnt = 0
        tmp = 0
        for i, num in enumerate(arr):
            if tmp + num <= k:
                cnt += 1
                tmp += num
            else:
                tmp += num - arr[i-cnt]
        return cnt


input = ['2019-01-21', '2016-04-01']

output = ['2019Q1', '2016Q2']

sol = Solution()
print(sol.convert(input))

sentence = "Geeksforgeeks,    is best @# Computer Science Portal.!!!"
print(sol.getWord(sentence=sentence))

print(string.punctuation)

print(sol.mostCount([1, 2, 1, 0, 1, 1, 0], 1))