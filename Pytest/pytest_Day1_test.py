# pip install pytest
import pytest
import pytest_check as check
# 1. Compare 2 number and display appropriate message
'''
def compare_two_number():
    num1 = 10
    num2  = 10

    if num1 == num2:
        print("pass")
    else:
        print("fail")

#compare_two_number()

# Compare two umbers using pytest library



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

# Soft Assertion

def test_compare_twoNumbers_soft_assertion():
    check.is_true(2==2,"Not equal 1")
    check.is_true(1 == 1, "not equal 2")
    check.equal(1,1,"numbers not equal 3")
    check.not_equal(1,2,"both numbers are equals")
    check.is_false(1==2,"both are numbers are equal 4")
