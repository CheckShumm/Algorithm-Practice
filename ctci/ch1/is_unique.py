'''
 Does a given string contain unique characters
 without the use additional data structures
 run time: O(nlogn)
'''

class Solution:

    def is_unique(self, s):
        '''
        :type s: string
        :rtype: boolean
        '''

        # sort string
        sorted_s = ''.join(sorted(s))

        # check for duplicates
        for i in range(len(sorted_s)-1):
            if sorted_s[i] == sorted_s[i+1]:
                return False

        return True

    def test(self):

        print('Unique String Test')
        s = ''
        while(s is not 'x'):
            s = input("Enter string..\n")
            print(self.is_unique(s))

if __name__ == "__main__":
    Solution().test()
