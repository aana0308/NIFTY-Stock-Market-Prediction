# Problem Statement 
Regardless of your investment strategy, fluctuations are expected in the financial market. Despite this variance, professional investors try to estimate their overall returns. Risks and returns differ based on investment types and other factors, which impact stability and volatility. To attempt to predict returns, there are many computer-based algorithms and models for financial market trading. Yet, with new techniques and approaches, data science could improve quantitative researchers' ability to forecast an investment's return.


The aim is to build a model that forecasts an investment's return rate. This will enable investors at any scale to make better decisions.

## Dataset

The dataset used is the NIFTY-50 Stock Market Data (2000 - 2021) (https://www.kaggle.com/rohanrao/nifty50-stock-market-data/download) from Kaggle. The data is the price history and trading volumes of the fifty stocks in the index NIFTY 50 from NSE (National Stock Exchange) India. All datasets are at a day-level with pricing and trading values split across .cvs files for each stock along with a metadata file with some macro-information about the stocks itself. The data spans from 1st January, 2000 to 30th April, 2021.

NSE India: https://www.nseindia.com/

**Target Variables: Open, Close, High, Low**
<br>
<br>
**Open Price :** The Stock at which opens at the start of market
<br>
**High price :** The particular stock which made high during that particular day
<br>
**Low Price :** The Particular stock which made Low during that particular day
<br>
**Close Price :** The stock closing at the end of the Market hours
<br>
<br>
**Mean Open:** 1267.759708 INR
<br>
**Max Open:** 33399.950000 INR
<br>
**Min Open:** 8.500000 INR
<br>
<br>
**Mean Close:** 1266.554351	INR
<br>
**Max Close:** 32861.950000	INR
<br>
**Min Close:** 9.150000 INR
<br>
<br>
**Mean High:** 1286.581440 INR
<br>
**Max High:** 33480.000000 INR
<br>
**Min High:** 9.750000 INR
<br>
<br>
**Mean Low:** 1247.488465 INR
<br>
**Max Low:** 32861.950000 INR
<br>
**Min Low:** 32468.100000 INR

## Model(s) Used

The models used in this task are ARIMA and LSTM.

**ARIMA :** ARIMA is an acronym that stands for AutoRegressive Integrated Moving Average. An ARIMA model is a class of statistical models for analyzing and forecasting time series data. The acronym is descriptive, capturing the key aspects of the model itself. Briefly, they are:

AR: Autoregression. A model that uses the dependent relationship between an observation and some number of lagged observations.
I: Integrated. The use of differencing of raw observations (e.g. subtracting an observation from an observation at the previous time step) in order to make the time series stationary.
MA: Moving Average. A model that uses the dependency between an observation and a residual error from a moving average model applied to lagged observations.
Each of these components are explicitly specified in the model as a parameter. A standard notation is used of ARIMA(p,d,q) where the parameters are substituted with integer values to quickly indicate the specific ARIMA model being used.

The parameters of the ARIMA model are defined as follows:

p: The number of lag observations included in the model, also called the lag order.
d: The number of times that the raw observations are differenced, also called the degree of differencing.
q: The size of the moving average window, also called the order of moving average.

**LSTM :** Long short-term memory (LSTM) is an artificial recurrent neural network (RNN) architecture used in the field of deep learning. Unlike standard feedforward neural networks, LSTM has feedback connections. It can process not only single data points (such as images), but also entire sequences of data (such as speech or video). A common LSTM unit is composed of a cell, an input gate, an output gate and a forget gate. The cell remembers values over arbitrary time intervals and the three gates regulate the flow of information into and out of the cell.

LSTM networks are well-suited to classifying, processing and making predictions based on time series data, since there can be lags of unknown duration between important events in a time series. LSTMs were developed to deal with the vanishing gradient problem that can be encountered when training traditional RNNs.


## Future Work
As a part of future work we need to fix offsets and randomness that appears and even try apply back LSTM to make a past comparision. 

