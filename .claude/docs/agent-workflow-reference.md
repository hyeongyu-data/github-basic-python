# 워크플로 레퍼런스

`CLAUDE.md`의 핵심 규칙을 실제 작업 순서로 풀어 쓴 문서입니다.

## 작업 흐름

```
이슈 → 브랜치 → 작업 → Draft PR → 셀프 리뷰 → Ready → 리뷰 → Squash merge
```

1. **이슈**: 코드 변경 전 이슈를 발행합니다(`.github/ISSUE_TEMPLATE`).
2. **브랜치**: 이슈의 `Create a branch`로 생성. 이름은 `<type>/<issue#>-설명`
   (소문자·하이픈). 예: `feat/42-add-login`.
3. **커밋**: `<type>: <설명>` (한국어, 50자 내외).
   type = `feat`, `fix`, `refactor`, `docs`, `test`, `chore`.
4. **PR**: 본문에 `Closes #<issue>`. 먼저 Draft로 열고 diff를 셀프 리뷰한 뒤
   Ready 전환.
5. **머지**: CI(`lint-test`) 통과 + 리뷰 승인 + 모든 대화 resolved 후
   **squash merge**. `main` 직접 push 금지(`branch_ruleset_main.json` 참조).

## 검증

```bash
ruff check . && ruff format --check .
pytest
```

## 하지 않을 것

- `main`에 직접 push
- secret / `.env` / 키 커밋
- 요청 범위를 벗어난 리팩터링을 같은 PR에 섞기
