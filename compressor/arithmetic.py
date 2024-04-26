import os
from arithmetic_coding.arithmetic_compress import encode
from arithmetic_coding.arithmetic_decompress import decode


def compress_text_file(input_file_path, output_file_path):
    """Compress a text file using arithmetic coding."""
    print(f"Compressing file: {input_file_path} -> {output_file_path}")

    encode(input_file_path, output_file_path)

    print(f"File compressed successfully: {input_file_path} -> {output_file_path}")


def decompress_text_file(input_file_path, output_file_path):
    """Decompress a text file using arithmetic coding."""
    print(f"Decompressing file: {input_file_path} -> {output_file_path}")

    decode(input_file_path, output_file_path)

    print(f"File decompressed successfully: {input_file_path} -> {output_file_path}")


def arithmetic_compress(input_folder_path, compressed_folder_path):
    """Compress all text files in a folder using arithmetic coding."""
    os.makedirs(compressed_folder_path, exist_ok=True)

    for filename in os.listdir(input_folder_path):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(input_folder_path, filename)
            output_file_path = os.path.join(
                compressed_folder_path, f"{filename[:-4]}.ac"
            )
            compress_text_file(input_file_path, output_file_path)


def arithmetic_decompress(compressed_folder_path, decompressed_folder_path):
    """Decompress all arithmetic-coded files in a folder."""
    os.makedirs(decompressed_folder_path, exist_ok=True)

    for filename in os.listdir(compressed_folder_path):
        if filename.endswith(".ac"):
            input_file_path = os.path.join(compressed_folder_path, filename)
            output_file_path = os.path.join(
                decompressed_folder_path, f"{filename[:-3]}.txt"
            )
            decompress_text_file(input_file_path, output_file_path)
