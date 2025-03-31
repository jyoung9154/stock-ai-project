# lstm_model.py
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

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
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))  # LSTM 입력 형태로 변환

    return X, y, scaler

# LSTM 모델 구축
def create_lstm_model(X_train):
    model = Sequential()

    # 첫 번째 LSTM 레이어
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
    model.add(Dropout(0.2))  # 과적합 방지를 위한 Dropout 레이어

    # 두 번째 LSTM 레이어
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dropout(0.2))

    # 출력 레이어 (종가 예측)
    model.add(Dense(units=1))

    model.compile(optimizer='adam', loss='mean_squared_error')  # 손실 함수 및 최적화 방법 설정
    return model

if __name__ == "__main__":
    import yfinance as yf
    stock_symbol = "AAPL"
    start_date = "2020-01-01"
    end_date = "2022-12-31"
    
    # 데이터 가져오기
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    X, y, scaler = preprocess_data(stock_data)

    # LSTM 모델 구축
    model = create_lstm_model(X)
    model.summary()  # 모델 구조 확인
