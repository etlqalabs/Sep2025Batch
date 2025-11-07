# test run in parallel
import pandas as pd
import pytest
import time
import os


def test_test_case_1():
    print("Test case 1 execution started")
    assert True,"Tets case 1 failed"
    print("Test case 1 execution completed")
    time.sleep(2)


def test_test_case_2():
    print("Test case 2 execution started")
    assert True, "Tets case 2 failed"
    print("Test case 2 execution completed")
    time.sleep(2)

def test_test_case_3():
    print("Test case 3 execution started")
    assert False, "Tets case 3 failed"
    print("Test case 3 execution completed")
    time.sleep(2)

def test_test_case_4():
    print("Test case 4 execution started")
    assert True, "Tets case 4 failed"
    print("Test case 4 execution completed")
    time.sleep(2)

def test_test_case_5():
    print("Test case 5 execution started")
    assert True, "Tets case 5 failed"
    print("Test case 5 execution completed")
    time.sleep(2)

