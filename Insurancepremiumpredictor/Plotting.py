import pandas
import matplotlib.pyplot as plt
import sklearn

df = pandas.read_csv('insurance.csv')
print(df)
print(df.isnull().sum())

print(plt.style.available)
plt.style.use('seaborn-deep')



figure,ax= plt.subplots()
ax.hist(df['children'], color = 'blue')
plt.xlabel('No. of children')
plt.ylabel('Freq')
plt.title('No. of Children owned by persons distribution')
plt.show()


#a bar chart to check Gender,smoking and bmi
median = df['bmi'].median()
plt.style.use('grayscale')
df['bmi'].fillna(median,inplace=True)
df.groupby(['sex','smoker'])['bmi'].mean().plot(kind='bar',color='maroon')  #
plt.title('Distribution showing Gender,Smoking and BMI')
plt.xlabel('Gender and Smoking')
plt.ylabel('BMI')
plt.show()

figure,ax= plt.subplots()
ax.hist(df['bmi'], color = 'green')
plt.xlabel('BMI')
plt.ylabel('Freq')
plt.title(' BMI Distribution')
plt.show()


figure,ax= plt.subplots()
ax.hist(df['region'],color='orange')
ax.set_xlabel('region')
ax.set_ylabel('smokers')
ax.set_title('Smokers Distribution')
plt.show()

figure,ax= plt.subplots()
ax.hist(df['charges'], color = 'red')
plt.xlabel('Charges Applied')
plt.ylabel('Freq')
plt.title('Charges Distribution')
plt.show()














