import requests
import yfinance as yf
import pandas as pd

def fetch_crypto_tickers(limit=100):
    """Fetch cryptocurrency tickers with names from CoinGecko."""
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": limit,
            "page": 1
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return [{"ticker": f"{coin['symbol'].upper()}-USD", "name": coin['name']} for coin in data]
    except Exception as e:
        raise RuntimeError(f"Failed to fetch cryptocurrency tickers. Please check your internet connection or try again later. Error: {e}")

def download_data(ticker):
    """Fetch historical data from Yahoo Finance."""
    data = yf.download(ticker, period="max", interval="1d")
    if data.empty:
        raise ValueError(f"No valid data for ticker {ticker}.")
    
    # Handle MultiIndex columns
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = ['_'.join(col).strip() for col in data.columns.values]

    if 'Close' not in data.columns and f'Close_{ticker}' not in data.columns:
        raise ValueError(f"'Close' column not found for ticker {ticker}.")
    
    # Drop rows where Close prices are missing
    close_column = 'Close' if 'Close' in data.columns else f'Close_{ticker}'
    return data.dropna(subset=[close_column]), close_column

def format_table(df):
    """Format the DataFrame for Streamlit display."""
    df = df.loc[:, ~df.columns.duplicated()]  # Remove duplicate columns
    df.reset_index(inplace=False)
    df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
    return df.rename(columns={0: "Predicted Closing Price"})


