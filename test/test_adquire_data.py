from source.adquire_data import read_data


def test_stream_raw_data():
    df = read_data()
    assert df.empty == False
