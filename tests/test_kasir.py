"""Unit test untuk modul kasir."""

import unittest

from kasir.models import Cart, Product
from kasir.pricing import calculate_discount
from kasir.receipt import build_receipt, format_rupiah

SAMPLE_PRODUCT = Product("P001", "Beras 5kg", 65_000)


class CartTest(unittest.TestCase):
    """Pengujian kelas Cart."""

    def test_add_item_accumulates_quantity(self) -> None:
        cart = Cart()
        cart.add_item(SAMPLE_PRODUCT, 1)
        cart.add_item(SAMPLE_PRODUCT, 2)
        self.assertEqual(cart.total, 195_000)

    def test_add_item_rejects_zero_quantity(self) -> None:
        with self.assertRaises(ValueError):
            Cart().add_item(SAMPLE_PRODUCT, 0)

    def test_remove_missing_item_raises_key_error(self) -> None:
        with self.assertRaises(KeyError):
            Cart().remove_item("P999")


class PricingTest(unittest.TestCase):
    """Pengujian aturan diskon."""

    def test_no_discount(self) -> None:
        self.assertEqual(calculate_discount(49_999), 0)

    def test_mid_discount(self) -> None:
        self.assertEqual(calculate_discount(50_000), 2_500)

    def test_high_discount(self) -> None:
        self.assertEqual(calculate_discount(100_000), 10_000)


class ReceiptTest(unittest.TestCase):
    """Pengujian pembuatan struk."""

    def test_format_rupiah(self) -> None:
        self.assertEqual(format_rupiah(1_250_000), "Rp 1.250.000")

    def test_insufficient_payment_raises_error(self) -> None:
        cart = Cart()
        cart.add_item(SAMPLE_PRODUCT, 1)
        with self.assertRaises(ValueError):
            build_receipt(cart, 1_000)


if __name__ == "__main__":
    unittest.main()
