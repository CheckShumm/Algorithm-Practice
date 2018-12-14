'''
 Description:
 Given two strings, check if one is a permutation of the other
 run time:
'''

class Solution:

    def is_permutation(self, s1, s2):
        '''
        :type s1,s2: string
        :rtype: boolean
        '''

        if len(s1) is not len(s2):
            return False

        s1_char_freq = self.get_char_freq(s1)
        s2_char_freq = self.get_char_freq(s2)

        for key in s1_char_freq:
            if key not in s2_char_freq:
                return False
            elif s1_char_freq[key] is not s2_char_freq[key]:
                return False

        return True;

    # given string return dict with char freq
    def get_char_freq(self, s):
        s_char_freq = {}
        for c in s:
            if c not in s_char_freq:
                s_char_freq[c] = 1
            else:
                s_char_freq[c] += 1

        return s_char_freq

    def test(self):
        print('is_permutation Test')
        s1 = ''
        s2 = ''
        while (s1 is not 'x' or s2 is not 'x'):
            s1 = input("Enter first string\n")
            s2 = input("Enter second string\n")
            print(self.is_permutation(s1,s2))

if __name__ == "__main__":
    Solution().test()
