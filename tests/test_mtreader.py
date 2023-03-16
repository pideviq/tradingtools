import unittest
import pandas
from pathlib import Path
from dataprocessing.readers.metatrader import MTReader
from dataprocessing.structures.metatrader import ColumnsNames, ColumnsTypes


class MTReaderTestCase(unittest.TestCase):

    def setUp(self) -> None:
        samples_folder: Path = Path.cwd().parent / 'samples'
        self.files: dict = {
            'general': samples_folder / 'mt_general.csv',
            'intraday_forex': samples_folder / 'mt_intraday_forex.csv',
        }

    def test_read_csv_with_general_data(self) -> None:
        general_data = MTReader(self.files['general']).read_csv()
        self.assertIsInstance(general_data, pandas.DataFrame)
        self.assertEqual(ColumnsNames.COMMON,
                         general_data.columns.values.tolist())
        self.assertEqual(ColumnsTypes.GENERAL, general_data.dtypes.to_dict())
        self.assertAlmostEqual(1807.84, general_data['Close'].iloc[-1], 2)
        self.assertEqual(497481, general_data['Tickvol'].iloc[-1])

    def test_read_csv_with_intraday_forex_data(self) -> None:
        forex_reader = MTReader(self.files['intraday_forex'],
                                is_intraday=True,
                                is_forex=True)
        forex_data = forex_reader.read_csv()
        columns = ColumnsNames.COMMON + ColumnsNames.SPREAD
        self.assertEqual(columns, forex_data.columns.values.tolist())
        self.assertEqual(ColumnsTypes.FOREX_INTRADAY,
                         forex_data.dtypes[columns].to_dict())
        self.assertAlmostEqual(1.21387, forex_data.iloc[0]['Close'], 5)
        self.assertEqual(7, forex_data.iloc[0]['Spread'])

    def test_empty_filename(self) -> None:
        with self.assertRaises(AttributeError):
            MTReader('')

    def test_folder_name_instead_of_filename(self) -> None:
        with self.assertRaises(FileNotFoundError):
            MTReader(Path.cwd())

    def test_non_existent_filename(self) -> None:
        with self.assertRaises(FileNotFoundError):
            MTReader(self.files['general'].parent / 'error.csv')

    def test_read_csv_with_non_csv(self) -> None:
        with self.assertRaises(ValueError):
            MTReader(Path(__file__)).read_csv()


if __name__ == '__main__':
    unittest.main()
