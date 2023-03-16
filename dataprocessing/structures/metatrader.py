class ColumnsNames:
    """Provide columns names for MetaTrader dataset.

    These columns names are used instead of original ones.
    """

    DATE = [
        'Date',
    ]
    TIME = [
        'Time',
    ]
    COMMON = [
        'Open',
        'High',
        'Low',
        'Close',
        'Tickvol',
    ]
    _VOL = [
        'Vol',
    ]
    SPREAD = [
        'Spread',
    ]

    GENERAL = DATE + COMMON + _VOL + SPREAD
    USE_GENERAL = DATE + COMMON

    INTRADAY = DATE + TIME + COMMON + _VOL + SPREAD
    USE_INTRADAY = DATE + TIME + COMMON + SPREAD


class ColumnsTypes:
    """Provide data types for columns.

    Is used in `pandas.read_csv()` in couple with corresponding description
    class.
    """

    _GENERAL_PRICES = {
        'Open': 'float64',
        'High': 'float64',
        'Low': 'float64',
        'Close': 'float64',
    }
    _FOREX_PRICES = {
        'Open': 'float32',
        'High': 'float32',
        'Low': 'float32',
        'Close': 'float32',
    }
    _TICKVOL = {
        'Tickvol': 'uint32',
    }
    _SPREAD = {
        'Spread': 'uint8',
    }

    GENERAL = _GENERAL_PRICES | _TICKVOL
    INTRADAY = GENERAL | _SPREAD

    FOREX = _FOREX_PRICES | _TICKVOL
    FOREX_INTRADAY = FOREX | _SPREAD
