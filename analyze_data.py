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
    with open(path + "/data_per_time" + str(0) + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0):
                time_per_time_index.append(float(row[0]))
                coverage_per_time.append(int(row[1]))
                bugs_per_time.append(int(row[2]))
                tests_per_time.append(int(row[3]))
            line_count += 1
            
    with open(path + "/data_per_test" + str(0) + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0):
                number_of_tests.append(int(row[0]))
                total_coverage_per_test.append(int(row[1]))
                bugs_per_test.append(int(row[2]))
            line_count += 1
        number_of_tests_min = line_count- 1
    return number_of_tests_min 

def read_csv(i, number_of_tests_min):
    number_of_tests_min_return = 0
    path = os.getcwd()
    with open(path + "/data_per_time" + str(i) + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0):

                coverage_per_time[line_count-1] += int(row[1]) 
                bugs_per_time[line_count-1] = int(row[2]) + int(bugs_per_time[line_count-1])
                tests_per_time[line_count -1] += int(row[3])
            line_count += 1

    with open(path + "/data_per_test" + str(i) + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0 and number_of_tests_min > line_count -1):
                total_coverage_per_test[line_count-1] = int(row[1]) + int(total_coverage_per_test[line_count-1])
                bugs_per_test[line_count-1] = int(row[2]) + int(bugs_per_test[line_count-1])

            line_count += 1
        if(number_of_tests_min > line_count - 1):
            number_of_tests_min_return = line_count - 1
        else:
            number_of_tests_min_return = number_of_tests_min
        return number_of_tests_min_return
    
def initial_baseline_read_csv():
    path = os.getcwd()
    with open(path + "/baseline_data_per_time" + str(0) + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0):
                baseline_time_per_time_index.append(float(row[0]))
                baseline_coverage_per_time.append(int(row[1]))
                baseline_bugs_per_time.append(int(row[2]))
                baseline_tests_per_time.append(int(row[3]))

            line_count += 1
            
    with open(path + "/baseline_data_per_test" + str(0) + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0):
                baseline_number_of_tests.append(int(row[0]))
                baseline_total_coverage_per_test.append(int(row[1]))
                baseline_bugs_per_test.append(int(row[2]))
            line_count += 1
        number_of_tests_min = line_count- 1
    return number_of_tests_min 


def baseline_read_csv(i, number_of_tests_min):
    number_of_tests_min_return = 0
    path = os.getcwd()
    with open(path + "/baseline_data_per_time" + str(i) + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0):

                baseline_coverage_per_time[line_count-1] += int(row[1]) 
                baseline_bugs_per_time[line_count-1] = int(row[2]) + int(bugs_per_time[line_count-1])
                baseline_tests_per_time[line_count -1] += int(row[3])
            line_count += 1

    with open(path + "/baseline_data_per_test" + str(i) + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0 and number_of_tests_min > line_count -1):
                baseline_total_coverage_per_test[line_count-1] = int(row[1]) + int(total_coverage_per_test[line_count-1])
                baseline_bugs_per_test[line_count-1] = int(row[2]) + int(bugs_per_test[line_count-1])

            line_count += 1
        if(number_of_tests_min > line_count - 1):
            number_of_tests_min_return = line_count - 1
        else:
            number_of_tests_min_return = number_of_tests_min
        return number_of_tests_min_return

    
def normalize(number_of_tests_min):
    for i in range(len(coverage_per_time)):
        coverage_per_time[i] = round(float(coverage_per_time[i]) / number_of_fuzzing)
        
    for i in range(number_of_tests_min):
        average_coverage_per_test.append(round(float(total_coverage_per_test[i]) / number_of_fuzzing))

    for i in range(len(baseline_coverage_per_time)):
        baseline_coverage_per_time[i] = round(float(baseline_coverage_per_time[i]) / number_of_fuzzing)
        
    for i in range(number_of_tests_min):
        baseline_average_coverage_per_test.append(round(float(baseline_total_coverage_per_test[i]) / number_of_fuzzing))


def show_results():

    plt.plot(time_per_time_index, coverage_per_time)
    plt.xlabel('time')
    plt.ylabel('coverage')
    plt.show()
    
    plt.clear_data()
    
    plt.plot(time_per_time_index, tests_per_time)
    plt.xlabel('time')
    plt.ylabel('tests')
    plt.show()
    
    plt.clear_data()

    plt.plot(number_of_tests, average_coverage_per_test)
    plt.xlabel('tests')
    plt.ylabel('coverage')
    plt.show()

    plt.clear_data()

    plt.plot(number_of_tests, average_coverage_per_test)
    plt.plot(number_of_tests, baseline_average_coverage_per_test)
    plt.xlabel('tests')
    plt.ylabel('coverage')
    plt.show()
    
def write_csv():
    path = os.getcwd()
    with open(path + "/final_result_data_per_time.csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["time", "coverage", "bug"])
        for i in range(len(time_per_time_index)):
            writer.writerow([time_per_time_index[i], coverage_per_time[i], tests_per_time[i]])
            
    with open(path + "/final_result_data_per_tests.csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["test", "coverage", "bug"])
        for i in range((number_of_tests_min)):
            writer.writerow([number_of_tests[i], average_coverage_per_test[i]])
    return

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
number_of_tests_min_baseline = initial_baseline_read_csv()
# add values from 1~nth fuzz
for i in range(1, number_of_fuzzing):
    number_of_tests_min = read_csv(i, number_of_tests_min)
    number_of_tests_min_baseline = baseline_read_csv(i, number_of_tests_min_baseline)
if (number_of_tests_min_baseline > number_of_tests_min):
    number_of_tests_min_final = number_of_tests_min
else:
    number_of_tests_min_final = number_of_tests_min_baseline
#normalize
normalize(number_of_tests_min_final)
#prtint redsuly
show_results()
write_csv()
