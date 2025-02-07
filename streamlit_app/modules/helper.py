import pandas as pd
import yfinance as yf
import streamlit as st

# Read cryptocurrency tickers from a CSV file.
@st.cache_data
def read_crypto_tickers():
    try:
        df = pd.read_csv("assets/dataCleaning/cryptoTickers.csv")
        
        # Ensure required columns are present
        required_columns = {"ticker", "name"}
        if not required_columns.issubset(df.columns):
            raise ValueError(f"Missing required columns: {required_columns - set(df.columns)}")
        
        # Return as a list of dictionaries for easier Streamlit handling
        return df.to_dict(orient="records")
    except FileNotFoundError:
        st.error("CSV file not found. Please check the file path.")
        return []
    except Exception as e:
        st.error(f"Error reading CSV: {e}")
        return []


# Fetch historical data from Yahoo Finance."""
def download_data(ticker):
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

# Format the DataFrame for Streamlit display."""
def format_table(df):
    df = df.loc[:, ~df.columns.duplicated()]  # Remove duplicate columns
    df.reset_index(inplace=False)
    df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
    return df.rename(columns={0: "Predicted Closing Price"})

