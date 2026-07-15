# Contributing

## 브랜치 규칙

`main`에 직접 커밋하지 않고 브랜치를 만들어 PR로 병합합니다.

```
feat-{ISSUE}/{짧은-설명}    # 예: feat-12/add-login
fix-{ISSUE}/{짧은-설명}     # 예: fix-31/null-check
```

## 작업 흐름

1. 이슈를 만들거나 담당 이슈를 정합니다.
2. 위 규칙으로 브랜치를 만듭니다: `git checkout -b feat-12/add-login`
3. 커밋 전 검사가 통과하는지 확인합니다 (`pre-commit install` 후 자동 실행).
4. 푸시하고 PR을 엽니다. PR 본문에 `Closes #이슈번호`를 넣습니다.
5. 리뷰 승인 + CI 통과 후 병합합니다.

## 커밋 메시지

한 줄 요약(50자 내외) + 필요 시 본문. 관례상 접두어를 권장합니다:
`feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`

## 코드 스타일

`ruff`(린트+포맷)로 통일합니다. 커밋 훅이 자동으로 정리하며, 수동 확인은:

```shell
ruff check . && ruff format --check .
```
