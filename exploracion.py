from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('avocado.csv')
#print(data.shape)


#print(data.info)

#print(data.describe())







#print(data['AveragePrice'].mean())





Albany = data[data['region']=='Albany']
Boise = data[data['region']=='Boise']
Boston = data[data['region']=='Boston']


x1=plt.subplot()
g_Albany = Albany.plot(x='year' , y='AveragePrice', kind='scatter', color="red", ax = x1)
g_Boise = Boise.plot(x='year' , y='AveragePrice', kind='scatter', color="blue", ax = x1)
g_Boston = Boston.plot(x='year' , y='AveragePrice', kind='scatter', color="yellow", ax = x1)

plt.show()
























