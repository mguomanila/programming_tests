'''
LongestPassword
START
Given a string containing words, find the longest word that satisfies specific conditions.
Programming language:  
You would like to set a password for a bank account. However, there are three restrictions on the format of the password:

it has to contain only alphanumerical characters (a−z, A−Z, 0−9);
there should be an even number of letters;
there should be an odd number of digits.
You are given a string S consisting of N characters. String S can be divided into words by splitting it at, and removing, the spaces. The goal is to choose the longest word that is a valid password. You can assume that if there are K spaces in string S then there are exactly K + 1 words.

For example, given "test 5 a0A pass007 ?xy1", there are five words and three of them are valid passwords: "5", "a0A" and "pass007". Thus the longest password is "pass007" and its length is 7. Note that neither "test" nor "?xy1" is a valid password, because "?" is not an alphanumerical character and "test" contains an even number of digits (zero).

Write a function:

def solution(S)

that, given a non-empty string S consisting of N characters, returns the length of the longest word from the string that is a valid password. If there is no such word, your function should return −1.

For example, given S = "test 5 a0A pass007 ?xy1", your function should return 7, as explained above.

Assume that:

N is an integer within the range [1..200];
string S consists only of printable ASCII characters and spaces.
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.


''' 

'''
simple 
short and simple tests ✘WRONG ANSWER 
got 4 expected 3
1. 0.044 s OK
2. 0.044 s OK
3. 0.044 s WRONG ANSWER,  got 4 expected 3
4. 0.044 s OK

one_word 
tests that contains one word only ✘WRONG ANSWER 
got -1 expected 15
1. 0.044 s OK
2. 0.044 s OK
3. 0.044 s OK
4. 0.044 s OK
5. 0.044 s WRONG ANSWER,  got -1 expected 15
6. 0.044 s OK
7. 0.044 s WRONG ANSWER,  got -1 expected 31

all_alphanumerical 
all words contain only alphanumerical characters ✘WRONG ANSWER 
got 10 expected 9
1. 0.044 s OK
2. 0.044 s WRONG ANSWER,  got 10 expected 9
3. 0.044 s WRONG ANSWER,  got 7 expected 9

▶ extra_characters 
valid passwords joined with some invalid characters ✘WRONG ANSWER 
got -1 expected 27
1. 0.044 s OK
2. 0.044 s OK
3. 0.044 s WRONG ANSWER,  got -1 expected 27
4. 0.044 s WRONG ANSWER,  got -1 expected 19


maximum 
biggest possible tests with mixed types of words ✘WRONG ANSWER 
got 100 expected 1
1. 0.044 s WRONG ANSWER,  got 100 expected 1
2. 0.044 s OK
3. 0.040 s OK
4. 0.040 s WRONG ANSWER,  got -1 expected 199
5. 0.040 s OK
'''

import string


def soln1(S):
    # write your code in Python 3.6
    def isAlphaNumeric(S):
        for s in S:
            if s not in string.ascii_letters and s not in string.digits:
                return False
        return True
    def isEven(S):
        count = 0
        for s in S:
            if s in string.ascii_letters:
                count += 1
        if not count % 2:
            return True
        else: return False
    def isOdd(S):
        count = 0
        for s in S:
            if s in string.digits:
                count += 1
        if not count % 3 or count == 1:
            return True
        else: return False
    n = len(S)
    space = string.whitespace.strip(' ')
    for s in space:
        pass
    words = S.split(' ')
    valid_passwd = []
    for w in words:
        if isAlphaNumeric(w) and isEven(w) and isOdd(w):
            valid_passwd.append(len(w))
    if not len(valid_passwd):
        return -1
    else:
        return max(valid_passwd)


def soln2(S):
    def odd(n):
        if n == 1 or n % 2 != 0: return True
        return False
    def even(n):
        if n % 2 == 0 : return True
        return False
    def check(w):
        valid = True
        letters = string.ascii_letters
        digits = string.digits
        valid_chars = letters + digits
        count_letters, count_digits = 0, 0
        for l in w:
            if l not in valid_chars:
                valid = 0
            else:
                if l in letters:
                    count_letters += 1
                if l in digits:
                    count_digits += 1
            if not valid: return False
        if not odd(count_digits): valid = False
        if not even(count_letters): valid = False
        return valid
    words = S.split(' ')
    wc = []
    for w in words:
        if check(w):
            wc.append(len(w))
    if wc:
        return max(wc)
    else: 
        return -1


if __name__ == '__main__':
    S = "test 5 a0A pass007 ?xy1"
    S1 = "test1 5 a0A passssdd7 pas0d07 ?xy1"
    a = soln1(S)
