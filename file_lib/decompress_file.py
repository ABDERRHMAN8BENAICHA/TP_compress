from string_lib.decompress_string import decompress_string


def decompress_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        data = f.read()

    decompressed_data = decompress_string(data)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(decompressed_data)