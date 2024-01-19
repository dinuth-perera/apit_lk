from collections import defaultdict


def calculate_apit(gross):
    annual_amount = int(gross * 12)

    # Define the tax ranges and calculations
    ranges_and_calculations = defaultdict(
        lambda: 0,
        {
            (0, 1200000): 0,
            (1200000, 1700000): ((annual_amount - 1200000) / 12) * 0.06,
            (1700000, 2200000): (500000 / 12) * 0.06 + ((annual_amount - 1700000) / 12) * 0.12,
            (2200000, 2700000): (500000 / 12) * 0.06 + (500000 / 12) * 0.12 + ((annual_amount - 2200000) / 12) * 0.18,
            (2700000, 3200000): (500000 / 12) * 0.06
            + (500000 / 12) * 0.12
            + (500000 / 12) * 0.18
            + ((annual_amount - 2700000) / 12) * 0.24,
            (3200000, 3700000): (500000 / 12) * 0.06
            + (500000 / 12) * 0.12
            + (500000 / 12) * 0.18
            + (500000 / 12) * 0.24
            + ((annual_amount - 3200000) / 12) * 0.30,
            (3700000, float("inf")): (500000 / 12) * 0.06
            + (500000 / 12) * 0.12
            + (500000 / 12) * 0.18
            + (500000 / 12) * 0.24
            + (500000 / 12) * 0.30
            + ((annual_amount - 3700000) / 12) * 0.36,
        },
    )

    # calculation for the range
    tax_amount = ranges_and_calculations[
        next(range_ for range_ in ranges_and_calculations.keys() if range_[0] < annual_amount <= range_[1])
    ]
    return round(tax_amount, 2)



