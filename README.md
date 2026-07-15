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
