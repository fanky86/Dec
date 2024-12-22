import base64

# Fungsi untuk mendeteksi apakah string adalah Base64
def is_base64(s):
    try:
        base64.b64decode(s)
        return True
    except Exception:
        return False

# Fungsi untuk mendeteksi apakah string adalah Hexadecimal
def is_hex(s):
    try:
        bytes.fromhex(s)
        return True
    except Exception:
        return False

# Fungsi untuk mendeteksi apakah string adalah Binary (biner)
def is_binary(s):
    try:
        int(s, 2)  # Uji apakah string adalah angka biner
        return len(s) % 8 == 0  # Binary harus kelipatan 8 bit
    except Exception:
        return False

# Fungsi untuk mendecode string biner ke teks
def decode_binary(binary_string):
    bytes_data = int(binary_string, 2).to_bytes(len(binary_string) // 8, byteorder='big')
    return bytes_data.decode('utf-8')

# Fungsi untuk mendecode script secara otomatis
def auto_decode(encoded_code):
    layers = 0  # Menghitung jumlah lapisan
    while True:
        if is_base64(encoded_code):  # Jika encoded_code adalah Base64
            encoded_code = base64.b64decode(encoded_code).decode('utf-8')
            layers += 1
        elif is_hex(encoded_code):  # Jika encoded_code adalah Hexadecimal
            encoded_code = bytes.fromhex(encoded_code).decode('utf-8')
            layers += 1
        elif is_binary(encoded_code):  # Jika encoded_code adalah Binary
            encoded_code = decode_binary(encoded_code)
            layers += 1
        else:
            break  # Berhenti jika tidak bisa didecode lebih lanjut
    return encoded_code, layers

# Contoh penggunaan
if __name__ == "__main__":
    # Contoh hasil encode berlapis
    encoded_script = input("Masukkan script hasil encoding: ")

    decoded_script, total_layers = auto_decode(encoded_script)
    print(f"Script berhasil didecode dengan {total_layers} lapisan.")
    print("Script asli:")
    print(decoded_script)
