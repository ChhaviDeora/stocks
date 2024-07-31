# # # import streamlit as st
# # # from datetime import date
# # # import yfinance as yf
# # # from prophet import Prophet
# # # from prophet.plot import plot_plotly
# # # from plotly import graph_objs as go

# # # START = "2015-01-01"
# # # TODAY = date.today().strftime("%Y-%m-%d")

# # # st.title('Stock Forecast App')

# # # # Let user input any stock ticker
# # # selected_stock = st.text_input('Enter stock ticker for prediction', 'GOOG')

# # # n_years = st.slider('Years of prediction:', 1, 4)
# # # period = n_years * 365

# # # @st.cache_data
# # # def load_data(ticker):
# # #     data = yf.download(ticker, START, TODAY)
# # #     data.reset_index(inplace=True)
# # #     return data

# # # data_load_state = st.text('Loading data...')
# # # data = load_data(selected_stock)
# # # data_load_state.text('Loading data... done!')

# # # st.subheader('Raw data')
# # # st.write(data.tail())

# # # # Plot raw data
# # # def plot_raw_data():
# # #     fig = go.Figure()
# # #     fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
# # #     fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
# # #     fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
# # #     st.plotly_chart(fig)

# # # plot_raw_data()

# # # # Predict forecast with Prophet
# # # df_train = data[['Date', 'Close']]
# # # df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

# # # m = Prophet()
# # # m.fit(df_train)
# # # future = m.make_future_dataframe(periods=period)
# # # forecast = m.predict(future)

# # # # Show and plot forecast
# # # st.subheader('Forecast data')
# # # st.write(forecast.tail())

# # # st.write(f'Forecast plot for {n_years} years')
# # # fig1 = plot_plotly(m, forecast)
# # # st.plotly_chart(fig1)


# # # # import streamlit as st
# # # # from datetime import date

# # # # import yfinance as yf
# # # # from prophet import Prophet
# # # # from prophet.plot import plot_plotly
# # # # from plotly import graph_objs as go

# # # # START = "2015-01-01"
# # # # TODAY = date.today().strftime("%Y-%m-%d")

# # # # st.title('Stock Forecast App')

# # # # stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
# # # # selected_stock = st.selectbox('Select dataset for prediction', stocks)

# # # # n_years = st.slider('Years of prediction:', 1, 4)
# # # # period = n_years * 365

# # # # @st.cache
# # # # def load_data(ticker):
# # # #     data = yf.download(ticker, START, TODAY)
# # # #     data.reset_index(inplace=True)
# # # #     return data

	
# # # # data_load_state = st.text('Loading data...')
# # # # data = load_data(selected_stock)
# # # # data_load_state.text('Loading data... done!')

# # # # st.subheader('Raw data')
# # # # st.write(data.tail())

# # # # # Plot raw data
# # # # def plot_raw_data():
# # # # 	fig = go.Figure()
# # # # 	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
# # # # 	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
# # # # 	fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
# # # # 	st.plotly_chart(fig)
	
# # # # plot_raw_data()

# # # # # Predict forecast with Prophet.
# # # # df_train = data[['Date','Close']]
# # # # df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

# # # # m = Prophet()
# # # # m.fit(df_train)
# # # # future = m.make_future_dataframe(periods=period)
# # # # forecast = m.predict(future)

# # # # # Show and plot forecast
# # # # st.subheader('Forecast data')
# # # # st.write(forecast.tail())
    
# # # # st.write(f'Forecast plot for {n_years} years')
# # # # fig1 = plot_plotly(m, forecast)
# # # # st.plotly_chart(fig1)
# # import streamlit as st
# # import finnhub
# # from datetime import date
# # import yfinance as yf
# # from prophet import Prophet
# # from prophet.plot import plot_plotly
# # from plotly import graph_objs as go

# # # API key for Finnhub
# # api_key = 'cqklv09r01qr0sv08qn0cqklv09r01qr0sv08qng'

# # # Initialize Finnhub client
# # finnhub_client = finnhub.Client(api_key=api_key)

# # START = "2015-01-01"
# # TODAY = date.today().strftime("%Y-%m-%d")

# # st.title('Stock Forecast App')

# # # Fetch stock symbols and names from Finnhub
# # @st.cache_data
# # def fetch_stock_list():
# #     symbols = finnhub_client.stock_symbols('US')
# #     return [(symbol['symbol'], symbol['description']) for symbol in symbols]

