import subprocess
import sys
import time
import csv
# use "pip install plotext" before running

import plotext as plt
import os
from collections import deque

number_of_tests_min = 0

def initial_read_csv():
    # open the file in the write mode
    # open the file in the write mode
    path = os.getcwd()
    with open(path + "/data_per_time" + str(0) + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0):
                time_per_time_index.append(float(row[0]))
                coverage_per_time.append(int(row[1]))
                bugs_per_time.append(int(row[2]))
            line_count += 1

    with open(path + "/data_per_test" + str(0) + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0):
                number_of_tests.append(int(row[0]))
                coverage_per_test.append(int(row[1]))
                bugs_per_test.append(int(row[2]))
            line_count += 1
        # -1 because of first line
        number_of_tests_min = line_count- 1
    return number_of_tests_min 

def read_csv(i, number_of_tests_min):
    # open the file in the write mode
    # open the file in the write mode
    number_of_tests_min_return = 0
    path = os.getcwd()
    with open(path + "/data_per_time" + str(i) + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0):
                coverage_per_time[line_count-1] = int(row[1]) + int(coverage_per_time[line_count-1])
                bugs_per_time[line_count-1] = int(row[2]) + int(bugs_per_time[line_count-1])

            line_count += 1

    with open(path + "/data_per_test" + str(i) + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0 and number_of_tests_min > line_count):
                coverage_per_test[line_count-1] = int(row[1]) + int(coverage_per_test[line_count-1])
                bugs_per_test[line_count-1] = int(row[2]) + int(bugs_per_test[line_count-1])

            line_count += 1
        # -1 because of first line
        if(number_of_tests_min > line_count - 1):
            number_of_tests_min_return = line_count - 1
        else:
            number_of_tests_min_return = number_of_tests_min
        return number_of_tests_min_return
    
def normalize(number_of_tests_min):
    for i in range(len(coverage_per_time)):
        coverage_per_time[i] = round(float(coverage_per_time[i]) / number_of_fuzzing)

    for i in range(len(coverage_per_test)):
        if (number_of_tests_min > i):
            print(coverage_per_test)
            coverage_per_test[i] = round(float(coverage_per_test[i]) / number_of_fuzzing)
        else:
            coverage_per_test.pop(i)


def show_results():
    print(coverage_per_time)

    plt.plot(time_per_time_index, coverage_per_time)
    plt.xlabel('time')
    plt.ylabel('number of inputs')
    plt.show()

    plt.clear_data()

    plt.plot(number_of_tests, coverage_per_test)
    plt.xlabel('tests')
    plt.ylabel('number of coverage')
    plt.show()

ENERGY = 50
number_of_fuzzing = 3
BUG_COMMAND = "test.gcda:stamp mismatch with notes file"

plot_duration = []
coverage_per_test = []
number_of_tests = []
bugs_per_test = []
time_per_time_index = []
coverage_per_time = []
bugs_per_time = []


if len(sys.argv) < 2:
    print("Please provide 1 argument (time for fuzz)")
    sys.exit()
elif len(sys.argv) > 2:
    print("Too much argument is provided")
    sys.exit()

if not str(sys.argv[1]).isnumeric():
    print("Argument must be an integer")
    sys.exit()
time_for_fuzz = sys.argv[1]
for i in range(number_of_fuzzing):
    subprocess.run(["python3", "testing.py", str(time_for_fuzz), str(i)])

# append values from 0th fuzz
number_of_tests_min = initial_read_csv()
# add values from 1~nth fuzz
for i in range(1, number_of_fuzzing):
    number_of_tests_min = read_csv(i, number_of_tests_min)
#normalize
normalize(number_of_tests_min)

show_results()
