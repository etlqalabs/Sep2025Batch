# Feature : use of fixture to read the input files for the tests
import pytest
import pandas as pd


@pytest.fixture()
def source_data_setup():
    df_source = pd.read_csv("Data/emp_details_source.csv")
    print("Source dataframe read - This executes Before Test")
    yield df_source
    print("Source dataframe read - This executes After Test")

@pytest.fixture()
def target_data_setup():
    df_target = pd.read_csv("Data/emp_details_target.csv")
    print("Target dataframe read - This executes Before Test")
    yield df_target
    print("Target dataframe read - This executes After Test")

@pytest.fixture()
def target_data_setup():
    df_target = pd.read_csv("Data/emp_details_target.csv")
    print("Target dataframe read - This executes Before Test")
    yield df_target
    print("Target dataframe read - This executes After Test")


@pytest.fixture(autouse=True)
def target_data_setup():
    print("This is autouse - pre test  excuetiuon fixture")
    yield
    print("This is autouse - post test excuetiuon fixture")