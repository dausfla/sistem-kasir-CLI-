# Coding Standard yang Diterapkan

Bahasa: **Python 3** - Standar: **PEP 8** (gaya kode) dan **PEP 257** (docstring).

| Aspek | Aturan | Contoh di proyek |
|-------|--------|------------------|
| Nama variabel & fungsi | `snake_case` | `calculate_discount`, `grand_total` |
| Nama kelas | `PascalCase` | `Cart`, `CartItem`, `Product` |
| Konstanta | `UPPER_SNAKE_CASE` | `MAX_QUANTITY_PER_ITEM` |
| Atribut privat | awalan `_` | `Cart._items` |
| Indentasi | 4 spasi, tanpa tab | semua file |
| Panjang baris | maksimal 79 karakter | semua file |
| Docstring | setiap modul, kelas, dan fungsi publik | `kasir/models.py` |
| Type hints | parameter dan return type | `def add_item(self, product: Product, quantity: int = 1) -> None` |
| Import | urut: standard library, lalu modul lokal; satu import per baris | `main.py` |
| Magic number | dipindah menjadi konstanta bernama | `DISCOUNT_TIER_HIGH = 100_000` |
| Struktur | satu tanggung jawab per modul | `models`, `pricing`, `receipt` |

## Konvensi Commit Git

Format: `tipe: deskripsi singkat`

- `feat` : fitur baru
- `fix`  : perbaikan bug
- `docs` : perubahan dokumentasi
- `test` : penambahan/perubahan test
- `chore`: pekerjaan pendukung (konfigurasi, setup)

## Cara Memeriksa Standar

```bash
pip install flake8
flake8 .
python -m unittest discover -v
```
