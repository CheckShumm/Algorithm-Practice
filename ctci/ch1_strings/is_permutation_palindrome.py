'''
 Description:
 Given a string verify if it is a permutation of a palindrome

 run time:
'''

class Solution:

    def is_permutation_palindrome(self, s):
        '''
        :type s: string
        :rtype: boolean
        '''
        # for a string to be a permutation of a permutation of a palindrome
        # character frequencies must be in power of 2, except for 1 char

        char_freq = {}

        for c in s:
            if c not in char_freq:
                char_freq[c] = 1
            else:
                char_freq[c] += 1

        flag = 0
        for key in char_freq:
            if (char_freq[key] % 2) > 0:
                if flag == 0:
                    flag +=1
                else:
                    return False

        return True


    def test(self):
        print('is_permutation_palindrome Test')
        s = ''
        while(s is not 'x'):
            s = input("Enter ...\n")
            print(self.is_permutation_palindrome(s))

if __name__ == "__main__":
    Solution().test()
