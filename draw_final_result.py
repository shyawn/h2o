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
    path = os.getcwd()
    with open(path + "/final_result_data_per_tests" + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0):
                number_of_tests.append(float(row[0]))
                total_coverage_per_test.append(int(row[1]))
            line_count += 1
    number_of_tests_min = line_count- 1
            
    with open(path + "/baseline_final_result_data_per_tests" + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0):
                baseline_number_of_tests.append(int(row[0]))
                baseline_total_coverage_per_test.append(int(row[1]))
            line_count += 1
        # -1 because of first line
    if (line_count < number_of_tests_min):
        number_of_tests_min = line_count -1
        
    with open(path + "/final_result_data_per_time" + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0):
                time_per_time_index.append(float(row[0]))
                coverage_per_time.append(int(row[1]))
            line_count += 1
            
    with open(path + "/baseline_final_result_data_per_time" + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0):
                time_per_time_index.append(float(row[0]))
                baseline_coverage_per_time.append(int(row[1]))
            line_count += 1
        # -1 because of first line
    return number_of_tests_min 


def show_results():

    plt.ylim(0, 6000)
    plt.yfrequency(6)
    plt.plot(number_of_tests, total_coverage_per_test)
    plt.plot(number_of_tests, baseline_total_coverage_per_test)
    plt.xlabel('tests')
    plt.ylabel('coverage')
    plt.show()
    
    plt.clear_data()
    plt.ylim(0, 6000)
    plt.yfrequency(6)
    plt.plot(time_per_time_index, coverage_per_time)
    plt.plot(time_per_time_index, baseline_coverage_per_time)
    plt.xlabel('time')
    plt.ylabel('coverage')
    plt.show()
    
    plt.clear_data()
    plt.ylim(0, 6000)
    plt.yfrequency(6)
    plt.plot(time_per_time_index, coverage_per_time)
    plt.xlabel('time')
    plt.ylabel('coverage')
    plt.show()
    
    plt.clear_data()
    plt.ylim(0, 6000)
    plt.yfrequency(6)
    plt.plot(number_of_tests, total_coverage_per_test)
    plt.xlabel('tests')
    plt.ylabel('coverage')
    plt.show()

plot_duration = []
total_coverage_per_test = []
average_coverage_per_test = []
number_of_tests = []
bugs_per_test = []
time_per_time_index = []
coverage_per_time = []
bugs_per_time = []
tests_per_time = []

baseline_total_coverage_per_test = []
baseline_plot_duration = []
baseline_average_coverage_per_test = []
baseline_number_of_tests = []
baseline_bugs_per_test = []
baseline_time_per_time_index = []
baseline_coverage_per_time = []
baseline_bugs_per_time = []
baseline_tests_per_time = []


if len(sys.argv) < 2:
    print("Please provide 1 argument (number of fuzzing executed)")
    sys.exit()
elif len(sys.argv) > 2:
    print("Too much argument is provided")
    sys.exit()

if not str(sys.argv[1]).isnumeric():
    print("Argument must be an integer")
    sys.exit()
number_of_fuzzing = int(sys.argv[1])

number_of_tests_min_final = 0
# append values from 0th fuzz
number_of_tests_min = initial_read_csv()
#normalize
show_results()
