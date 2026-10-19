# 03-03. VS Code로 작업 폴더와 파일 관리

[← 목차](./README.md) | [다음 →](./04_codex_workflow.md)

## 목표
VS Code에서 폴더·Markdown 파일을 만들고 프로젝트 구조를 이해합니다. **Python 설치는 아직 필요하지 않습니다.**

## 1. 준비
1. 공식 사이트 [Visual Studio Code](https://code.visualstudio.com/)에서 운영체제용 설치 파일을 받습니다.
2. 설치 후 VS Code를 실행하고 **File → Open Folder**로 새 작업 폴더를 엽니다.
3. VS Code 왼쪽 Explorer에서 **New File**을 클릭하고 `README.md`를 만듭니다.
4. 아래 텍스트를 적고 **Ctrl+S**로 저장합니다. Mac에서는 Cmd+S를 사용합니다.

```markdown
# 나의 첫 AI 실습
목표: 가상 빵가게의 판매량과 매출을 정리한다.
입력: 날짜, 준비수량, 주문수량, 판매수량, 개당가격
단위: 수량은 개, 가격과 매출은 원
완료 조건: 판매 합계 85개와 매출 170,000원을 계산식으로 확인한다.
```

## 2. 추천 폴더 구조
```text
my-ai-practice/
├── README.md
├── data/
│   └── sample.csv
├── prompts/
│   └── analysis_prompt.md
└── results/
    └── review.md
```

데이터는 [공통 sample.csv](../examples/bakery_sales/sample.csv)를 내려받아 `data/sample.csv`로 저장하세요. [열 뜻·예상 정답](../examples/bakery_sales/README.md)을 함께 확인합니다. 교육용 가상값이며, CSV는 쉼표로 칸을 구분하는 텍스트 파일입니다. 스프레드시트에서 한글이 깨지면 UTF-8 인코딩으로 가져오세요.

## 3. VS Code에서 할 수 있는 일
- Explorer: 폴더와 파일 보기
- Editor: 코드·Markdown 편집
- Terminal: 명령 실행 (실습 전 명령 의미 확인)
- Source Control: Git 변경 파일 확인 (Git 설정·설치가 필요할 수 있음)
- Extensions: 부가기능 설치 (출처와 권한 확인)

## 4. 오류 예방
- 폴더 전체를 열었는지 확인합니다. 파일 하나만 열면 상대경로가 혼동될 수 있습니다.
- Windows에서 파일 확장자 숨김 설정 때문에 `README.md.txt`가 되지 않았는지 확인합니다.
- 신뢰할 수 없는 폴더에서는 코드 실행과 확장 프로그램 설치에 주의합니다.

## 체크리스트
- [ ] `README.md`를 만들고 저장했다.
- [ ] Markdown 파일 내용을 다시 열어 확인했다.
- [ ] 데이터를 공개해도 되는지 확인했다.

관련 학습: [Python 개발환경 구축](https://github.com/star-kbin/Python-Learning)

