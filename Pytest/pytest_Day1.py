# 1. Compare 2 number and display appropriate message

def compare_two_number():
    num1 = 10
    num2  = 10

    if num1 == num2:
        print("pass")
    else:
        print("fail")

#compare_two_number()

# Compare two umbers using pytest library
# pip install pytest
import pytest
import pytest_check as check

'''
# Hard assertion....
def test_compare_two_number_hard_assertion():
    print("Test started.....")
    num1 = 10
    num2 = 20
    assert num1 < num2, "num1 is lesser than num2"
    assert num1 == num2, "Two numbers are not equal"
    assert num1 != num2, "Two numbers are not equal"
    print("Test completed...")
'''

# Soft assertion....
def test_compare_two_number_hard_assertion():
    print("Test started.....")
    num1 = 10
    num2 = 20
    assert num1 < num2, "num1 is lesser than num2"
    assert num1 == num2, "Two numbers are not equal"
    assert num1 != num2, "Two numbers are not equal"
    print("Test completed...")
