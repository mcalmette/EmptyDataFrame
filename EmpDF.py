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

    #Join two dfs
    df1=df1.join(dfSPY)
    #Drop dates that market not open
    df1 = df1.dropna()
    print(df1)

if __name__ == "__main__":
    test_run()