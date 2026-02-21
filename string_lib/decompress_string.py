def decompress_string(data):
    number = ""
    decompressed = []

    for char in data:
        if char.isdigit():
            number += char
        else:
            count = int(number) if number else 1
            decompressed.append(char * count)
            number = ""

    return ''.join(decompressed)