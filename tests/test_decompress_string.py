from string_lib.decompress_string import decompress_string


def test_decompress_string():
    assert decompress_string("1a1b1c1d1e1f1g") == "abcdefg"