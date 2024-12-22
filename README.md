<h1 align="center">Python Encoder & Decoder</h1>

<p align="center">
  <strong>Dibuat oleh Fanky</strong><br>
  Proyek ini menyediakan dua alat utama untuk encoding dan decoding file Python: <br>
  <b>encpython.py</b> (encoder) dan <b>decpython.py</b> (decoder).
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/Status-Active-success" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
</p>

---

## 📋 Fitur

- **Encoding Berlapis**:
  - Mendukung format: <strong>Base64</strong>, <strong>Hexadecimal</strong>, dan <strong>Binary</strong>.
  - Jumlah lapisan encoding dapat disesuaikan.
- **Decoder Otomatis**:
  - Mendeteksi format encoding secara otomatis.
  - Mendukung decoding berlapis hingga script asli ditemukan.
- **Mudah Digunakan** melalui Command Line Interface (CLI).

---

## 🛠️ Persyaratan

- **Python 3.x** harus terinstal di sistem.
- Tidak ada pustaka tambahan yang diperlukan.

---

## 🚀 Cara Pemasangan

1. **Unduh File**
   - Simpan file `encpython.py` dan `decpython.py` di direktori yang sama.

2. **Pastikan Python Terinstal**
   - Jalankan perintah berikut untuk memverifikasi instalasi Python:
     ```bash
     python --version
     ```
   - Jika belum terinstal, unduh Python dari <a href="https://www.python.org/">python.org</a>.

3. **Ubah Izin Eksekusi (Opsional, untuk Linux/MacOS)**
   - Jalankan perintah berikut untuk memberikan izin eksekusi:
     ```bash
     chmod +x encpython.py decpython.py
     ```

---

## 📖 Cara Penggunaan

### 1️⃣ Encoding dengan <code>encpython.py</code>

Gunakan script <code>encpython.py</code> untuk mengenkripsi file Python Anda.

#### Sintaks:
```bash
python encpython.py <input_file> <output_file> <method> <layers>
