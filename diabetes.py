import pandas as pd
import numpy as np
df=pd.read_csv("diabetes.csv")
df.head().T
df.shape
df.isnull().values.any()
df.dtypes
df['outcome']=df['outcome']as type('6001')
df.dtypes['outcome']
df.info()
df.value_counts()
df.mean()
df.median()
df.mode()
df.var()
df.std()
df.skew(axis-=0,skipna=True)
df.kurtosis()