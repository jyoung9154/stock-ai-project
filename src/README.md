# 주식 가격 예측 AI 프로젝트

이 프로젝트는 과거 주식 데이터를 기반으로 LSTM 및 RandomForest 모델을 활용하여 주가를 예측하는 AI 시스템입니다. 또한 뉴스 데이터를 크롤링하고 감성 분석을 수행하여 더 정확한 예측을 지원합니다.

## 기능 개요

- 야후 파이낸스 API를 통한 주식 데이터 수집
- 네이버 금융 뉴스 크롤링
- 뉴스 텍스트 감성 분석
- LSTM 딥러닝 모델을 이용한 주가 예측
- RandomForest 머신러닝 모델을 이용한 주가 예측
- 예측 결과 시각화

## 설치 방법

1. 이 저장소를 클론합니다:
   ```bash
   git clone https://github.com/jyoung9154/stock-ai-project.git
   cd stock-ai-project
   ```

2. 필요한 패키지를 설치합니다:
   ```bash
   pip install -r requirements.txt
   ```

## 필요 패키지

프로젝트를 실행하기 위해 다음 패키지가 필요합니다:
yfinance
numpy
pandas
scikit-learn
tensorflow
matplotlib
requests
beautifulsoup4
transformers


## 사용 방법

### 1. 주식 데이터 수집

특정 주식의 과거 데이터를 수집합니다.

```bash
python src/get_stock_data.py
```

기본적으로 애플(AAPL) 주식 데이터를 수집하도록 설정되어 있으며, 다른 주식을 분석하고 싶다면 코드에서 `stock_symbol` 변수를 변경하세요.

### 2. 뉴스 데이터 수집

네이버 금융에서 인기 주식 관련 뉴스를 수집합니다.

```bash
python src/news_crawling.py
```

이 스크립트는 네이버 금융에서 인기 검색 종목 10개의 뉴스를 수집합니다.

### 3. 감성 분석 실행

뉴스 텍스트에 대한 감성 분석을 수행합니다.

```bash
python src/sentiment_analysis.py
```

이 스크립트는 샘플 텍스트에 대한 감성 분석을 실행합니다. 실제 뉴스 텍스트를 분석하려면 코드에서 `sample_text` 변수를 수정하세요.

### 4. LSTM 모델 확인

LSTM 모델 구조를 확인합니다.

```bash
python src/lstm_model.py
```

이 스크립트는 LSTM 모델의 구조를 출력합니다.

### 5. 주가 예측 모델 학습

RandomForest 모델을 학습시킵니다.

```bash
python src/train_model.py
```

이 스크립트는 주식 데이터를 가져와 RandomForest 모델을 학습시키고 성능을 평가합니다.

### 6. 예측 및 시각화

학습된 모델을 사용하여 주가를 예측하고 결과를 시각화합니다.

```bash
python src/predict_and_visualize.py
```

이 스크립트는 주가 예측 결과를 그래프로 시각화합니다.

## 프로젝트 구조
stock-ai-project/
│
├── src/
│ ├── get_stock_data.py # 주식 데이터 수집
│ ├── news_crawling.py # 뉴스 데이터 크롤링
│ ├── sentiment_analysis.py # 뉴스 감성 분석
│ ├── lstm_model.py # LSTM 모델 정의
│ ├── train_model.py # RandomForest 모델 학습
│ └── predict_and_visualize.py # 예측 및 시각화
│
├── requirements.txt # 필요 패키지 목록
└── README.md # 프로젝트 설명

## 커스터마이징

- 다른 주식을 분석하려면: 각 파일에서 `stock_symbol` 변수를 원하는 주식 티커로 변경하세요.
- 데이터 기간 변경: `start_date`와 `end_date` 변수를 수정하세요.
- 모델 파라미터 조정: `lstm_model.py`에서 LSTM 레이어 수, 유닛 수 등을 조정하거나, `train_model.py`에서 RandomForest 파라미터를 조정할 수 있습니다.

## 주의사항

- 이 프로젝트는 학습 및 실험 목적으로 제작되었으며, 실제 투자 결정에 직접 활용하는 것은 권장되지 않습니다.
- 주식 시장은 다양한 외부 요인에 영향을 받으므로 예측 정확도에 한계가 있습니다.
- API 사용량 제한으로 인해 과도한 데이터 요청은 오류를 발생시킬 수 있습니다.

## 라이센스

이 프로젝트는 MIT 라이센스에 따라 배포됩니다.

## 기여 방법

프로젝트에 기여하고 싶으시다면 이슈를 생성하거나 PR을 보내주세요.

## 마지막 업데이트
2025년 03월 31일