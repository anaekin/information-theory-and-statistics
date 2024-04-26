import os
from bwt_compressor.compressor import compress, decompress


def compress_text_file(input_file_path, output_file_path):
    print(f"Compressing file: {input_file_path} -> {output_file_path}")
    with open(input_file_path, "r", encoding="utf-8") as f_in:
        file_content = f_in.read()

    # Perform BWT compression on text content
    compressed_content = compress(file_content)

    # Write compressed content to output file
    with open(output_file_path, "wb") as f_out:
        f_out.write(compressed_content)

    print(f"File compressed successfully: {input_file_path} -> {output_file_path}")


def decompress_text_file(input_file_path, output_file_path):
    print(f"Decompressing file: {input_file_path} -> {output_file_path}")
    with open(input_file_path, "rb") as f_in:
        compressed_content = f_in.read()

    # Perform BWT decompression on compressed content
    decompressed_content = decompress(compressed_content)

    # Write decompressed content to output file
    with open(output_file_path, "w", encoding="utf-8") as f_out:
        f_out.write(decompressed_content)

    print(f"File decompressed successfully: {input_file_path} -> {output_file_path}")


def bwt_compress(input_folder_path, compressed_folder_path):
    """Compress all text files in a folder using BWT compression."""
    os.makedirs(compressed_folder_path, exist_ok=True)

    for filename in os.listdir(input_folder_path):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(input_folder_path, filename)
            output_file_path = os.path.join(
                compressed_folder_path, f"{filename[:-4]}.bwt"
            )
            compress_text_file(input_file_path, output_file_path)


def bwt_decompress(compressed_folder_path, decompressed_folder_path):
    """Decompress all BWT-compressed files in a folder."""
    os.makedirs(decompressed_folder_path, exist_ok=True)

    for filename in os.listdir(compressed_folder_path):
        if filename.endswith(".bwt"):
            input_file_path = os.path.join(compressed_folder_path, filename)
            output_file_path = os.path.join(
                decompressed_folder_path, f"{filename[:-4]}.txt"
            )
            decompress_text_file(input_file_path, output_file_path)
