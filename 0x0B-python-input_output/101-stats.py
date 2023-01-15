#!/usr/bin/python3
import sys

total_size = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

try:
    for i, line in enumerate(sys.stdin, start=1):
        parts = line.strip().split()
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        total_size += file_size
        status_counts[status_code] += 1

        if i % 10 == 0:
            print("File size:", total_size)
            for status_code in sorted(status_counts.keys()):
                if status_counts[status_code] > 0:
                    print(f"{status_code}: {status_counts[status_code]}")

except KeyboardInterrupt:
    print("File size:", total_size)
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")
