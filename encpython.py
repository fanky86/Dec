import base64
import os
import sys

# Fungsi untuk encode script Python secara berlapis
def layered_encode(code, method="binary", layers=1):
    try:
        for _ in range(layers):
            if method == "binary":
                code = base64.b64encode(code.encode('utf-8')).decode('utf-8')
            elif method == "hex":
                code = code.encode('utf-8').hex()
            else:
                raise ValueError("Metode encoding tidak dikenal. Gunakan 'binary' atau 'hex'.")
        return code
    except Exception as e:
        raise ValueError(f"Error dalam proses encoding: {e}")

# Fungsi untuk menghasilkan script hasil encoding berlapis
def encode_script(input_file, output_file, method="binary", layers=1):
    try:
        with open(input_file, 'r') as file:
            original_code = file.read()

        encoded_code = layered_encode(original_code, method, layers)

        if method == "binary":
            decode_snippet = """
for _ in range({layers}):
    decoded_code = base64.b64decode(decoded_code).decode('utf-8')
"""
        elif method == "hex":
            decode_snippet = """
for _ in range({layers}):
    decoded_code = bytes.fromhex(decoded_code).decode('utf-8')
"""

        with open(output_file, 'w') as file:
            file.write(f"""
import base64
import os

# Script hasil encoding berlapis
encoded_code = "{encoded_code}"
decoded_code = encoded_code
{decode_snippet.format(layers=layers)}

# Simpan ke file sementara
temp_file = "temp_script.py"
with open(temp_file, 'w') as temp:
    temp.write(decoded_code)

# Jalankan file sementara
os.system(f'python {{temp_file}}')

# Hapus file sementara
os.remove(temp_file)
""")
        print(f"Script berhasil di-encode dengan {layers} lapisan metode '{method}' ke file: {output_file}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Menu utama untuk memilih metode dan jumlah lapisan encoding
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Penggunaan: python encoder.py <input_file> <output_file> <method> <layers>")
        print("Metode tersedia: binary, hex")
        print("Contoh: python encoder.py script_asli.py encoded_script.py binary 3")
    else:
        input_script = sys.argv[1]
        output_script = sys.argv[2]
        method = sys.argv[3].lower()
        try:
            layers = int(sys.argv[4])
            if layers < 1:
                raise ValueError("Jumlah lapisan harus >= 1")
        except ValueError as e:
            print(f"Kesalahan input jumlah lapisan: {e}")
            sys.exit(1)

        # Encode dengan metode dan lapisan yang dipilih
        encode_script(input_script, output_script, method, layers)
