import numpy as np
from dateutil.relativedelta import relativedelta


def apply_payment_into_asset(asset, payoff_amount, payoff_date):
    if payoff_date in asset.value.keys():
        asset.value[payoff_date] += payoff_amount
    else:
        asset.value[payoff_date] = asset.get_value(payoff_date) + payoff_amount
    return asset


def apply_regular_payment_into_asset(asset, regular_amount, interval, from_date, to_date):
    # interval is a relative delta object
    # apply regular payments into asset from from_date to to_date
    apply_date = from_date
    while apply_date < to_date:
        asset = apply_payment_into_asset(asset, regular_amount, apply_date)
        apply_date += interval
    return asset
