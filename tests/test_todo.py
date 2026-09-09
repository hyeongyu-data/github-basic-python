from src.todo import main


def test_add_list_done_rm(tmp_path, capsys):
    f = str(tmp_path / "todo.json")

    assert main(["--file", f, "add", "우유 사기"]) == 0
    assert main(["--file", f, "add", "PR 리뷰"]) == 0

    assert main(["--file", f, "list"]) == 0
    out = capsys.readouterr().out
    assert "1. [ ] 우유 사기" in out
    assert "2. [ ] PR 리뷰" in out

    assert main(["--file", f, "done", "1"]) == 0
    assert main(["--file", f, "rm", "2"]) == 0
    capsys.readouterr()

    assert main(["--file", f, "list"]) == 0
    out = capsys.readouterr().out
    assert "1. [x] 우유 사기" in out
    assert "PR 리뷰" not in out


def test_empty_list(tmp_path, capsys):
    assert main(["--file", str(tmp_path / "x.json"), "list"]) == 0
    assert "할 일 없음" in capsys.readouterr().out


def test_out_of_range(tmp_path, capsys):
    f = str(tmp_path / "todo.json")
    main(["--file", f, "add", "하나"])
    capsys.readouterr()
    assert main(["--file", f, "done", "99"]) == 1
    assert "없습니다" in capsys.readouterr().out
