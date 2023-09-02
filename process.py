import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class CustomTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        print('\n>>>>>>>init() called.\n')
    def fit(self, X, y = None):
        print('\n>>>>>>>fit() called.\n')
        return self
    def transform(self, X, y = None):
        print('\n>>>>>>>transform() called.\n')
        print("\n>>>> Input : ",X)
        X.drop(columns = 'Route',inplace = True)
        X['Source'] = X['Source'].apply(lambda x: x.lower())
        X['Destination'] = X['Destination'].replace({'New Delhi':'Delhi'})
        X['Destination'] = X['Destination'].apply(lambda x: x.lower())
        X['Date_of_Journey'] = pd.to_datetime(X['Date_of_Journey'],dayfirst = True)
        X['Day_of_Journey'] = X['Date_of_Journey'].dt.weekday
        X['Month'] = X['Date_of_Journey'].dt.month
        X['Month'] = X['Month'].replace({1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'})
        X.drop(columns = 'Date_of_Journey',inplace = True)
        X.loc[X['Dep_Time'] < '12:00','Dep_Time']='AM'
        X.loc[X['Dep_Time'] !='AM','Dep_Time']='PM'
        X['Arrival_Time'] = X['Arrival_Time'].apply(lambda x: x.split()[0])
        X.loc[X['Arrival_Time'] < '12:00','Arrival_Time']='AM'
        X.loc[X['Arrival_Time'] !='AM','Arrival_Time']='PM'
        X['Additional_Info'].replace({'No info':'No Info'},inplace = True)
        print("\n>>>> Output : ", X)
        return X

class CustomTransformer1(BaseEstimator, TransformerMixin):
    def __init__(self):
        print('\n>>>>>>>init() called.\n numerical')
    def fit(self, X, y = None):
        print('\n>>>>>>>fit() called.\n numerical')
        return self
    def transform(self, X, y = None):
        print('\n>>>>>>>transform() called.\n numerical')
        print("\n>>>> Input : ",X)
        X['Duration'] = (pd.to_timedelta(X['Duration']).dt.seconds // 60).astype(int)
        #X.drop(columns = 'Duration',inplace = True)
        #DF = pd.DataFrame(X['Duration'])
        print("\n>>>> Output : ",X)
        return X
