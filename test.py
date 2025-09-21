import sys
import numpy as np
import pandas as pd 
import matplotlib as mpl
from sklearn.datasets import load_iris

'''
print(sys.version)
print(np.__version__)
print(pd.__version__)
print(mpl.__version__)ß
print(sklearn.__version__)
'''


iris = load_iris(as_frame=True)
#print(iris) #в виде массива выводит 
df = iris.frame #df == dataframe
#print(df)
df.to_csv("iris.csv", index=False) #прописываем индекс, так как по умолчанию в csv файл сохранилась бы шапка таблицы, а нам нужна чистая 

'''
print('***************************')
print(df.head())
print('***************************')
print(df.info())
print('***************************')
print(df.describe())
'''

feature_cols = ['sepal length (cm)','sepal width (cm)','petal length (cm)',]