# About dataset

# ETDataset(Electricity Transformer Dataset)
https://github.com/zhouhaoyi/ETDataset

ETT: 부하, 오일 온도를 포함하여 2개 스테이션에 있는 2개의 전기 변압기의 데이터

예시)
![ETT data demo](https://github.com/qor6/NeuralNetwork_donga/assets/87318054/07702354-05c7-4955-967b-47240564e0bc)

**ETT-small**
- ETTh1.csv (1시간 간격)

- ETTh2.csv (1시간 간격 : 2016.07.01 ~ 2018.06.26.19:00)

- ETTm1.csv (15분 간격)

- ETTm1.csv (15분 간격  : 2016.07.01 ~ 2018.06.26.19:45)


|column|설명|
|:---:|:---:|
| date | 기록 날짜 |
| HUFL | 고부하 유용 |
| HULL | 고부하 무용 |
| MUFL | 중간부하 유용 |
| MULL | 중간부하 무용 |
| LUFL | 저부하 유용 |
| LULL | 저부하 무용 |
| OT | 유류 온도 (target) |


energy data 사용 예정 - 전처리 과정에서 고군분투
