import numpy as np 
import matplotlib.pyplot as plt 
from sklearn import svm, preprocessing
import pandas as pd 
from matplotlib import style
style.use("ggplot")
import time

df = pd.read_csv('save.csv')

X = df[['DE Ratio',
             'Trailing P/E',
             'Price/Sales',
             'Price/Book',
             'Profit Margin',
             'Operating Margin',
             'Return on Assets',
             'Return on Equity',
             'Revenue Per Share',
             'Market Cap',
             'Enterprise Value',
             'Forward P/E',
             'PEG Ratio',
             'Enterprise Value/Revenue',
             'Enterprise Value/EBITDA',
             'Revenue',
             'Gross Profit',
             'EBITDA',
             'Net Income Avl to Common ',
             'Diluted EPS',
             'Earnings Growth',
             'Revenue Growth',
             'Total Cash',
             'Total Cash Per Share',
             'Total Debt',
             'Current Ratio',
             'Book Value Per Share',
             'Cash Flow',
             'Beta',
             'Held by Insiders',
             'Held by Institutions',
             'Shares Short (as of',
             'Short Ratio',
             'Short % of Float',
             'Shares Short (prior ']]
y = df["Status"].values.reshape(-1,1)

print(X.shape, y.shape)

def Analysis():

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    from sklearn.preprocessing import StandardScaler
    X_scaler = StandardScaler().fit(X_train)
    y_scaler = StandardScaler().fit(y_train)
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)
    y_train_scaled = y_scaler.transform(y_train)
    y_test_scaled = y_scaler.transform(y_test)
    from sklearn.svm import SVC
    model = SVC(kernel="linear")
    model.fit(X_train_scaled, y_train_scaled.astype(int))
   
    # from sklearn.metrics import mean_squared_error

    predictions = model.predict(X_test_scaled)
    # MSE = mean_squared_error(y_test_scaled, predictions)


    # print(f"MSE: {MSE}")
    from sklearn.metrics import classification_report
    print(classification_report(y_test_scaled.astype(int), predictions))


Analysis()

