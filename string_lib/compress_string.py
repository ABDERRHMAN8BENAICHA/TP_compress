def compress_string(data):
    if not data:
        return ""

    compressed = []
    count = 1

    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            count += 1
        else:
            compressed.append(str(count) + data[i-1])
            count = 1

    compressed.append(str(count) + data[-1])
    return ''.join(compressed)