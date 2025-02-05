# NN_lecture(3학년 2학기)
뉴럴네트워크 수업 관련 프로젝트 및 실습

## 실습 : MLP, CNN, RNN(LSTM), AutoEncoder etc.

## 프로젝트 : Koopa (Learning Non-stationary Time Series Dynamics with Koopman Predictors)
- 기획서
- 중간 발표
- 최종 발표
- 최종 결과 보고서

**서론(Introduction)**

Koopa는 효율적인 시계열 예측을 위한 경량 MLP이론 기반 모델로 고도로 훈련된 심층 예측기와 비교하여 77.3%의 훈련 시간과 76.0%의 메모리 설치 공간을 절약하면서도 최첨단 성능을 발휘한다.

유비쿼터스 비정지 시계열을 묘사하는 데 초점을 맞춘 Koopa는 실제 세계 시계열의 비선형 진화를 자연스럽게 다루는 현대의 Koopman 이론에 의해 강화된 모델 용량을 보여주며 종단 간 예측 훈련을 달성하기 위해 재구성 손실 함수가 없는 표준 Koopman Autoencoder와 다르다.

**롤링 예측에 적용 가능(Applicable for Rolling Forecast)**

롤링 예측 중에 들어오는 시계열에 연산자를 적용함으로써 연속적인 분포 이동에 적응함으로써 보다 정확한 성능을 달성 할 수 있으며, 연산자 적응의 순진한 구현은 DMD 알고리즘을 기반으로 한다. 복잡도가 감소된 반복 알고리즘을 제안하며 논문의 부록에서 확인 가능하다.

또한 이 시나리오를 더 잘 이해하기 위해 튜토리얼 노트이 있다. 자세한 내용은 operator_adaptation.ipynb를 참조.(https://github.com/qor6/Koopman/blob/main/operator_adaptation.ipynb)


관련 기사 : https://url.kr/qc6w5t

시각화 tool 예상 : Grafana

# ComputerVision(4학년1학기)
컴퓨터 비전 수업 관련 실습

## 실습 : 이미지 출력(박스&페인트), 에지 검출
https://github.com/qor6/NeuralNetwork-ComputerVision_donga/tree/main/OpenCV
