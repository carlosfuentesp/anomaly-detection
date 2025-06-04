import pandas as pd
from unittest.mock import patch
from source.machine_learning.adquire_data import read_data


def test_stream_raw_data():
    # create a small DataFrame with the correct number of columns
    sample_df = pd.DataFrame([list(range(42))])
    with patch('source.machine_learning.adquire_data.get_file', return_value='dummy_path'), \
         patch('pandas.read_csv', return_value=sample_df.copy()):
        df = read_data()
    assert not df.empty
