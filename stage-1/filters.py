import pandas as pd

df = pd.read_csv('latest-customers.txt')
# df = pd.DataFrame(data , index=labels)
# print(df.to_string())

res = df[(df['age'] > 40) & (df['age'] < 59)]

res1 = res[['name','phone','email']]

res1.to_csv("res.txt",index = False)

