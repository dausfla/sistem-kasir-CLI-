"""Program utama sistem kasir sederhana (CLI)."""

from typing import Dict

from kasir.models import Cart, Product
from kasir.receipt import build_receipt, format_rupiah

CATALOG: Dict[str, Product] = {
    product.code: product
    for product in (
        Product("P001", "Beras 5kg", 65_000),
        Product("P002", "Minyak Goreng 1L", 18_000),
        Product("P003", "Gula Pasir 1kg", 16_000),
        Product("P004", "Telur 1kg", 28_000),
        Product("P005", "Kopi Sachet", 2_500),
    )
}

MENU = """
=== SISTEM KASIR ===
1. Lihat daftar produk
2. Tambah produk ke keranjang
3. Hapus produk dari keranjang
4. Lihat keranjang
5. Bayar & cetak struk
0. Keluar
"""


def show_catalog() -> None:
    """Menampilkan daftar produk yang tersedia."""
    for product in CATALOG.values():
        print(f"{product.code}  {product.name:<20} "
              f"{format_rupiah(product.price)}")


def show_cart(cart: Cart) -> None:
    """Menampilkan isi keranjang saat ini."""
    if cart.is_empty():
        print("Keranjang masih kosong.")
        return
    for item in cart.items:
        print(f"{item.product.code}  {item.product.name:<20} "
              f"x{item.quantity:<3} {format_rupiah(item.subtotal)}")
    print(f"Total: {format_rupiah(cart.total)}")


def handle_add(cart: Cart) -> None:
    """Menangani input penambahan produk ke keranjang."""
    code = input("Kode produk: ").strip().upper()
    product = CATALOG.get(code)
    if product is None:
        print("Kode produk tidak ditemukan.")
        return
    try:
        quantity = int(input("Jumlah: "))
        cart.add_item(product, quantity)
        print(f"{product.name} ditambahkan.")
    except ValueError as error:
        print(f"Input tidak valid: {error}")


def handle_remove(cart: Cart) -> None:
    """Menangani input penghapusan produk dari keranjang."""
    code = input("Kode produk yang dihapus: ").strip().upper()
    try:
        cart.remove_item(code)
        print("Produk dihapus.")
    except KeyError as error:
        print(error.args[0])


def handle_checkout(cart: Cart) -> bool:
    """Memproses pembayaran. Mengembalikan True jika transaksi selesai."""
    if cart.is_empty():
        print("Keranjang kosong, tidak ada yang dibayar.")
        return False
    try:
        paid = int(input("Uang dibayar: "))
        print(build_receipt(cart, paid))
        return True
    except ValueError as error:
        print(f"Pembayaran gagal: {error}")
        return False


def main() -> None:
    """Menjalankan loop menu utama."""
    cart = Cart()
    while True:
        print(MENU)
        choice = input("Pilih menu: ").strip()
        if choice == "1":
            show_catalog()
        elif choice == "2":
            handle_add(cart)
        elif choice == "3":
            handle_remove(cart)
        elif choice == "4":
            show_cart(cart)
        elif choice == "5":
            if handle_checkout(cart):
                cart = Cart()
        elif choice == "0":
            print("Terima kasih!")
            break
        else:
            print("Menu tidak dikenal.")


if __name__ == "__main__":
    main()
