
import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return  os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """Read Stock data (adjusted close) for given symb"""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols: # add SPY for ref if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                              parse_dates=True, usecols=['Date','Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close' : symbol})
        df = df.join(df_temp)
        if symbol == 'SPY': #drop dates SPY didnt trade
            df = df.dropna(subset=[["SPY"]])

    return df

def plot_data(df, title= "Stock prices"):
    a = df.plot(title=title,fontsize=16)
    a.set_xlabel("Date")
    a.set_ylabel("Price")
    plt.show()

def run():
    start_date = '2019-06-22'
    end_date = '2020-03-24'
    dates = pd.date_range(start_date, end_date)

    #create an empty df
    df1 = pd.DataFrame(index=dates)

    #Read SPY data into tmp df
    dfSPY = pd.read_csv("SPY.csv", index_col="Date", parse_dates=True
                        , usecols=['Date', 'Adj Close'],
                        na_values=['nan'])

    #Renme 'Adj Close' column to 'SPY' to prevent crash
    dfSPY = dfSPY.rename(columns={'Adj Close': 'SPY'})

    #Join two dfs
    df1=df1.join(dfSPY, how='inner')

    #more stocks
    #comparing to spy
    symbols = ['MSFT']

    for symbol in symbols:
        df_temp = pd.read_csv("{}.csv".format(symbol), index_col='Date',
                              parse_dates=True, usecols=['Date','Adj Close']
                                                        ,na_values=['nan'])

        df_temp = df_temp.rename(columns={'Adj Close' : symbol})
        df1 = df1.join(df_temp)

    plot_data(df1)


if __name__ == "__main__":
    run()
