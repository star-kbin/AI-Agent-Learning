"""교사용: 로컬 링크·교안 구성·선택 예제 실행을 확인합니다. 외부 패키지 불필요."""

import re
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def main():
    failures = []
    count = 0
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        source = path.read_text(encoding="utf-8")
        if source.count("```") % 2:
            failures.append(f"{path.relative_to(ROOT)}: 닫히지 않은 코드 블록")
        if source.count("<details>") != source.count("</details>"):
            failures.append(f"{path.relative_to(ROOT)}: details 태그 불일치")
        # 코드 블록 속 예시 경로는 실제 링크 검사에서 제외합니다.
        text = re.sub(r"```.*?```", "", source, flags=re.S)
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"(?:[a-z]+:|#)", target):
                continue
            local = unquote(target.split("#", 1)[0]).strip("<>")
            count += 1
            if local and not (path.parent / local).exists():
                failures.append(f"{path.relative_to(ROOT)}: 링크 대상 없음 {local}")
    for folder in ("04_document_data", "05_ai_coding", "06_v2g_project", "07_safety_evaluation"):
        files = list((ROOT / folder).glob("[0-9][0-9]_*.md"))
        if len(files) != 5 or not (ROOT / folder / "README.md").exists():
            failures.append(f"{folder}: README·5개 교안 구성 오류")
        assessment = (ROOT / folder / "05_assessment.md").read_text(encoding="utf-8")
        if len(re.findall(r"^\d\. \*\*\(20점\)\*\*", assessment, re.M)) != 5:
            failures.append(f"{folder}: 20점 문항5개 확인 실패")
    if failures:
        raise SystemExit("\n".join(failures))
    print(f"구성·로컬 링크 {count}개 확인: 통과", flush=True)

    # 저장소 루트와 예제 폴더에서 각각 실행: 작업 위치 독립성을 확인합니다.
    commands = [
        ([sys.executable, str(ROOT / "examples/bakery_sales/calculate.py")], ROOT),
        ([sys.executable, str(ROOT / "examples/bakery_sales/calculate.py")], ROOT / "examples/bakery_sales"),
        ([sys.executable, str(ROOT / "examples/bakery_sales/daily_sales.py")], ROOT),
        ([sys.executable, "-m", "unittest", "discover", "-s", str(ROOT / "examples/bakery_sales"), "-p", "test_daily_sales.py", "-v"], ROOT),
        ([sys.executable, "-m", "unittest", "discover", "-s", str(ROOT / "examples/v2g"), "-p", "test_simulate.py", "-v"], ROOT),
        ([sys.executable, str(ROOT / "examples/v2g/simulate.py")], ROOT),
        ([sys.executable, str(ROOT / "examples/v2g/simulate.py")], ROOT / "examples/v2g"),
    ]
    for command, cwd in commands:
        subprocess.run(command, cwd=cwd, check=True)
    # 배포용 입력·정답·실행 파일만 별도 폴더에 복사해 독립 실행도 확인합니다.
    with tempfile.TemporaryDirectory() as directory:
        folder = Path(directory)
        for name in ("simulate.py", "sample.csv", "expected.csv"):
            (folder / name).write_bytes((ROOT / "examples/v2g" / name).read_bytes())
        subprocess.run([sys.executable, str(folder / "simulate.py")], cwd=folder, check=True)
    print("교안·예제 검증 전체 통과", flush=True)


if __name__ == "__main__":
    main()
