## https://ehpub.co.kr/tag/%EB%B9%88-dataframe-%EC%83%9D%EC%84%B1/

import pandas as pd

df1 = pd.DataFrame(index=range(10), columns=range(10))




s = 100
k = 50

df1.loc[100,100] = s - k





print(df1)

df1.to_excel("testdf1.xlsx")