from file_lib.compress_file import compress_file
from string_lib.decompress_string import decompress_string


def test_compress_file_real_paths():
    input_path = "./data/original.txt"
    output_path = "./data/compressed_original.txt"

    compress_file(input_path, output_path)

    with open(output_path, "r", encoding="utf-8") as f:
        compressed = f.read()

    assert compressed != ""


def test_compress_then_decompress_real_paths():
    input_path = "./data/original.txt"
    compressed_path = "./data/compressed_original.txt"

    compress_file(input_path, compressed_path)

    with open(compressed_path, "r", encoding="utf-8") as f:
        compressed = f.read()

    decompressed = decompress_string(compressed)

    with open(input_path, "r", encoding="utf-8") as f:
        original = f.read()

    assert decompressed == original