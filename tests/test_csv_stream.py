import os
import time
from hello_python.csv_stream import stream_csv


def test_stream_csv_reads_lines(tmp_path):
    file_path = tmp_path / "big.scv"
    lines = [f"{i},val{i}" for i in range(11)]
    file_path.write_text("\n".join(lines), encoding="utf-8")

    gen = stream_csv(str(file_path))

    first = next(gen)
    assert first == ["0", "val0"]

    second = next(gen)
    assert second == ["1", "val1"]

    all_rows = list(stream_csv(str(file_path)))
    assert len(all_rows) == 11


def test_stream_csv_memory(tmp_path):
    file_path = tmp_path / "huge.csv"
    file_path.write_text("\n".join(f"{i},x" for i in range(1_000)))

    gen = stream_csv(str(file_path))
    rows = [next(gen) for _ in range(5)]
    assert rows[0] == ["0", "x"]
    assert rows[-1] == ["4", "x"]


def test_inspect_tmp(tmp_path):
    p = tmp_path / "peek.csv"
    # p.write_text("1,x\n2,y\n")
    p.write_text([f"{i},x\n" for i in range(100)])
    print(f"TMP: {tmp_path}")  # muestra la ruta
    if os.getenv("PAUSE_TESTS") == "1":
        time.sleep(30)  # tiempo para abrir el dir en otro terminal
    rows = list(stream_csv(str(p)))
    assert rows == [["1", "x"], ["2", "y"]]
