from main import build_performance_table


def test_build_performance_table_group_and_average(sample_rows):
    table = build_performance_table(sample_rows)

    assert len(table) == 2

    assert table[0]['position'] == 'Backend Developer'
    assert table[0]['performance'] == 4.85

    assert table[1]['position'] == 'Mobile Developer'
    assert table[1]['performance'] == 4.6


def test_build_performance_table_ignores_broken_rows(broken_rows):
    table = build_performance_table(broken_rows)

    assert len(table) == 1
    assert table[0]['position'] == 'Backend Developer'
    assert table[0]['performance'] == 6.0
