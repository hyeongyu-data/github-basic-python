# 프로젝트 이름

> 한 줄 소개 — 이 프로젝트가 무엇을 하는지 간단히 적으세요.

<!-- 배지 예시 (레포 경로에 맞게 수정하세요) -->
<!-- ![CI](https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg) -->
<!-- ![License](https://img.shields.io/badge/license-MIT-blue.svg) -->

## Prerequisites

- Python 3.11+
- pip (또는 uv / poetry)

## Installation

```shell
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pre-commit install   # 커밋 전 자동 검사 훅 설치 (최초 1회)
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
├── .github/                 # 이슈·PR 템플릿, CI 워크플로
├── .claude/docs/            # AI 에이전트 상세 가이드
├── src/                     # 소스 코드
├── tests/                   # 테스트
├── CLAUDE.md                # AI 코딩 에이전트 진입점
├── AGENTS.md → CLAUDE.md    # symlink
├── .agents → .claude        # symlink
├── branch_ruleset_main.json # main 브랜치 보호 규칙 (GitHub Ruleset import용)
├── .editorconfig            # 에디터 공통 설정
├── .python-version
├── .gitignore
├── .pre-commit-config.yaml
├── CONTRIBUTING.md
├── LICENSE
├── pyproject.toml           # 도구 설정 (ruff 등)
└── requirements.txt
```

## AI 에이전트 (Claude Code 등)

[`CLAUDE.md`](CLAUDE.md)가 진입점이고 상세 규칙은 `.claude/docs/`에 있습니다.
`AGENTS.md`는 `CLAUDE.md`의, `.agents`는 `.claude`의 symlink입니다.

## Contributing

[CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요. 브랜치 규칙은 `feat-{ISSUE}/{설명}` 형식입니다.

## License

MIT — 자세한 내용은 [LICENSE](LICENSE)를 참조하세요.
