import csv

with open('top-1m.csv') as csv_file:
    with open('output_brute.txt', 'w') as f:
        f.write('{')
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                f.write(f'"{row[1]}",')
                # print(f'\t{row[0]} works in the {row[1]}')
                line_count += 1
        f.write('};')
    print(f'Processed {line_count} lines.')


