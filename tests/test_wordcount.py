from hello_python.wordcount import word_frequency


def test_simple_counter():
    text = "Hello world hello"
    result = word_frequency(text)
    assert result == {"hello": 2, "world": 1}


def test_punctuation_and_case():
    text = "Dogs, dogs! Cats; cats. DOGS"
    result = word_frequency(text)
    assert result["dogs"] == 3
    assert result["cats"] == 2


def test_empty_string():
    assert word_frequency("") == {}


def test_big_file(tmp_path):
    # simular archivo temporal grande
    content = "lorem ipsum dolor sit amet\n" * 1000
    file = tmp_path / "big.txt"
    file.write_text(content)

    text = file.read_text()
    result = word_frequency(text)
    assert result["lorem"] == 1000
    assert result["ipsum"] == 1000
