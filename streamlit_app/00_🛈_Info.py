import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Info", page_icon="🪙")

# Generate the current timestamp dynamically
current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

st.markdown(
    """# 🪙 **CryptoPredictor**
### **Predicting Cryptocurrency Prices with ML**

**CryptoPredictor is a machine learning-powered app designed to forecast cryptocurrency prices. Built with Python and Streamlit, it utilises historical data to predict trends for popular cryptocurrencies, empowering users with data-driven insights.**

## 🛠️ **How It's Built**

CryptoPredictor is built with the following core frameworks and tools:

- **Streamlit** - To create an intuitive web interface.
- **Yahoo Finance API (YFinance)** - To fetch up-to-date cryptocurrency data.
- **CoinGecko API** - To dynamically fetch the top 100 cryptocurrencies based on market capitalisation, ensuring real-time selection of popular tokens.
- **LSTM (Long Short-Term Memory)** - A neural network model optimised for time-series predictions.
- **Plotly** - To generate dynamic and interactive financial charts.
- **Pandas** - To manipulate and process cryptocurrency datasets.

## 🧑‍💻 **How It Works**

1. The user selects a cryptocurrency (e.g., BTC, ETH).
2. Historical price data is retrieved using the Yahoo Finance API.
3. The LSTM model is trained on the past 60 days of historical data.
4. Predictions are generated for the next 1–90 days.
5. Results are displayed with interactive charts and tables.

## ✨ **Key Features**

- **Real-time cryptocurrency data** - Access accurate and up-to-date information.
- **Interactive charts** - View historical trends and future predictions visually.
- **Custom prediction ranges** - Forecast prices for 1 to 90 days.
- **Downloadable CSV** - Save prediction results for further analysis.
- **User-friendly interface** - Accessible for novice and experienced users alike.

## 🚀 **Getting Started**

### **Local Installation**

1. Clone the repository:
```bash
git clone https://github.com/user/CryptoPredictor.git
```
**Hint:** Replace `user` with `josericodata` in the URL above. I am deliberately asking you to pause here so you can support my work. If you appreciate it, please consider giving the repository a star or forking it. Your support means a lot—thank you! 😊

2. Create a virtual environment:
```bash
python3 -m venv venvCrypto
```

3. Activate the virtual environment:
```bash
source venvCrypto/bin/activate
```

4. Install requirements:
```bash
pip install -r requirements.txt
```

5. Navigate to the app directory:
```bash
cd streamlit_app
```

6. Run the app:
```bash
streamlit run 00_🛈_Info.py
```

The app will be live at ```http://localhost:8501```



## 🌟 Future Enhancements

Planned improvements and new features include:

- **Integration of advanced ML models** (e.g., Prophet) for better prediction accuracy.
- **Support for additional cryptocurrencies** to expand coverage.
- **Volatility analysis** to measure price swings and potential risks.
- **User accounts and history tracking** for tailored predictions and personalised experiences.


## 🔧 Environment Setup

The CryptoPredictor app is built and tested using the following software environment:

- **Operating System**: Ubuntu 22.04.5 LTS (Jammy)
- **Python Version**: Python 3.10.12

Ensure your environment matches or exceeds these versions for optimal performance.


## 📋 Important Notes

- **CoinGecko API Error 429**: If too many requests are made to the URL, the API may block further requests. Please restart or close the app, and try again after a minute or two. The data should then be available..
- **Using the Crypto Predictor**:
    1. Select a cryptocurrency from the dropdown menu.
    2. Choose the desired prediction range using the slider.
    3. Adjust the **Epochs** slider to set the number of training iterations. Note: Higher epochs result in longer training times but can improve model accuracy.
    4. Click the **Run Prediction** button to generate results.


## ⚠️ Disclaimer

This app is designed to demonstrate my skills in data modeling and analytics, showcasing how data-driven insights can assist in building my portfolio as a data analyst. It is not intended to provide financial advice or investment guidance. The predictions are for illustrative purposes only and should not be relied upon for making financial decisions.
"""
)

# Display the timestamp in a Streamlit app
st.write("### 🔄 Last Updated")
st.write(f"The app was last updated on: **{current_timestamp}**")

