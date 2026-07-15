# 프로젝트 이름

> 한 줄 소개 — 이 프로젝트가 무엇을 하는지 간단히 적으세요.

<!-- 배지 예시 (레포 경로에 맞게 수정하세요) -->
<!-- ![CI](https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg) -->
<!-- ![License](https://img.shields.io/badge/license-MIT-blue.svg) -->

> **Python 스타터 템플릿입니다.** 다른 언어면 언어 무관 [github-basic-base](https://github.com/hyeongyu-data/github-basic-base)를 쓰세요. `Use this template` 버튼 또는 `gh repo create <이름> --template hyeongyu-data/github-basic-python`.

## 🚀 새 프로젝트 시작 (셋업)

1. **템플릿으로 레포 생성** — 위 `Use this template` 버튼, 또는:
   ```shell
   gh repo create <이름> --template hyeongyu-data/github-basic-python --private --clone
   ```
2. **placeholder 채우기** — `LICENSE`(이름·연도), `README.md`, `CLAUDE.md`(프로젝트 설명), `src/`·`tests/`(예시 코드 교체).
3. **로컬 세팅:**
   ```shell
   pip install pre-commit && pre-commit install   # 커밋 전 자동 검사
   git config commit.template .gitmessage          # 커밋 메시지 양식
   ```
4. **main 브랜치 보호 적용** — 템플릿은 파일만 복제되므로 ruleset은 직접 걸어야 합니다(레포가 public이거나 GitHub Pro 필요). 혼자 쓰면 파일에서 `required_approving_review_count`를 `0`으로:
   ```shell
   gh api repos/<owner>/<repo>/rulesets --method POST --input branch_ruleset_main.json
   ```
5. **릴리스** — 라벨별 자동 분류(`.github/release.yml`):
   ```shell
   gh release create v0.1.0 --generate-notes
   ```

> 1·3·4를 한 방에: `newproj <이름> [python|base] [private|public]` 헬퍼(`~/.newproj.zsh`).

## Prerequisites

- Python 3.11+
- pip (또는 uv / poetry)

## Installation

```shell
python -m venv .venv && source .venv/bin/activate
pip install ruff pytest pre-commit   # 개발 도구 (런타임 의존성은 pyproject.toml에 추가)
pre-commit install                   # 커밋 전 자동 검사 훅 (최초 1회)
```

## Usage

```python
from src.main import add

print(add(10, 5))  # 15
```

## Test

```shell
pytest
```

## Project layout

```
.
├── .github/                 # 이슈·PR 템플릿, CI, dependabot
├── .claude/docs/            # AI 에이전트 참고 문서 (워크플로/리뷰/보안/금지)
├── src/                     # 소스 코드
├── tests/                   # 테스트
├── CLAUDE.md                # AI 코딩 에이전트 진입점
├── AGENTS.md → CLAUDE.md    # symlink
├── .agents → .claude        # symlink
├── branch_ruleset_main.json # main 브랜치 보호 규칙 (GitHub Ruleset import용)
├── CONTRIBUTING.md
├── LICENSE
├── pyproject.toml           # 의존성 + 도구 설정 (ruff 등)
├── .editorconfig .gitattributes .gitignore .gitmessage .python-version
└── .pre-commit-config.yaml
```

## AI 에이전트 (Claude Code 등)

[`CLAUDE.md`](CLAUDE.md)가 진입점이고 상세 참고 문서는 `.claude/docs/`에
있습니다 (워크플로·코드리뷰·계획리뷰·보안·금지사항). `AGENTS.md`는
`CLAUDE.md`의, `.agents`는 `.claude`의 symlink입니다.

## Contributing

[CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요. 브랜치 규칙은 `<type>/<issue#>-설명` 형식입니다 (예: `feat/42-add-login`).

## License

MIT — 자세한 내용은 [LICENSE](LICENSE)를 참조하세요.
