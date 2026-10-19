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
목표: 가상의 데이터를 바탕으로 분석 계획을 작성한다.
입력: date, kwh, price_per_kwh
완료 조건: 입력 열과 검증 항목이 README에 설명되어 있다.
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

데이터 파일은 임의로 작성한 **가상 데이터**만 사용합니다.

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
