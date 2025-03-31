import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import yfinance as yf
from sklearn.model_selection import train_test_split

# 주식 데이터 전처리
def preprocess_data(stock_data):
    data = stock_data[['Close']].values  # 종가 데이터만 사용
    scaler = MinMaxScaler(feature_range=(0, 1))  # 데이터 스케일링 (0~1 사이로 정규화)
    data_scaled = scaler.fit_transform(data)  # 데이터 스케일링

    # 학습에 사용할 시퀀스를 준비합니다.
    X, y = [], []
    for i in range(60, len(data_scaled)):  # 60일의 데이터로 예측
        X.append(data_scaled[i-60:i, 0])  # 60일 데이터
        y.append(data_scaled[i, 0])  # 예측할 값 (현재일의 종가)
    
    X, y = np.array(X), np.array(y)
    return X, y, scaler

if __name__ == "__main__":
    # 데이터 가져오기
    stock_symbol = "AAPL"
    start_date = "2023-01-01"
    end_date = "2025-12-31"
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

    # 데이터 전처리
    X, y, scaler = preprocess_data(stock_data)

    # 데이터 분할 (학습용, 테스트용 데이터)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # 모델 학습 (Random Forest Regressor 사용)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train.reshape(X_train.shape[0], -1), y_train)  # X_train을 2D 배열로 변환

    # 예측
    y_pred = model.predict(X_test.reshape(X_test.shape[0], -1))  # X_test을 2D 배열로 변환

    # 성능 평가
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")

    # 예측 결과 역변환 (스케일링 복원)
    y_pred_rescaled = scaler.inverse_transform(y_pred.reshape(-1, 1))
    y_test_rescaled = scaler.inverse_transform(y_test.reshape(-1, 1))

    print("Predicted stock price:", y_pred_rescaled[:5])  # 예측된 주식 가격 (상위 5개)
    print("Actual stock price:", y_test_rescaled[:5])  # 실제 주식 가격 (상위 5개)
