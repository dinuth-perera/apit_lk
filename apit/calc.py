from collections import defaultdict

def calculate_apit(gross):
    annual_amount = int(gross * 12)

    ranges_and_calculations = defaultdict(
        lambda: 0,
        {
            (0, 1800000): 0,
            (1800000, 2800000): ((annual_amount - 1800000) / 12) * 0.06,
            (2800000, 3300000): (1000000 / 12) * 0.06 + ((annual_amount - 2800000) / 12) * 0.18,
            (3300000, 3800000): (1000000 / 12) * 0.06 + (500000 / 12) * 0.18 + ((annual_amount - 3300000) / 12) * 0.24,
            (3800000, 4300000): (1000000 / 12) * 0.06 + (500000 / 12) * 0.18 + (500000 / 12) * 0.24 + ((annual_amount - 3800000) / 12) * 0.30,
            (4300000, float("inf")): (
                (1000000 / 12) * 0.06 +
                (500000 / 12) * 0.18 +
                (500000 / 12) * 0.24 +
                (500000 / 12) * 0.30 +
                ((annual_amount - 4300000) / 12) * 0.36
            ),
        }
    )

    tax_amount = ranges_and_calculations[
        next(range_ for range_ in ranges_and_calculations.keys() if range_[0] < annual_amount <= range_[1])
    ]
    return round(tax_amount, 2)
