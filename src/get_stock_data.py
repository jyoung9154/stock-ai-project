import yfinance as yf

def get_stock_data(stock_symbol, start_date, end_date):
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    return stock_data

if __name__ == "__main__":
    stock_symbol = "AAPL"  # 예시: Apple 주식
    start_date = "2023-01-01"
    end_date = "2025-12-31"
    data = get_stock_data(stock_symbol, start_date, end_date)
    print(data.head())  # 데이터 확인
