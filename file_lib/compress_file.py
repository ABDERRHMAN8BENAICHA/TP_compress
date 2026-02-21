from string_lib.compress_string import compress_string


def compress_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        data = f.read()

    compressed_data = compress_string(data)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(compressed_data)