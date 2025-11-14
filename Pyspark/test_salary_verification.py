import time

import pandas as pd
from sqlalchemy import create_engine
import  pytest
from pyspark.sql import SparkSession

@pytest.fixture()
def spark():
    spark = SparkSession.builder.appName("Test cases Execution").getOrCreate()
    yield spark

@pytest.fixture()
def mysql():
    mysql_conn = create_engine("mysql+pymysql://root:Admin%40143@localhost:3308/db_nov9")
    yield mysql_conn

def test_verify_salary_between_file_and_table(spark,mysql):
    df_expected = spark.read.option("multiline","true").option("inferSchema","true").json("Data/salary.json").toPandas()
    df_actual = pd.read_sql("select * from stag_salary",mysql)
    print("Expected dataframe : ",df_expected)
    print("Acyual dataframe : ", df_actual)

    # matching columns orders
    df_expected = df_expected[sorted(df_expected.columns)]
    df_actual= df_actual[sorted(df_actual.columns)]
    time.sleep(10)
    assert df_expected.equals(df_actual)," not matching"





