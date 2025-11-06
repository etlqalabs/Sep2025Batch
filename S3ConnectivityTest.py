
# s3://bucket-read-write-files/employees_data/

# Bucket name : bucket-read-write-files
# Path : employees_data
# file_key : employees_data/emp_details_source.csv
import pandas as pd
import boto3
from io import StringIO

# initiate a session with AWS
s3 = boto3.client("s3")

def read_file_from_s3(bucket_name,file_key):
    # fetch the csv file from s3
    response = s3.get_object(Bucket=bucket_name,Key=file_key)
    csv_content = response['Body'].read().decode('utf-8')

    data = StringIO(csv_content)
    df = pd.read_csv(data)
    print(df)
    return df


def write_file_to_s3(df_name,bucket_name,file_key):
    csv_buffer = StringIO()
    df_name.to_csv(csv_buffer,index=False)
    s3.put_object(Bucket=bucket_name,Key=file_key,Body=csv_buffer.getvalue())


bucket_name = "bucket-read-write-files"
file_key_read = "employees_data/emp_details_source.csv"
file_key_write = "employees_data/emp_details_target.csv"
df = read_file_from_s3(bucket_name,file_key_read)
write_file_to_s3(df,bucket_name,file_key_write)





