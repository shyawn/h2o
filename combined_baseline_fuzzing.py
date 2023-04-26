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
    global Runtime_of_target_func, Time_for_generate_input
    path = os.getcwd()
    with open(path + "/baseline_data_per_time" + str(0) + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0):
                time_per_time_index.append(float(row[0]))
                coverage_per_time.append(int(row[1]))
                bugs_per_time.append(int(row[2]))
                tests_per_time.append(int(row[3]))

            line_count += 1
            
    with open(path + "/baseline_data_per_test" + str(0) + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0):
                number_of_tests.append(int(row[0]))
                total_coverage_per_test.append(int(row[1]))
                bugs_per_test.append(int(row[2]))
            line_count += 1
        # -1 because of first line
        number_of_tests_min = line_count- 1
        
    with open(path + "/baseline_timeinfo" + str(0) + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0):
                Runtime_of_target_func += float(row[0])
                Time_for_generate_input += float(row[1])
            line_count += 1
    return number_of_tests_min 

def read_csv(i, number_of_tests_min):
    # open the file in the write mode
    global Runtime_of_target_func, Time_for_generate_input
    number_of_tests_min_return = 0
    path = os.getcwd()
    with open(path + "/baseline_data_per_time" + str(i) + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0):

                coverage_per_time[line_count-1] += int(row[1]) 
                bugs_per_time[line_count-1] = int(row[2]) + int(bugs_per_time[line_count-1])
                tests_per_time[line_count -1] += int(row[3])
            line_count += 1

    with open(path + "/baseline_data_per_test" + str(i) + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0 and number_of_tests_min > line_count -1):
                total_coverage_per_test[line_count-1] = int(row[1]) + int(total_coverage_per_test[line_count-1])
                bugs_per_test[line_count-1] = int(row[2]) + int(bugs_per_test[line_count-1])

            line_count += 1
        # -1 because of first line
        if(number_of_tests_min > line_count - 1):
            number_of_tests_min_return = line_count - 1
        else:
            number_of_tests_min_return = number_of_tests_min
            
    with open(path + "/baseline_timeinfo" + str(i) + ".csv", 'r') as f:
        reader = csv.reader(f)
        line_count = 0
        for row in reader:
            if (line_count != 0):
                Runtime_of_target_func += float(row[0])
                Time_for_generate_input += float(row[1])
            line_count += 1
            
    return number_of_tests_min_return
    
def normalize(number_of_tests_min):
    
    global Runtime_of_target_func, Time_for_generate_input, average_Runtime_of_target_func, average_Time_for_generate_input
    for i in range(len(coverage_per_time)):
        coverage_per_time[i] = round(float(coverage_per_time[i]) / number_of_fuzzing)
    for i in range(len(coverage_per_time)):
        tests_per_time[i] = round(float(tests_per_time[i]) / number_of_fuzzing)
    for i in range(number_of_tests_min):
        average_coverage_per_test.append(round(float(total_coverage_per_test[i]) / number_of_fuzzing))
        
    average_Runtime_of_target_func = Runtime_of_target_func / number_of_fuzzing
    average_Time_for_generate_input = Time_for_generate_input / number_of_fuzzing


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
    
def write_csv():
    # open the file in the write mode
    # open the file in the write mode
    path = os.getcwd()
    with open(path + "/baseline_final_result_data_per_time.csv", 'w') as f:
    # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        #firstly write down datas per time
        writer.writerow(["time", "coverage", "bug"])
        for i in range(len(time_per_time_index)):
            writer.writerow([time_per_time_index[i], coverage_per_time[i], tests_per_time[i]])
    with open(path + "/baseline_final_result_data_per_tests.csv", 'w') as f:
    # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        #firstly write down datas per time
        writer.writerow(["test", "coverage", "bug"])
        for i in range((number_of_tests_min)):
            writer.writerow([number_of_tests[i], average_coverage_per_test[i]])
    with open(path + "/baseline_final_timeinfo" + ".csv", 'w') as f:
    # create the csv writer
        writer = csv.writer(f)
        # write a row to the csv file
        #firstly write down datas per time
        writer.writerow(["average time taken for running tests", "average time taken for generate inputs"])
        writer.writerow([average_Runtime_of_target_func, average_Time_for_generate_input])

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

Runtime_of_target_func = 0
average_Runtime_of_target_func = 0
Time_for_generate_input = 0
average_Time_for_generate_input = 0

if len(sys.argv) < 3:
    print("Please provide 2 argument (time for fuzz, how many time to fuzz)")
    sys.exit()
elif len(sys.argv) > 3:
    print("Too much argument is provided")
    sys.exit()

if not str(sys.argv[1]).isnumeric():
    print("Argument must be an integer")
    sys.exit()
time_for_fuzz = sys.argv[1]
number_of_fuzzing = int(sys.argv[2])
for i in range(number_of_fuzzing):
    subprocess.run(["python3", "testing_baseline.py", str(time_for_fuzz), str(i)])

# append values from 0th fuzz
number_of_tests_min = initial_read_csv()
# add values from 1~nth fuzz
for i in range(1, number_of_fuzzing):
    number_of_tests_min = read_csv(i, number_of_tests_min)

#normalize
normalize(number_of_tests_min)
show_results()
write_csv()
