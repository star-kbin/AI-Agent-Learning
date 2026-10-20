# 실습 예제 모음

일반 사용자도 이해하기 쉬운 **빵가게의 준비 수량·주문 수량·판매 수량**으로 AI 활용을 연습합니다.

## 빵가게 3일 판매 기록

- [용어 풀이·표·손계산·연습 문제](./bakery_sales/README.md)
- [CSV 원본](./bakery_sales/sample.csv)
- [Python 계산 예제](./bakery_sales/calculate.py) (선택, 외부 패키지 불필요)

모두 교육용 가상 데이터입니다. 코딩 없이 표와 계산기로 진행할 수 있습니다. 같은 기록을 [01 기본 개념](../01_agent_concepts/README.md), [02 프롬프트](../02_prompt_engineering/README.md), [03 도구 활용](../03_tools/README.md), [04 문서·데이터](../04_document_data/README.md), [05 협업 코딩](../05_ai_coding/README.md)에서 이어 씁니다.

[첫 화면](../README.md)

## 하루 계산과 코드 검증 (05)

- [하루 계산 함수](./bakery_sales/daily_sales.py): 준비·주문·가격 입력을 파일 읽기와 분리합니다.
- [검증 예제](./bakery_sales/test_daily_sales.py): 정상·경계·오류 입력을 확인합니다.
- [읽기·손계산 경로와 선택 실행 안내](../05_ai_coding/03_testing_debugging.md)

## V2G 4시간 프로젝트 (06)

- [준비 파일·조건·실행 방법](./v2g/README.md)
- [가상 입력](./v2g/sample.csv) · [손계산 정답](./v2g/expected.csv) · [실행 저장 결과](./v2g/result.csv)
- [실행 예제](./v2g/simulate.py) · [검증 예제](./v2g/test_simulate.py)

차량1대·4행의 작은 예제입니다. 기본 경로는 코드 없이 표로 계산하며, 선택 실행에도 외부 Python 패키지는 필요하지 않습니다.
