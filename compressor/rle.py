import os


def encode_bits(bits):
    """Compress binary data using Run-Length Encoding (RLE) on bits."""
    compressed_data = bytearray()
    i = 0
    while i < len(bits):
        bit = bits[i]
        count = 1
        while i + 1 < len(bits) and bits[i + 1] == bit:
            count += 1
            i += 1
        compressed_data.extend([count, bit])
        i += 1
    return compressed_data


def decode_bits(compressed_data):
    """Decompress binary data encoded with Run-Length Encoding (RLE) on bits."""
    decompressed_data = bytearray()
    i = 0
    while i < len(compressed_data):
        count = compressed_data[i]
        bit = compressed_data[i + 1]
        decompressed_data.extend([bit] * count)
        i += 2
    return decompressed_data


def read_binary_file(file_path):
    """Read the contents of a binary file."""
    with open(file_path, "rb") as file:
        return file.read()


def write_compressed_binary_file(encoded_data, output_file_path):
    """Write the compressed binary data to a file."""
    with open(output_file_path, "wb") as file:
        file.write(encoded_data)


def compress_binary_file(input_file_path, output_file_path):
    print(f"Compressing file: {input_file_path} -> {output_file_path}")
    """Compress a binary file using Run-Length Encoding (RLE) on bits."""
    # Read the input binary file
    original_data = read_binary_file(input_file_path)

    # Compress the data using Run-Length Encoding on bits
    compressed_data = encode_bits(original_data)

    # Write the compressed data to the output file
    write_compressed_binary_file(compressed_data, output_file_path)

    print(f"File compressed successfully: {input_file_path} -> {output_file_path}")


def decompress_binary_file(input_file_path, output_file_path):
    print(f"Decompressing file: {input_file_path} -> {output_file_path}")
    """Decompress a binary file encoded with Run-Length Encoding (RLE) on bits."""
    # Read the compressed data from the input file
    compressed_data = read_binary_file(input_file_path)

    # Decompress the data using Run-Length Encoding on bits
    decompressed_data = decode_bits(compressed_data)

    # Write the decompressed data to the output file
    with open(output_file_path, "wb") as file:
        file.write(decompressed_data)

    print(f"File decompressed successfully: {input_file_path} -> {output_file_path}")


def rle_compress(input_folder_path, compressed_folder_path):
    """Compress all binary files in a folder using Run-Length Encoding (RLE) on bits."""
    os.makedirs(compressed_folder_path, exist_ok=True)

    for filename in os.listdir(input_folder_path):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(input_folder_path, filename)
            output_file_path = os.path.join(
                compressed_folder_path, f"{filename[:-4]}.rle"
            )
            compress_binary_file(input_file_path, output_file_path)


def rle_decompress(folder_path, decompressed_folder_path):
    """Decompress all binary files in a folder encoded with Run-Length Encoding (RLE) on bits."""
    os.makedirs(decompressed_folder_path, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.endswith(".rle"):
            input_file_path = os.path.join(folder_path, filename)
            output_file_path = os.path.join(
                decompressed_folder_path, f"{filename[:-4]}.bin"
            )
            decompress_binary_file(input_file_path, output_file_path)
