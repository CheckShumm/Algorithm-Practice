'''
 Description:
 given string s, and its length l
 replace all spaces with %20

 run time:
'''

class Solution:

    def URLify(self, s, l):
        '''
        :type s: string
        :type l: integer
        :rtype: string
        '''
        sol = ''
        space = False

        for c in s:
            if c is not ' ':
                sol += c
                space = False
            elif c is ' ' and space is False:
                sol += "%20"
                space = True

        return sol

    def test(self):
        print('URLify Test')
        s = ''
        while(s is not 'x'):
            s = input("Enter string\n")
            print(self.URLify(s, 2))
if __name__ == "__main__":
    Solution().test()
