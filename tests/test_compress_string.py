from string_lib.compress_string import compress_string


def test_compress_string():
    assert compress_string("abcdefg") == "1a1b1c1d1e1f1g"