"""Model data untuk aplikasi kasir sederhana."""

from dataclasses import dataclass
from typing import Dict, List

MAX_QUANTITY_PER_ITEM = 99


@dataclass(frozen=True)
class Product:
    """Produk yang dijual di toko.

    Attributes:
        code: Kode unik produk, misalnya "P001".
        name: Nama produk.
        price: Harga satuan dalam Rupiah.
    """

    code: str
    name: str
    price: int


@dataclass
class CartItem:
    """Satu baris item di dalam keranjang belanja."""

    product: Product
    quantity: int

    @property
    def subtotal(self) -> int:
        """Mengembalikan harga satuan dikali jumlah."""
        return self.product.price * self.quantity


class Cart:
    """Keranjang belanja yang menyimpan item berdasarkan kode produk."""

    def __init__(self) -> None:
        self._items: Dict[str, CartItem] = {}

    def add_item(self, product: Product, quantity: int = 1) -> None:
        """Menambahkan produk ke keranjang.

        Raises:
            ValueError: Jika jumlah <= 0 atau melebihi batas maksimum.
        """
        if quantity <= 0:
            raise ValueError("Jumlah harus lebih dari 0.")

        current = self._items.get(product.code)
        new_quantity = quantity + (current.quantity if current else 0)
        if new_quantity > MAX_QUANTITY_PER_ITEM:
            raise ValueError(
                f"Jumlah maksimum per item adalah {MAX_QUANTITY_PER_ITEM}."
            )
        self._items[product.code] = CartItem(product, new_quantity)

    def remove_item(self, product_code: str) -> None:
        """Menghapus produk dari keranjang.

        Raises:
            KeyError: Jika produk tidak ada di keranjang.
        """
        if product_code not in self._items:
            raise KeyError(f"Produk {product_code} tidak ada di keranjang.")
        del self._items[product_code]

    @property
    def items(self) -> List[CartItem]:
        """Daftar item di keranjang."""
        return list(self._items.values())

    @property
    def total(self) -> int:
        """Total harga seluruh item sebelum diskon."""
        return sum(item.subtotal for item in self._items.values())

    def is_empty(self) -> bool:
        """Mengembalikan True jika keranjang kosong."""
        return not self._items
