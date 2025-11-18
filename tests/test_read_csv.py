from main import read_csv


def test_read_csv_marge_multiple_files(csv_files):
    rows = read_csv(csv_files)

    assert len(rows) == 2

    names = {row['name'] for row in rows}
    assert names == {'David Chen', 'Elena Popova'}

    positions = {row['position'] for row in rows}
    assert positions == {'Mobile Developer', 'Backend Developer'}
