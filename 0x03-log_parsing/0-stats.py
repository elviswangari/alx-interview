#!/usr/bin/python3
'''
read line from stdin process data
and return the sizez of codes
'''
import sys


def process_log_data():
    '''
    process data
    '''
    status_codes = {
            '200': 0, '300': 0, '400': 0, '401': 0,
            '403': 0, '404': 0, '405': 0, '500': 0
            }
    total_size = 0
    count = 0

    try:
        for line in sys.stdin:
            # split line
            list_line = line.split()

            # check num of elements
            if len(list_line) > 4:
                status_code = list_line[-2]
                file_size = int(list_line[-1])

                # update the status code if exists
                if status_code in status_codes:
                    status_codes[status_code] += 1

                total_size += file_size
                count += 1

            if count == 10:
                print_summary(total_size, status_codes)
                count = 0
                total_size = 0
                status_codes = {
                        '200': 0, '300': 0, '400': 0, '401': 0,
                        '403': 0, '404': 0, '405': 0, '500': 0
                        }

    except KeyboardInterrupt:
        pass

    finally:
        print_summary(total_size, status_codes)


def print_summary(total_size, status_codes):
    '''prints the output'''
    print('File size:', total_size)

    for key, value in sorted(status_codes.items()):
        if value != 0:
            print(f'{key}: {value}')


if __name__ == '__main__':
    process_log_data()
