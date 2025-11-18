import sys
from pathlib import Path

import pytest

ROOT_DIR = Path(__file__).resolve().parents[1]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

HEADER = (
    'name,position,completed_tasks,performance,skills,team,experience_years\n'
)


@pytest.fixture
def sample_rows():
    """Нормальные строки из CSV для build_performance_table (dict)."""
    return [
        {
            'name': 'David Chen',
            'position': 'Mobile Developer',
            'completed_tasks': '36',
            'performance': '4.6',
            'skills': 'Swift...',
            'team': 'Mobile Team',
            'experience_years': '3',
        },
        {
            'name': 'Elena Popova',
            'position': 'Backend Developer',
            'completed_tasks': '43',
            'performance': '4.8',
            'skills': 'Java...',
            'team': 'API Team',
            'experience_years': '4',
        },
        {
            'name': 'Tom Anderson',
            'position': 'Backend Developer',
            'completed_tasks': '49',
            'performance': '4.9',
            'skills': 'Go...',
            'team': 'API Team',
            'experience_years': '7',
        },
    ]


@pytest.fixture
def broken_rows():
    """Строки с некорректными performance, чтобы проверить игнор."""
    return [
        {
            'name': 'Alice',
            'position': 'Backend Developer',
            'completed_tasks': '10',
            'performance': 'not-a-number',
            'skills': 'Python',
            'team': 'API Team',
            'experience_years': '3',
        },
        {
            'name': 'Bob',
            'position': 'Backend Developer',
            'completed_tasks': '5',
            'performance': '6.0',
            'skills': 'Go',
            'team': 'API Team',
            'experience_years': '2',
        },
    ]


@pytest.fixture
def csv_files(tmp_path):
    """Два CSV-файла с одинаковым хедером для теста read_csv."""
    file1 = tmp_path / 'file1.csv'
    file1.write_text(
        HEADER
        + 'David Chen,Mobile Developer,36,4.6,'
          '"Swift, Kotlin, React Native, iOS",Mobile Team,3\n',
        encoding='utf-8',
    )

    file2 = tmp_path / 'file2.csv'
    file2.write_text(
        HEADER
        + 'Elena Popova,Backend Developer,43,4.8,'
          '"Java, Spring Boot, MySQL, Redis",API Team,4\n',
        encoding='utf-8',
    )

    return [str(file1), str(file2)]


@pytest.fixture
def cli_args_performance(tmp_path, monkeypatch):
    """Файл + подмена sys.argv для main()."""
    data_file = tmp_path / 'data.csv'
    data_file.write_text(
        HEADER
        + 'Alice,Backend Developer,10,4.0,"Python, Django",Backend Team,3\n'
        + 'Bob,Backend Developer,5,6.0,"Go, gRPC",Backend Team,2\n',
        encoding='utf-8',
    )

    monkeypatch.setattr(
        sys,
        'argv',
        ['main.py', '-f', str(data_file), '-r', 'performance'],
    )
    return str(data_file)
