#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""
import sys


if __name__ == '__main__':
    total_size, line_count = 0, 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status_stats = {code: 0 for code in status_codes}

    def display_stats(statistics: dict, file_size: int) -> None:
        print("File size: {:d}".format(file_size))
        for code, count in sorted(statistics.items()):
            if count:
                print("{}: {}".format(code, count))

    try:
        for input_line in sys.stdin:
            line_count += 1
            data_parts = input_line.split()
            try:
                code = data_parts[-2]
                if code in status_stats:
                    status_stats[code] += 1
            except BaseException:
                pass
            try:
                total_size += int(data_parts[-1])
            except BaseException:
                pass
            if line_count % 10 == 0:
                display_stats(status_stats, total_size)
        display_stats(status_stats, total_size)
    except KeyboardInterrupt:
        display_stats(status_stats, total_size)
        raise
