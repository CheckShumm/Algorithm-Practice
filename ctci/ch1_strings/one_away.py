'''
 Description:
 Given two strings see if they are one edit away from being equal

 run time: O(n)
'''

class Solution:

    def one_away(self, s1, s2):
        '''
        :type s1,s2: string
        :rtype: boolean
        '''
        if len(s1) == len(s2):
            l = len(s1)
            return self.replace(s1, s2, l)
        elif len(s1) > len(s2):
            l = len(s1)
            return self.remove(s1, s2, l)
        elif len(s1) < len(s2):
            l = len(s2)
            return self.insert(s1, s2, l)
        else:
            return False


    def replace(self, s1, s2, l):
        flag = 0
        for i in range(l-1):
            if s1[i] is not s2[i]:
                flag += 1
            if flag == 2:
                return False
        return True

    def insert(self, s1, s2, l):
        j = 0
        for i in range(l-1):
            if s1[i] is not s2[j]:
                j += 1
            if j-i == 2:
                return False
            j += 1
        return True

    def remove(self, s1, s2, l):
        j = 0
        for i in range(l-1):
            if s1[i] is not s2[j]:
                i += 1
            if i-j == 2:
                return False
            j += 1
        return True

    def test(self):
        print('one_away Test')
        s1 = ''
        while(s1 is not 'x'):
            s1 = input("Enter string 1...\n")
            s2 = input("Enter string 2...\n")
            print(self.one_away(s1,s2))

if __name__ == "__main__":
    Solution().test()
