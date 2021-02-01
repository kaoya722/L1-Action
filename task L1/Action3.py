import pandas as pd
import numpy as np

data = pd.read_csv('D:/资料/培训/2021/黑马大赛/task L1/car_complain.csv')
df = pd.DataFrame(data)
df_index = df.problem.str.split(',', expand=True).stack().to_frame()
df_index = df_index.reset_index(level=1,drop=True).rename(columns={0:'ProblemID'})
df1 = df[['brand']].join(df_index)
df2 = df[['car_model']].join(df_index)

#result1 = df.groupby('brand').agg([np.count_nonzero, np.mean])
result1 = df1.groupby('brand').count()
result1 = result1.sort_values('ProblemID',ascending=False)
print(result1)

#result2 = df.groupby('car_model').agg([np.count_nonzero, np.mean])
result2 = df2.groupby('car_model').count()
result2 = result2.sort_values('ProblemID',ascending=False)
print(result2)

x1 = df[['brand']].join(df_index).groupby('brand').count().rename(columns={'ProblemID':'x'})
x2 = pd.DataFrame(df.groupby("brand")['car_model'].nunique())
x2 = x2.rename(columns={'car_model':'x'})
result3=x1.div(x2)
result3 = result3.sort_values('x',ascending=False)

print(result3)
