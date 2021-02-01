import pandas as pd
df = pd.DataFrame({
                    '姓名':['张飞','关羽','刘备','典韦','许诸'],
                    '语文':[68,95,98,90,80],
                    '数学':[65,76,86,88,90],
                    '英语':[30,98,88,77,90]
                    })
df = df.set_index('姓名')
print(df)
print(df.describe())

zhangfei=sum(df.loc['张飞'])
guanyu=sum(df.loc['关羽'])
liubei=sum(df.loc['刘备'])
dianwei=sum(df.loc['典韦'])
xuzhu=sum(df.loc['许诸'])
df['总分']=[zhangfei,guanyu,liubei,dianwei,xuzhu]
df.sort_values(by='总分',inplace=True,ascending=True)
print(df)