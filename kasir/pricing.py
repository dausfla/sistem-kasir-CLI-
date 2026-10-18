"""Aturan perhitungan diskon."""

DISCOUNT_TIER_HIGH = 100_000
DISCOUNT_TIER_MID = 50_000
DISCOUNT_RATE_HIGH = 0.10
DISCOUNT_RATE_MID = 0.05


def calculate_discount(total: int) -> int:
    """Menghitung diskon berdasarkan total belanja.

    Aturan:
        - total >= 100.000 : diskon 10%
        - total >= 50.000  : diskon 5%
        - selain itu       : tanpa diskon
    """
    if total >= DISCOUNT_TIER_HIGH:
        return int(total * DISCOUNT_RATE_HIGH)
    if total >= DISCOUNT_TIER_MID:
        return int(total * DISCOUNT_RATE_MID)
    return 0