# # stock_list = fetch_stock_list()
# # stock_dict = {symbol: description for symbol, description in stock_list}

# # # Convert stock_dict keys to a list for selectbox
# # stock_keys = list(stock_dict.keys())

# # # Let user search and select any stock ticker from the list
# # selected_stock = st.selectbox('Select dataset for prediction', stock_keys, format_func=lambda x: f"{x} - {stock_dict[x]}")

# # n_years = st.slider('Years of prediction:', 1, 4)
# # period = n_years * 365

# # @st.cache_data
# # def load_data(ticker):
# #     data = yf.download(ticker, START, TODAY)
# #     data.reset_index(inplace=True)
# #     return data

# # data_load_state = st.text('Loading data...')
# # data = load_data(selected_stock)
# # data_load_state.text('Loading data... done!')

# # st.subheader('Raw data')
# # st.write(data.tail())

# # # Plot raw data
# # def plot_raw_data():
# #     fig = go.Figure()
# #     fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
# #     fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
# #     fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
# #     st.plotly_chart(fig)

# # plot_raw_data()

# # # Predict forecast with Prophet
# # df_train = data[['Date', 'Close']]
# # df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

# # m = Prophet()
# # m.fit(df_train)
# # future = m.make_future_dataframe(periods=period)
# # forecast = m.predict(future)

# # # Show and plot forecast
# # st.subheader('Forecast data')
# # st.write(forecast.tail())

# # st.write(f'Forecast plot for {n_years} years')
# # fig1 = plot_plotly(m, forecast)
# # st.plotly_chart(fig1)
# # import streamlit as st
# # import finnhub
# # from datetime import date
# # import yfinance as yf
# # from prophet import Prophet
# # from prophet.plot import plot_plotly
# # from plotly import graph_objs as go

# # # API key for Finnhub
# # api_key = 'cqklv09r01qr0sv08qn0cqklv09r01qr0sv08qng'

# # # Initialize Finnhub client
# # finnhub_client = finnhub.Client(api_key=api_key)

# # START = "2015-01-01"
# # TODAY = date.today().strftime("%Y-%m-%d")

# # st.title('Stock Forecast App')

# # # Fetch stock symbols and names from Finnhub
# # @st.cache_data
# # def fetch_stock_list():
# #     symbols = finnhub_client.stock_symbols('US')
# #     return [(symbol['symbol'], symbol['description']) for symbol in symbols]

# # stock_list = fetch_stock_list()
# # stock_dict = {symbol: description for symbol, description in stock_list}

# # # Convert stock_dict keys to a list for selectbox
# # stock_keys = list(stock_dict.keys())

# # # Let user search and select any stock ticker from the list
# # selected_stock = st.selectbox('Select dataset for prediction', stock_keys, format_func=lambda x: f"{x} - {stock_dict[x]}")

# # n_years = st.slider('Years of prediction:', 1, 4)
# # period = n_years * 365

# # @st.cache_data
# # def load_data(ticker):
# #     data = yf.download(ticker, START, TODAY)
# #     data.reset_index(inplace=True)
# #     return data

# # data_load_state = st.text('Loading data...')
# # data = load_data(selected_stock)
# # data_load_state.text('Loading data... done!')

# # st.subheader('Raw data')
# # st.write(data.tail())

# # # Plot raw data
# # def plot_raw_data():
# #     fig = go.Figure()
# #     fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
# #     fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
# #     fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
# #     st.plotly_chart(fig)

# # plot_raw_data()

# # # Predict forecast with Prophet
# # df_train = data[['Date', 'Close']]
# # df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

# # m = Prophet()
# # m.fit(df_train)
# # future = m.make_future_dataframe(periods=period)
# # forecast = m.predict(future)

# # # Show and plot forecast
# # st.subheader('Forecast data')
# # st.write(forecast.tail())

# # st.write(f'Forecast plot for {n_years} years')
# # fig1 = plot_plotly(m, forecast)
# # st.plotly_chart(fig1)
# import streamlit as st
# import finnhub
# from datetime import date
# import yfinance as yf
# from prophet import Prophet
# from prophet.plot import plot_plotly
# from plotly import graph_objs as go

# # API key for Finnhub
# api_key = 'cqklv09r01qr0sv08qn0cqklv09r01qr0sv08qng'  # Replace with your actual API key

# # # Initialize Finnhub client
# # finnhub_client = finnhub.Client(api_key=api_key)

