## Koopa 실행하기

**1. Koopa 논문의 [repository](https://github.com/thuml/Koopa/tree/main)에서 초록색의 `<> Code `에서 `Download Zip`을 선택하여 전체 코드를 다운 받고 압축을 푼다.**
![codeDownload](https://github.com/qor6/NeuralNetwork_donga/assets/87318054/2d13fc65-ba12-43d4-85a5-1b40ef4b19b7)


**2. repository를 아래로 내려 Preparation 섹션에서 Google Drive를 통해 데이터를 다운 받는다.**
![dateDownload](https://github.com/qor6/NeuralNetwork_donga/assets/87318054/b08a43d5-24c2-48b6-9c41-ee0f929b8706)


**3. 다운로드 된 dataset.zip 파일을 1.에서 압축 푼 Koopa-main 폴더 안에 data라는 폴더명으로 압축을 풀어 저장합니다.**
![datesetunzip](https://github.com/qor6/NeuralNetwork_donga/assets/87318054/325a1527-5394-4af5-b9f4-872126b4699c)


**4. 터미널을 열어 아래의 명령어를 실행합니다.**
```console
pip install torch numpy pandas matplotlib scikit-learn
```


*error 가 발생하기도 하는데 본인의 컴퓨터 환경에 맞춰 `torch`, `numpy`, `pandas`, `matplotlib`, `scikit-learn`을 꼭 설치합니다.

저는 다음과 같은 오류가 발생에 chat-gpt에게 물어보고 터미널에 명령어를 작성하여 해결하였습니다.

![error solve](https://github.com/qor6/NeuralNetwork_donga/assets/87318054/d1924130-a5cb-4344-83d8-7aeb1454ba13)

![image](https://github.com/qor6/NeuralNetwork_donga/assets/87318054/4ce7279b-e4db-4ad8-aa70-ad6c500184b1)

![install result](https://github.com/qor6/NeuralNetwork_donga/assets/87318054/322a4ebf-d46c-4b75-a3ac-df641f5f5e8d)

* 꼭 `설치`하셔야 됩니다. 하나라도 설치되지 않으면 다음의 예시와 같이 해당 패키지(`sklearn`)를 설치하라고 합니다.

![install](https://github.com/qor6/NeuralNetwork_donga/assets/87318054/249a709b-f919-4d06-af9a-1bb049be307b)


**5. Koopa를 실행시키기 위해 아래의 명령어를 실행합니다.**
```console
python3 run.py --model_id my_model --model Koopa --data ETTh2 --root_path ./data/dataset/ETT/ --seq_len 96 --is_training 1
```

```console
--model_id my_model (모델을 식별하는 문자열)
--model Koopa (사용할 모델을 지정, 현재 옵션은 Koopa 뿐이다)
--data ETTh2 (데이터셋 지정)
--root_path ./data/dataset/ETT/ (데이터셋의 파일의 path를 위치에 맞추어 바꾸어 줍니다)
--seq_len 96 (입력 시퀀스 길이)
--is_training 1 (모델이 훈련 모드(1)인지 아닌지(0)을 나타내는 정수 플래그)
```
![trainng start](https://github.com/qor6/NeuralNetwork_donga/assets/87318054/320dd921-4176-43ec-abc2-fb9a81f6a2eb)
