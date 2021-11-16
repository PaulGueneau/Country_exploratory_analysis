import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
#
# test_df = pd.read_csv('/home/gueneau/PycharmProjects/Analyse_Titanic/test.csv')
# train_df = pd.read_csv('/home/gueneau/PycharmProjects/Analyse_Titanic/train.csv')

df = pd.read_csv('/home/gueneau/PycharmProjects/Analyse_Titanic/countries_indicators.csv')
# dataset = [train_df,test_df]
#
print(df.columns.values)#features
print(df.tail())
