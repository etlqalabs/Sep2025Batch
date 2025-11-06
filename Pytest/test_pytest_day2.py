import pandas as pd
import pytest
'''
def test_addition1():
    assert 2+2==4,"addition is wrong"

# Fixture : pre-requiste setup in your test
# We will try to test whether emp_details are matching between source and target files

def test_compare_emp_details_betwwwen_source_and_target_without_fixture():
    print("test started.... ")
    df_source = pd.read_csv("Data/emp_details_source.csv")
    df_target = pd.read_csv("Data/emp_details_target.csv")
    assert df_source.equals(df_target),"Data between source ans target does not match"
    print("test completed.... ")

def test_duplicate_values_in_emp_details_Files__without_fixture():
    print("test started.... ")
    df_source = pd.read_csv("Data/emp_details_source.csv")
    dupes_count_source = df_source.duplicated().sum()
    df_target = pd.read_csv("Data/emp_details_target.csv")
    dupes_count_target = df_target.duplicated().sum()
    assert dupes_count_source == 0,"Source file is having duplicates"
    assert dupes_count_target == 0, "Target file is having duplicates"
    print("test completed.... ")
    '''
'''
@pytest.mark.regression
def test_compare_emp_details_between_source_and_target_using_fixture(source_data_setup,target_data_setup):
    print("test started.... ")
    assert source_data_setup.equals(target_data_setup),"Data between source ans target does not match"
    print("test completed.... ")

@pytest.mark.regression
@pytest.mark.smoke
def test_duplicate_values_in_emp_details_Files__without_fixture(source_data_setup,target_data_setup):
    print("test started.... ")
    dupes_count_source = source_data_setup.duplicated().sum()
    dupes_count_target = target_data_setup.duplicated().sum()
    assert dupes_count_source == 0,"Source file is having duplicates"
    assert dupes_count_target == 0, "Target file is having duplicates"
    print("test completed.... ")



# marker : used to group the test cases in specific category.
# There are pre-defined markers( skip,xfail) and we can define custom (e.g. smoke,DQ,regresison)

@pytest.mark.DQ
@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.skip
def test_markertest1():
    print("Markers 1 test - step 1 ......")
    print("Markers 1 test - step 2 ......")
    print("Markers 1 test - step 3 ......")
    assert 1 ==2 ," not equal "

@pytest.mark.DQ
@pytest.mark.xfail
@pytest.mark.skip
def test_markertest2():
    print("Markers 2 test - step 1 ......")
    print("Markers 2 test - step 2 ......")
    print("Markers 2 test - step 3 ......")
    assert 1 ==3 ," not equal "
    print("Markers 2 test - step 4 ......")
'''

# This test case does not explcit call the fixture which is marked as autouse=True but when it executes
# it automatically executre the fixture before and after the test case
def test_autouse_testcase():
    assert True,"assertion failed"