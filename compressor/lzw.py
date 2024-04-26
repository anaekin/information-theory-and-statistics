import os
from lzw3.compressor import LZWCompressor
from lzw3.decompressor import LZWDecompressor

encode = LZWCompressor().compress
decode = LZWDecompressor().decompress


def compress_text_file(input_file_path, output_file_path):
    print(f"Compressing file: {input_file_path} -> {output_file_path}")

    # Perform LZW compression on text content
    encode(input_file_path, output_file_path)

    print(f"File compressed successfully: {input_file_path} -> {output_file_path}")


def decompress_text_file(input_file_path, output_file_path):
    print(f"Decompressing file: {input_file_path} -> {output_file_path}")

    # Perform LZW decompression on compressed content
    decode(input_file_path, output_file_path)

    print(f"File decompressed successfully: {input_file_path} -> {output_file_path}")


def lzw_compress(input_folder_path, compressed_folder_path):
    """Compress all text files in a folder using LZW compression."""
    os.makedirs(compressed_folder_path, exist_ok=True)

    for filename in os.listdir(input_folder_path):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(input_folder_path, filename)
            output_file_path = os.path.join(
                compressed_folder_path, f"{filename[:-4]}.lzw"
            )
            compress_text_file(input_file_path, output_file_path)


def lzw_decompress(compressed_folder_path, decompressed_folder_path):
    """Decompress all LZW-compressed files in a folder."""
    os.makedirs(decompressed_folder_path, exist_ok=True)

    for filename in os.listdir(compressed_folder_path):
        if filename.endswith(".lzw"):
            input_file_path = os.path.join(compressed_folder_path, filename)
            output_file_path = os.path.join(
                decompressed_folder_path, f"{filename[:-4]}.txt"
            )
            decompress_text_file(input_file_path, output_file_path)
