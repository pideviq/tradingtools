import pandas
from pathlib import Path
from dataprocessing.structures.metatrader import ColumnsNames, ColumnsTypes


class MTReader:
    """MetaTrader dataset reader."""

    _filepath: Path = None
    _parse_dates: list = None
    _columns_names: list = None
    _use_columns: list = None
    _columns_types: dict = None

    def __init__(self, filepath: Path, is_intraday: bool = False,
                 is_forex: bool = False) -> None:
        """Initialize new reader for the dataset.

        :param Path filepath: path to raw dataset file
        :param bool is_intraday: is period less than *1 Day* (default False)?
        :param bool is_forex: is instrument related to FOREX (default False)?
        :raises FileNotFoundError: if there is no such file
        :raises AttributeError: if `filepath` is not an instance of Path
        """
        try:
            if filepath.exists() and filepath.is_file():
                self._filepath = filepath
            else:
                raise FileNotFoundError('No such file')
        except AttributeError:
            raise AttributeError(
                "'filepath' must be an instance of 'pathlib.Path'")

        if is_intraday:
            self._parse_dates = [ColumnsNames.DATE + ColumnsNames.TIME]
            self._columns_names = ColumnsNames.INTRADAY
            self._use_columns = ColumnsNames.USE_INTRADAY
            self._columns_types = ColumnsTypes.FOREX_INTRADAY if is_forex \
                else ColumnsTypes.INTRADAY
        else:
            self._parse_dates = ColumnsNames.DATE
            self._columns_names = ColumnsNames.GENERAL
            self._use_columns = ColumnsNames.USE_GENERAL
            self._columns_types = ColumnsTypes.FOREX if is_forex else \
                ColumnsTypes.GENERAL

    def read_csv(self) -> pandas.DataFrame:
        """`pandas.read_csv()` wrapper. Return DataFrame object.

        :returns: DataFrame object with loaded data
        :raises ValueError: if file type is not '.csv'
        """
        if self._filepath.suffix != '.csv':
            raise ValueError("call 'read_csv()' with incorrect file type")
        return pandas.read_csv(
            self._filepath,
            sep='\t',
            index_col=0,
            header=0,
            parse_dates=self._parse_dates,
            names=self._columns_names,
            usecols=self._use_columns,
            dtype=self._columns_types)
