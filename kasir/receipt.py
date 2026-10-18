"""Pembuatan struk pembayaran."""

from kasir.models import Cart
from kasir.pricing import calculate_discount

RECEIPT_WIDTH = 44


def format_rupiah(amount: int) -> str:
    """Memformat angka menjadi format Rupiah, contoh: Rp 15.000."""
    return "Rp " + f"{amount:,}".replace(",", ".")


def build_receipt(cart: Cart, paid: int) -> str:
    """Membuat teks struk dari isi keranjang dan jumlah uang dibayar.

    Raises:
        ValueError: Jika uang yang dibayar kurang dari total akhir.
    """
    discount = calculate_discount(cart.total)
    grand_total = cart.total - discount
    if paid < grand_total:
        raise ValueError("Uang pembayaran kurang.")

    line = "=" * RECEIPT_WIDTH
    rows = [line, "STRUK PEMBELIAN".center(RECEIPT_WIDTH), line]
    for item in cart.items:
        rows.append(f"{item.product.name} x{item.quantity}")
        rows.append(f"{format_rupiah(item.subtotal):>{RECEIPT_WIDTH}}")
    rows.append("-" * RECEIPT_WIDTH)
    summary = [
        ("Total", cart.total),
        ("Diskon", -discount),
        ("Grand Total", grand_total),
        ("Bayar", paid),
        ("Kembalian", paid - grand_total),
    ]
    for label, value in summary:
        amount = format_rupiah(value)
        rows.append(f"{label:<20}{amount:>{RECEIPT_WIDTH - 20}}")
    rows.append(line)
    return "\n".join(rows)
