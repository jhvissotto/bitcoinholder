import yfinance as yf
import pandas as pd

tickers = {
    "BTC-USD": "btc_usd_mensal.csv",
    "^GSPC": "sp500_mensal.csv",
    "^RUT": "russell2000_mensal.csv",
    "^DJI": "dowjones_mensal.csv",
}

for ticker, filename in tickers.items():
    print(f"Baixando {ticker}...")
    data = yf.download(ticker, period="max", interval="1mo", auto_adjust=True, progress=False)

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data = data.reset_index()
    data.to_csv(filename, index=False)
    print(f"  Salvo: {filename} ({len(data)} linhas)")

print("\nConcluído!")
