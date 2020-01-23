import pandas
import sklearn
import matplotlib

df=pandas.read_csv('insurance.csv')
print(df)

print(df.describe())
print(df.corr())
print(df.dtypes)

print (df.isnull().sum())    #checking empties


#no empties so we replace texts

df['sex'].replace({'male':0,'female':1},inplace=True)

df['smoker'].fillna('N',inplace=True)
df['smoker'].replace({'yes':0,'no':1},inplace=True)

df['region'].fillna('N',inplace=True)
df['region'].replace({'southeast':0,'southwest':1,'northeast':2,'northwest':3,'N':4},inplace=True)


array=df.values  # reading all data into an array
features=array[:,0:6] # (:) means all rows ...7 is not counted here
labels=array[:,6]  #7th column which is the sales status is counted here


#splitting70% of data for training
#and 30% of data for testing
from sklearn import model_selection
X_train,X_test,Y_train,Y_test=model_selection.train_test_split(features,labels,test_size=0.3,random_state=42)

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train,Y_train)   #training the algorithm
print('Training...Finished')


predictions= model.predict(X_test)
print(predictions)# model will predict charges- from X_tests,,, we hide the y tests which has the answers(sales)
print("======")
print(Y_test)
# compare this predictions and the y-test(sales)
from sklearn.metrics import r2_score
# r squared,mean square error
print('R Squared=',r2_score(Y_test,predictions))

from sklearn.metrics import mean_squared_error
print('Mean Squared Error',mean_squared_error(Y_test,predictions))
# we need to find the square root

# plotting .... we visualize  the model performance in a scatter plot
import matplotlib.pyplot as plt
plt.style.use('seaborn')
figure, ax = plt.subplots()
ax.scatter(Y_test,predictions,color='green')
ax.plot(Y_test,Y_test,color='red') #line
ax.set_xlabel('Y test')
ax.set_ylabel('Model predictions')
ax.set_title('Y test vs Y test')
plt.show()

#new insurance member
#28,male,33,3,no,southeast
member =[[28,0,33,3,1,1]]
observation = model.predict(member)
print('your insurance premium charges are', observation,'Kshs')








