import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

csv_path = Path(__file__).parent / 'data' / 'studentscores.csv'
dataset = pd.read_csv(csv_path)
X = dataset.iloc[ : , :1].values
Y = dataset.iloc[ : ,1].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, 
                                                    test_size=1/4, 
                                                    random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor = regressor.fit(X_train, Y_train)
