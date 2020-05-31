import pandas as pd

def test_run():
    start_date = '2020-01-22'
    end_date = '2020-02-01'
    dates = pd.date_range(start_date,end_date)

    #create an empty df
    df1 = pd.DataFrame(index=dates)

    #Read SPY data into tmp df
    dfSPY = pd.read_csv("SPY.csv", index_col="Date",parse_dates=True
                        ,usecols=['Date', 'Adj Close'],na_values=['nan'])

    #Renme 'Adj Close' column to 'SPY' to prevent crash
    dfSPY = dfSPY.rename(columns={'Adj Close' : 'SPY'})

    #Join two dfs
    df1=df1.join(dfSPY,how='inner')

    #more stocks
    symbols = ['SPY','IBM']

    for symbol in symbols:
        df_temp = pd.read_csv("{}.csv".format(symbol), index_col='Date',
                              parse_dates=True,usecols=['Date','Adj Close'],
                              na_values=['nan'])

        df_temp = df_temp.rename(columns = {'Adj Close' : symbol})
        df=df1.join(df_temp)

if __name__ == "__main__":
    test_run()