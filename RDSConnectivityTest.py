import pandas as pd
from sqlalchemy import create_engine


mysql_engine = create_engine("mysql+pymysql://admin:password@sepmysqldb.cnkoc8gg2fb4.ap-south-1.rds.amazonaws.com:3306/employees")

df = pd.read_sql("""select * from emp""",mysql_engine)
print(df)

df.to_sql("emp_bkp",mysql_engine)
