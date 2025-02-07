import yfinance as yf
import pandas as pd

# Path to the CSV file with crypto tickers
TICKERS_CSV_PATH = "assets/dataCleaning/cryptoTickers.csv"

def read_crypto_tickers():
    """Read cryptocurrency tickers from a CSV file."""
    try:
        tickers_df = pd.read_csv(TICKERS_CSV_PATH)
        if tickers_df.empty or 'ticker' not in tickers_df.columns or 'name' not in tickers_df.columns:
            raise ValueError("CSV file missing required columns or is empty.")
        return tickers_df.to_dict(orient="records")
    except Exception as e:
        raise RuntimeError(f"Failed to read crypto tickers from CSV. Error: {e}")

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

