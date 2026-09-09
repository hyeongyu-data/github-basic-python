"""최소한의 할 일 목록 CLI.

저장 위치: --file 인자 > TODO_FILE 환경변수 > ~/.todo.json
"""

import argparse
import json
import os
from pathlib import Path


def _resolve_path(file_arg: str | None) -> Path:
    if file_arg:
        return Path(file_arg)
    return Path(os.environ.get("TODO_FILE") or Path.home() / ".todo.json")


def _load(path: Path) -> list[dict]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return []


def _save(path: Path, items: list[dict]) -> None:
    path.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")


def _render(items: list[dict]) -> str:
    if not items:
        return "(할 일 없음)"
    return "\n".join(
        f"{i}. [{'x' if it['done'] else ' '}] {it['text']}"
        for i, it in enumerate(items, start=1)
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="todo", description="간단한 할 일 목록")
    parser.add_argument("--file", help="할 일 저장 파일 경로")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list", help="전체 목록 출력")
    p_add = sub.add_parser("add", help="할 일 추가")
    p_add.add_argument("text", help="할 일 내용")
    p_done = sub.add_parser("done", help="완료 표시")
    p_done.add_argument("number", type=int, help="항목 번호 (1부터)")
    p_rm = sub.add_parser("rm", help="항목 삭제")
    p_rm.add_argument("number", type=int, help="항목 번호 (1부터)")

    args = parser.parse_args(argv)
    path = _resolve_path(args.file)
    items = _load(path)

    if args.command == "list":
        print(_render(items))
        return 0

    if args.command == "add":
        items.append({"text": args.text, "done": False})
        _save(path, items)
        print(f"추가됨: {args.text}")
        return 0

    # done / rm — 번호 검증 공통
    if not 1 <= args.number <= len(items):
        print(f"오류: {args.number}번 항목이 없습니다 (1~{len(items)})")
        return 1

    target = items[args.number - 1]
    if args.command == "done":
        target["done"] = True
        _save(path, items)
        print(f"완료: {target['text']}")
    else:  # rm
        items.pop(args.number - 1)
        _save(path, items)
        print(f"삭제됨: {target['text']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
