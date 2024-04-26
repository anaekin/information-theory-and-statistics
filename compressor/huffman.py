import os
import huffman_coding

encode = huffman_coding.encode
decode = huffman_coding.decode


def compress_text_file(input_file_path, output_file_path):
    print(f"Compressing file: {input_file_path} -> {output_file_path}")
    with (
        open(input_file_path, mode="r", newline="") as f_in,
        open(output_file_path, mode="wb", buffering=0) as f_out,
    ):
        try:
            encode(f_in=f_in, f_out=f_out)
        finally:
            f_in.close()
            f_out.close()

    print(f"File compressed successfully: {input_file_path} -> {output_file_path}")


def decompress_text_file(input_file_path, output_file_path):
    print(f"Decompressing file: {input_file_path} -> {output_file_path}")
    with (
        open(input_file_path, mode="rb", buffering=0) as f_in,
        open(output_file_path, mode="w", newline="") as f_out,
    ):
        try:
            decode(f_in=f_in, f_out=f_out)
        finally:
            f_in.close()
            f_out.close()

    print(f"File decompressed successfully: {input_file_path} -> {output_file_path}")


def huffman_compress(folder_path, compressed_folder_path):
    """Compress all text files in a folder using Huffman coding."""
    # Create compressed folder if it does not exist
    os.makedirs(compressed_folder_path, exist_ok=True)

    # Iterate over files in the input folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(folder_path, filename)
            output_file_path = os.path.join(
                compressed_folder_path, f"{filename[:-4]}.bin"
            )
            compress_text_file(input_file_path, output_file_path)


def huffman_decompress(folder_path, decompressed_folder_path):
    """Compress all text files in a folder using Huffman coding."""
    # Create compressed folder if it does not exist
    os.makedirs(decompressed_folder_path, exist_ok=True)

    # Iterate over files in the input folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".bin"):
            input_file_path = os.path.join(folder_path, filename)
            output_file_path = os.path.join(
                decompressed_folder_path, f"{filename[:-4]}.txt"
            )
            decompress_text_file(input_file_path, output_file_path)