# # START = "2015-01-01"
# # TODAY = date.today().strftime("%Y-%m-%d")

# # st.title('Stock Forecast App')

# # # Fetch stock symbols and names from Finnhub
# # @st.cache_data
# # def fetch_stock_list():
# #     symbols = finnhub_client.stock_symbols('US')
# #     return [(symbol['symbol'], symbol['description']) for symbol in symbols]

# # stock_list = fetch_stock_list()
# # stock_dict = {symbol: description for symbol, description in stock_list}

# # # Convert stock_dict keys to a list for selectbox
# # stock_keys = list(stock_dict.keys())

# # # Let user search and select any stock ticker from the list
# # selected_stock = st.selectbox('Select dataset for prediction', stock_keys, format_func=lambda x: f"{x} - {stock_dict[x]}")

# # n_years = st.slider('Years of prediction:', 1, 4)
# # period = n_years * 365

# # @st.cache_data
# # def load_data(ticker):
# #     data = yf.download(ticker, START, TODAY)
# #     data.reset_index(inplace=True)
# #     return data

# # data_load_state = st.text('Loading data...')
# # data = load_data(selected_stock)
# # data_load_state.text('Loading data... done!')

# # st.subheader('Raw data')
# # st.write(data.tail())

# # # Plot raw data
# # def plot_raw_data():
# #     fig = go.Figure()
# #     fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
# #     fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
# #     fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
# #     st.plotly_chart(fig)

# # plot_raw_data()

# # # Predict forecast with Prophet
# # df_train = data[['Date', 'Close']]
# # df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

# # m = Prophet()
# # m.fit(df_train)
# # future = m.make_future_dataframe(periods=period)
# # forecast = m.predict(future)

# # # Show and plot forecast
# # st.subheader('Forecast data')
# # st.write(forecast.tail())

# # st.write(f'Forecast plot for {n_years} years')
# # fig1 = plot_plotly(m, forecast)
# # st.plotly_chart(fig1)

# import streamlit as st
# from datetime import date

# import yfinance as yf
# from prophet import Prophet
# from prophet.plot import plot_plotly
# from plotly import graph_objs as go

# START = "2015-01-01"
# TODAY = date.today().strftime("%Y-%m-%d")

# st.title('Stock Forecast App')

# stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
# selected_stock = st.selectbox('Select dataset for prediction', stocks)

# n_years = st.slider('Years of prediction:', 1, 4)
# period = n_years * 365


# @st.cache
# def load_data(ticker):
#     data = yf.download(ticker, START, TODAY)
#     data.reset_index(inplace=True)
#     return data

	
# data_load_state = st.text('Loading data...')
# data = load_data(selected_stock)
# data_load_state.text('Loading data... done!')

# st.subheader('Raw data')
# st.write(data.tail())

# # Plot raw data
# def plot_raw_data():
# 	fig = go.Figure()
# 	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
# 	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
# 	fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
# 	st.plotly_chart(fig)
	
# plot_raw_data()

# # Predict forecast with Prophet.
# df_train = data[['Date','Close']]
# df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

# m = Prophet()
# m.fit(df_train)
# future = m.make_future_dataframe(periods=period)
# forecast = m.predict(future)

# # Show and plot forecast
# st.subheader('Forecast data')
# st.write(forecast.tail())
    
# st.write(f'Forecast plot for {n_years} years')
# fig1 = plot_plotly(m, forecast)
# st.plotly_chart(fig1)

# st.write("Forecast components")
# fig2 = m.plot_components(forecast)
# st.write(fig2)
import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

# Constants
START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

# Streamlit app title
st.title('Stock Forecast App')

# Dropdown menu for stock selection
stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
selected_stock = st.selectbox('Select dataset for prediction', stocks)

# Slider for number of years of prediction
n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365

@st.cache_data
def load_data(ticker):
    """Fetches stock data from Yahoo Finance."""
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')

# Display raw data
st.subheader('Raw data')
st.write(data.tail())

def plot_raw_data():
    """Plots raw stock data."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="Stock Open"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="Stock Close"))
    fig.layout.update(title_text='Time Series Data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

# Prepare data for forecasting
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

# Forecasting with Prophet
m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Display forecast data
st.subheader('Forecast data')
st.write(forecast.tail())

# Plot forecast
st.write(f'Forecast plot for {n_years} years')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

# Show forecast components
st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)

