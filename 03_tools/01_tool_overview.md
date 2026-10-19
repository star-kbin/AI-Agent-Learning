# 03-01. ChatGPT · Codex · VS Code · GitHub 역할 이해

[← 목차](./README.md) | [다음 →](./02_chatgpt_workflow.md)

## 1. 같은 일을 하는 도구일까?
|도구|주요 역할|대표 사용 예|
|---|---|---|
|ChatGPT|대화형 문제 정의, 설명, 아이디어, 문서 초안|보고서 목차·요구사항 정리|
|Codex|코드 저장소를 이해하고 코드 변경·테스트를 돕는 코딩 에이전트|함수 수정·테스트 추가·리팩터링|
|VS Code|파일 편집·폴더 탐색·터미널·디버깅 작업공간|프로젝트 열기·코드 실행|
|GitHub|Git 저장소 호스팅·버전 기록·협업|README 게시·변경 이력·PR|

**Git은 버전을 관리하는 도구, GitHub는 Git 저장소를 호스팅하는 서비스**입니다. VS Code 자체가 AI 모델은 아닙니다. Codex는 사용 가능한 제품 형태와 접근 권한에 따라 사용법이 다릅니다.

## 2. 무엇부터 사용해야 할까?
- **설명·기획·글쓰기:** ChatGPT부터 시작
- **파일 편집·읽기:** VS Code 사용
- **여러 파일의 코드 수정·테스트:** Codex 활용(사용 가능한 경우)
- **버전 관리·공유·리뷰:** GitHub 사용
- **코딩 없이 학습:** ChatGPT + GitHub 웹 브라우저만으로도 시작 가능

## 3. 도구 결합의 예
'[빵가게 3일 판매 기록](../examples/bakery_sales/README.md)을 요약하는 과제'를 수행한다고 가정합니다.
1. ChatGPT에 목표·입력 열·검증 조건을 설명하고 실행 계획을 받습니다.
2. VS Code에서 `README.md`와 가상의 CSV 파일을 확인합니다. 수량은 개, 가격·매출은 원이며 판매 합계는 85개, 매출은 170,000원입니다.
3. Codex에 **먼저 변경 계획을 제시하고 승인된 파일만 수정**하도록 요청합니다.
4. 직접 코드 실행 결과와 예상 계산을 대조합니다.
5. GitHub에 코드·README를 올리고 변경 이유를 기록합니다.

## 4. 꼭 구분하기
- AI 답변 생성 ≠ 실제 파일 수정
- 코드 작성 ≠ 코드 실행 성공
- GitHub 업로드 ≠ 코드 품질 보증
- PR 작성 ≠ main 브랜치 반영
- 자동화 허용 ≠ 무제한 접근 권한

## 확인 질문
1. VS Code와 GitHub의 차이는?
2. AI가 "수정했습니다"라고 말하면 무엇으로 확인해야 하나요?
3. 코드를 GitHub에 공개하기 전에 점검할 보안 사항 두 가지는?

<details><summary>답안 보기</summary>

1. VS Code는 로컬 편집 환경, GitHub는 저장소 호스팅·협업 서비스입니다.
2. 실제 파일 diff(변경 내용), 실행·테스트 결과를 확인합니다.
3. 비밀키/토큰과 개인정보·기밀 데이터가 있는지 검사합니다.
</details>

## 공식 참고 자료
- [ChatGPT 도움말](https://help.openai.com/)
- [OpenAI Codex 문서](https://developers.openai.com/codex/)
- [VS Code 문서](https://code.visualstudio.com/docs)
- [GitHub Docs](https://docs.github.com/)

