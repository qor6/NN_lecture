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


energy data 사용 예정 - 전처리 과정 중에 있다

|column|설명|
|:---:|:---:|
| 날짜 | 20190101 | 2019년 1월 1일 |
| 시간 | 1000 | 10시 |
| 시/도 | 경기도 | 과천시 |
| 읍_면_동 | BB001동 | 자세한 주소는 공개하기 힘듬 |
| 고객번호 | b72c577b37 |
| 계약종별 | 심야전력(을)II | 계약종별마다 있다 | 
| 계약전력 | 750 | 계약된 전력량 |
| 공급방식 | 삼상4선(22.9kV-y) | 공급 방식을 저의 내림 |
| 고저압구분 | 고압 |
| 유효전력량 | 0.58 | 사용가능한 전력량 | 
| 지상무효전력량 | 0.18 |  |
| 진상무효전력량| 0 |  |
