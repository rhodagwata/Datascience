import pandas
import sklearn

import matplotlib

df=pandas.read_csv('real_estate_data.csv')
print(df)

print(df.describe())
print(df.corr())
print(df.dtypes)

print (df.isnull().sum())    #checking empties

print(df.groupby('exterior_walls').size())


from sklearn import preprocessing
le = preprocessing.LabelEncoder()
df['exterior_walls'].fillna('N',inplace=True)
df['exterior_walls'] = le.fit_transform(df['exterior_walls'])




df['roof'].fillna('N',inplace=True)
df['roof'] = le.fit_transform(df['roof'])

df['basement'].fillna(2,inplace=True)
#df['basement'].replace({'Wood Siding':0,'Brick':1,'Concrete Block':2},inplace=True)

df['property_type'] = le.fit_transform(df['property_type'])





array=df.values  # reading all data into an array
features=array[:,1:26]

labels=array[:,0]



#splitting70% of data for training
#and 30% of data for testing
from sklearn import model_selection
X_train,X_test,Y_train,Y_test=model_selection.train_test_split(features,labels,test_size=0.3,random_state=42)

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
model=KNeighborsRegressor()
model.fit(X_train,Y_train)   #training the algorithm
print('Training...Finished')


predictions= model.predict(X_test)
print(predictions)# model will predict charges- from X_tests,,, we hide the y tests which has the answers(sales)
print("======")
print(Y_test)


#comparing predictions and the y-test
#you import r squared and mean squared error

from sklearn.metrics import r2_score
print('R Squared=',r2_score(Y_test,predictions))

from sklearn.metrics import mean_squared_error
print('Mean Squared Error',mean_squared_error(Y_test,predictions))

import matplotlib.pyplot as plt
plt.style.use('seaborn')
figure, ax = plt.subplots()
ax.scatter(Y_test,predictions,color='green')
ax.plot(Y_test,Y_test,color='red') #line
ax.set_xlabel('Y test')
ax.set_ylabel('Model predictions')
ax.set_title('Y test vs Y test')
plt.show()


from sklearn.feature_selection import SelectKBest, chi2
test = SelectKBest(score_func=chi2, k=10)
fit = test.fit(features, labels)
print(fit.scores_)



house =[[1,1,642,1944,0,0,1,0,159,13,36,17,92,12,66,50,28.0,36.0,88.0,176.0,61.0,7.0,3.0,2011]]
observation = model.predict(house)
print('The price of your house is',observation,'Kshs')


