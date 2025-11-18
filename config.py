import argparse


def configure_arg_parser():
    parser = argparse.ArgumentParser(
        description='Парсер информации по сотрудникам'
    )

    parser.add_argument(
        '-f',
        '--files',
        nargs='+',
        required=True,
        help='Путь к CSV-файлам'
    )
    parser.add_argument(
        '-r',
        '--report',
        choices=['performance'],
        required=True,
        help=(
            'Средняя эфективность сотрудников сгруппированных по позициям'
        )
    )

    return parser
