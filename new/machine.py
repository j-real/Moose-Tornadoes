import numpy as np 
import matplotlib.pyplot as plt 
from sklearn import svm, preprocessing
import pandas as pd 
from matplotlib import style 
style.use ("ggplot")

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



# def Build_Data_Set ():
#     data_df = pd.DataFrame.from_csv("save.csv")
    
#     X = np.array(data_df[FEATURES].values.tolist())
#     y = data_df["Status"].replace("underperform",0).replace("outperform",1).values.reshape(-1,1)

#     # X = preprocessing.scale(X)

#     return X,y

def Analysis():

    # test_size = 500

    # X,y = Build_Data_Set()
    # print(len(X))
    # clf = svm.SVC(kernel="linear", C=1.0)
    # clf.fit(X[:-test_size],y[:-test_size])
    # correct_count = 0

    # for x in range (1, test_size+1):
    #     if clf.predict(X[-x])[0] == y[-x]:
    #         correct_count += 1
    # print("Accuracy:", (correct_count/test_size)*100.00)
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
    model.fit(X_train_scaled, y_train_scaled.ravel())
    # plt.scatter(model.predict(X_train_scaled), model.predict(X_train_scaled) - y_train_scaled, c="blue", label="Training Data")
    # plt.scatter(model.predict(X_test_scaled), model.predict(X_test_scaled) - y_test_scaled, c="orange", label="Testing Data")
    # plt.legend()
    # plt.hlines(y=0, xmin=y_test_scaled.min(), xmax=y_test_scaled.max())
    # plt.title("Residual Plot")
    # plt.show()
    print("Accuracy:" % model.score(X_test_scaled, y_test_scaled.astype(int)))
    from sklearn.metrics import mean_squared_error

    predictions = model.predict(X_test_scaled)
    MSE = mean_squared_error(y_test_scaled, predictions)
    # r2 = model.score(X_test_scaled, y_test_scaled)

    print(f"MSE: {MSE}")




    # w = clf.coef_[0]
    # a = -w[0]/w[1]
    # xx=np.linspace(min(X[:,0]), max(X[:,0]))
    # yy = a*xx - clf.intercept_[0]/w[1]

    # h0 = plt.plot(xx,yy, "k-", label="non weighted")
    # plt.scatter(X[:,0], X[:,1], c=y)
    # plt.show()

Analysis()


