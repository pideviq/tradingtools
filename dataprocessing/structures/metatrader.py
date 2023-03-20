from typing import Final


class ColumnsNames:
    """Provide columns names for MetaTrader dataset.

    These columns names are used instead of original ones.
    """

    DATE: Final[str] = 'Date'
    TIME: Final[str] = 'Time'
    OPEN: Final[str] = 'Open'
    HIGH: Final[str] = 'High'
    LOW: Final[str] = 'Low'
    CLOSE: Final[str] = 'Close'
    TICKVOL: Final[str] = 'Tickvol'
    VOL: Final[str] = 'Vol'
    SPREAD: Final[str] = 'Spread'

    COMMON: Final[list[str]] = [
        OPEN,
        HIGH,
        LOW,
        CLOSE,
        TICKVOL,
    ]

    GENERAL: Final[list[str]] = [DATE] + COMMON + [VOL, SPREAD]
    USE_GENERAL: Final[list[str]] = [DATE] + COMMON

    INTRADAY: Final[list[str]] = [DATE, TIME] + COMMON + [VOL, SPREAD]
    USE_INTRADAY: Final[list[str]] = [DATE, TIME] + COMMON + [SPREAD]


class ColumnsTypes:
    """Provide data types for columns.

    Is used in `pandas.read_csv()` in couple with corresponding description
    class.
    """

    _PRICE_COLUMNS: Final[tuple[str]] = (
        ColumnsNames.OPEN,
        ColumnsNames.HIGH,
        ColumnsNames.LOW,
        ColumnsNames.CLOSE,
    )

    _GENERAL_PRICES: Final[dict[str: str]] = {
        column: 'float64' for column in _PRICE_COLUMNS}
    _FOREX_PRICES: Final[dict[str: str]] = {
        column: 'float32' for column in _PRICE_COLUMNS}
    _TICKVOL: Final[dict[str: str]] = {
        ColumnsNames.TICKVOL: 'uint32',
    }
    _SPREAD: Final[dict[str: str]] = {
        ColumnsNames.SPREAD: 'uint8',
    }

    GENERAL: Final[dict[str: str]] = _GENERAL_PRICES | _TICKVOL
    INTRADAY: Final[dict[str: str]] = GENERAL | _SPREAD

    FOREX: Final[dict[str: str]] = _FOREX_PRICES | _TICKVOL
    FOREX_INTRADAY: Final[dict[str: str]] = FOREX | _SPREAD
