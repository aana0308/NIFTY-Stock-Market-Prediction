import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model

#Scrapping the data
start='2010-01-01'
end='2020-01-01'
user_input=input("Stock Name:")
df = data.DataReader(user_input,'yahoo',start,end)

#Reseting Index
df=df.reset_index()

#Using Only Close Column
df=df.drop(['Date','Adj Close'],axis=1)
print(df.head())
print(df.describe())

#Getting 100 and 200 days Moving Average
ma100=df.Close.rolling(100).mean()
ma200=df.Close.rolling(200).mean()

#plotting the Same
plt.figure(figsize= (12,6))
plt.title("Close value, Ma100 and Ma200 Vs Time Steps")
plt.plot(df.Close)
plt.plot(ma100,'r')
plt.plot(ma200,'g')

# Splitting the data set into training and testing data
data_training=pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing=pd.DataFrame(df['Close'][int(len(df)*0.70):int(len(df))])

#Scalling the data usind Minmaxscaler
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))
data_training_array= scaler.fit_transform(data_training)
#Loading Model
model=load_model('keras_model.h5')

#Testing the model
past_100_days=data_training.tail(100)
final_df=past_100_days.append(data_testing,ignore_index=True)
input_data=scaler.fit_transform(final_df)
x_test=[]
y_test=[]
for  i in range(100, input_data.shape[0]):
    x_test.append(input_data[i-100: i])
    y_test.append(input_data[i,0])
x_test, y_test=np.array(x_test),np.array(y_test)
print(x_test.shape)
print(y_test.shape)
y_predicted=model.predict(x_test)
scalar=scaler.scale_
scale_factor=1/(scalar[0])
y_predicted=y_predicted*scale_factor
y_test=y_test*scale_factor

#plotting the Prediction
plt.figure(figsize=(12,6))
plt.plot(y_test,'b',label='Original Price')
plt.plot(y_predicted,'g',label='Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()