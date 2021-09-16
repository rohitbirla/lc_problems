from src.IsPalindrome import isPalindrome
from src.ImplementstrStr import strStr
from src.LengthOfLastWord import lengthOfLastWord
from src.PlusOne import plusOne
from src.RemoveDuplicates import removeDuplicates
from src.ReverseInteger import reverse
from src.RomanToInteger import romanToInt
from src.TwoSum import twoSum

def test_isPalindrome():
    assert isPalindrome("malayalam") == True

def test_strStr():
    assert strStr("hello","ll") == 2

def test_lengthOfLastWord():
    assert lengthOfLastWord("Hello World") == 5

def test_plusOne():
    assert plusOne([4,3,2,1]) == [4,3,2,2]

def test_removeDuplicates():
    assert removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5

def test_reverse():
    assert reverse(-123) == -321

def test_romanToInt():
    assert romanToInt("LVIII") == 58

def test_twoSum():
    assert twoSum([3,2,4],6) == [1,2]








