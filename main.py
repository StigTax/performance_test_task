import csv
from collections import defaultdict

from tabulate import tabulate

from config import configure_arg_parser


def read_csv(files):
    rows = []

    for file in files:
        with open(file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows.extend(reader)
    return rows


def build_performance_table(rows):
    stats = defaultdict(lambda: {'sum': 0.0, 'count': 0.0})
    for row in rows:
        try:
            position = row['position']
            performance = float(row['performance'])
        except (KeyError, ValueError):
            continue

        stats[position]['sum'] += performance
        stats[position]['count'] += 1

    table = []
    for position, perform in stats.items():
        avg = perform['sum'] / perform['count']
        table.append(
            {
                'position': position,
                'performance': round(avg, 2),
            }
        )
    table.sort(key=lambda row: row['performance'], reverse=True)
    return table


def get_performance(rows):
    table = build_performance_table(rows)
    print(
        tabulate(
            table,
            headers='keys',
            tablefmt='github',
            showindex=range(1, len(table) + 1),
            floatfmt=".1f",
        )
    )


REPORT_HANDLERS = {
    'performance': get_performance,
}


def main():
    parser = configure_arg_parser()
    args = parser.parse_args()

    rows = read_csv(args.files)

    handler = REPORT_HANDLERS.get(args.report)
    handler(rows)


if __name__ == '__main__':
    main()
