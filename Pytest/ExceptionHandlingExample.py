import pandas as pd

def emp_details_source_file():
    try:
        df = pd.read_csv("Data/emp_details_source.csv1")
        print("Source file content :", df)

    except FileNotFoundError as e:
        print(f"Source file doesn not exist in the location.{e}")

    except Exception as e:
        print(f"Unknow exception encountered {e}")

    finally:
        print("File closed")


def emp_details_target_file():
    df = pd.read_csv("Data/emp_details_target.csv")
    print("Target file content :",df)

emp_details_source_file()
#emp_details_target_file()

