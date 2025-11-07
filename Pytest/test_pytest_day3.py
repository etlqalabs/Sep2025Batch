import pandas as pd
import pytest

@pytest.mark.order(3)
@pytest.mark.smoke
@pytest.mark.regression
def test_test_case_1():
    assert True,"Tets case 1 failed"

@pytest.mark.order(4)
@pytest.mark.smoke
def test_test_case_2():
    assert True,"Tets case 2 failed"

@pytest.mark.order(5)
@pytest.mark.smoke
def test_test_case_3():
    assert True,"Tets case 3 failed"

@pytest.mark.order(11)
@pytest.mark.regression
def test_test_case_4():
    assert True,"Tets case 4 failed"

@pytest.mark.order(12)
@pytest.mark.regression
def test_test_case_5():
    assert True,"Tets case 5 failed"


@pytest.mark.order(6)
def test_data_extraction_test_case_1():
    assert True,"data_extraction_test_case_1 failed"

@pytest.mark.order(7)
def test_data_extraction_test_case_5():
    assert True,"data_extraction_test_case_5 failed"

@pytest.mark.order(8)
def test_data_extraction_test_case_3():
    assert True,"data_extraction_test_case_3 failed"

@pytest.mark.order(9)
def test_data_extraction_test_case_4():
    assert True,"data_extraction_test_case_4failed"

@pytest.mark.order(10)
def test_data_extraction_test_case_2():
    assert True,"data_extraction_test_case_2 failed"

@pytest.mark.order(2)
def test_data_transformation_test_case_4():
    assert True, "test_data_transformation_test_case_4 failed"

@pytest.mark.order(1)
def test_data_transformation_test_case_2():
    assert True, "test_data_transformation_test_case_2 failed"