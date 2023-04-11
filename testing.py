import subprocess
import sys
import time
import csv
# use "pip install plotext" before running
from mutate import *
from mutation_probability import *
from generate_input import *
import plotext as plt
import os
from collections import deque

ENERGY = 50
Test_Index = 40
BUG_COMMAND = "test.gcda:stamp mismatch with notes file"
nth_fuzz = 0

if len(sys.argv) < 3:
    print("Please provide 2 argument (time for the fuzz, order of the fuzz)")
    sys.exit()

elif len(sys.argv) > 3:
    # Set number of iterations from cmd line
    print("Too much argument is provided")
    sys.exit()

if not str(sys.argv[1]).isnumeric():
    print("Argument must be an integer")
    sys.exit()

# Set number of iterations from cmd line
time_for_fuzz = float(sys.argv[1])
# Set number of iterations from cmd line
nth_fuzz = int(sys.argv[2])
print (nth_fuzz)

# Initialization of global variables
coverage_dict = []
# overall_coverage_dict = {}
plot_duration = []
coverage_per_test = []
number_of_tests = []
tests_per_time = []
time_per_time_index = []
coverage_per_time = []
bugs_per_time = []
bugs_per_test = []
Total_bugs = 0

number_of_iteration = 0
time_index = 0
time_for_generating_seeds = 0.0
time_interval = 0.0
number_of_coverage = 0

# Initialization of Seed
seed = deque()
for i in range(100):
    scheme = new_scheme()
    host = new_host()
    port = new_port()
    path = new_path()
    seed.append((scheme, host, port, path, ENERGY))


# Initialization of probability for scheme, host, port and path
# Note: 0 -> scheme, 1 -> host, 2 -> port, 3 -> path
p_map = {"scheme": 25, "host": 25, "port": 25, "path": 25}

# Total seed
# Note: Some of the seed might not be executed because of either time constraint or exception
total_seed = set()

# TODO: Complete the assign energy function
def assign_energy(url):
    return ENERGY


# Set time constant using (time_for_fuzz/600)
time_interval = time_for_fuzz/600

# Helper functions
def read_gcov(scheme, host, port, path, location):
    # global coverage_dict, overall_coverage_dict, seed
    global coverage_dict, seed
    with open('test.txt', 'w') as file1:
        with open ('test.c.gcov', 'r') as file2:
            line = file2.read()
            file1.write(line)
    file2.close()
    file1.close()

    with open ('test.txt', 'r') as file:
        key = ""
        line_count = 0
        is_interesting = False
        for line in file.readlines():
            if (line_count < 38):
                line_count += 1
                continue
            
            coverage_list = line.split(':')
            # Get number of times line is run
            coverage = coverage_list[0].strip()
            # Get line number
            line_number = coverage_list[1].strip()
            # Ignore line 0s
            if int(line_number):
                # Check if coverage is not ##### or -
                if coverage.isnumeric():
                    # Generate key for each iteration
                    key = coverage
                else:
                    key = "#"
            if key != "":
                if(len(coverage_dict) <= int(line_number)):
                    coverage_dict.append([key])
                    is_interesting = True
                elif key not in (coverage_dict[int(line_number)]):
                    is_interesting = True
                    coverage_dict[int(line_number)].append(key)
                line_count += 1

        p_scheme = p_map["scheme"]
        p_host = p_map["host"]
        p_port = p_map["port"]
        p_path= p_map["path"]
        print(coverage_dict)
        # do updated prob and assign energy when the mutated input is interesting
        if is_interesting == True:
            # store in seed if output is interesting
            new_prob = update_probability(p_scheme, p_host, p_port, p_path, location, 0)

            output_url = scheme + host + port + path
            energy = assign_energy(output_url)
            seed.append((scheme, host, port, path, energy))
            total_seed.add(output_url)
            print("interesting")
        else:
            new_prob = update_probability(p_scheme, p_host, p_port, p_path, location, 1)

        p_map["scheme"] = new_prob[0]
        p_map["host"] = new_prob[1]
        p_map["port"] = new_prob[2]
        p_map["path"] = new_prob[3]

    file.close()    
def end_time_checker():
    return (time.time() - start_time - time_for_generating_seeds) > time_for_fuzz

def time_info_gathering(i):
    return (time.time() - start_time - time_for_generating_seeds) > i * time_interval

def show_results():
    end_time = time.time()
    total_duration = end_time - start_time
    print("Total time taken: ", total_duration)

    #show total seed
    print(total_seed)
    # Plotting total number of inputs vs time
    plt.plot(plot_duration, number_of_tests)
    plt.xlabel('time')
    plt.ylabel('number of inputs')
    plt.show()

    plt.clear_data()

    plt.plot(plot_duration, coverage_per_test)
    plt.xlabel('time')
    plt.ylabel('number of coverage')
    plt.show()

def write_csv():
    # open the file in the write mode
    # open the file in the write mode
    path = os.getcwd()
    with open(path + "/data_per_time" + str(nth_fuzz) + ".csv", 'w') as f:
    # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        #firstly write down datas per time
        writer.writerow(["time", "coverage", "bug"])
        for i in range(len(time_per_time_index)):
            writer.writerow([time_per_time_index[i], coverage_per_time[i], bugs_per_time[i], tests_per_time[i]])
    with open(path + "/data_per_test" + str(nth_fuzz) + ".csv", 'w') as f:
    # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        #firstly write down datas per time
        writer.writerow(["test", "coverage", "bug"])
        for i in range((len(number_of_tests)//Test_Index)):
            writer.writerow([number_of_tests[i * Test_Index ], coverage_per_test[i * Test_Index], bugs_per_test[i * Test_Index]])
    return
# Main running code
start_time = time.time()
try:
    #infinite loop (loops break when time.time() - start_time > time_for_fuzz)
    while(1):


        # subprocess.run(["./testing"])

        # Getting output from testing.c
        if seed:
            data = seed.popleft()

            scheme = data[0]
            host = data[1]
            port = data[2]
            path = data[3]
            energy = data[4]

            p_scheme = p_map["scheme"]
            p_host = p_map["host"]
            p_port = p_map["port"]
            p_path= p_map["path"]
           
            
            # Run testing for n number of times, where n is the assigned energy
            for i in range(energy):
                number_of_iteration += 1
                print("\nIteration: ", number_of_iteration)
                subprocess.run(["gcc", "-o", "test", "--coverage", "test.c"])
                print("compiled")
                mutate_res = mutate(p_scheme, p_host, p_port, p_path, scheme, host, port, path)
                new_url = mutate_res[0] + mutate_res[1] + mutate_res[2] + mutate_res[3]
                location = mutate_res[4]
                url_len = len(mutate_res[0] + mutate_res[1] + mutate_res[2] + mutate_res[3])
                print(url_len)
                print (new_url)
                print (location)
                #new_url is mutated url, url_len is length of scheme, host, port
                
                subprocess.run(["./test", str(new_url), str(url_len)])
                
                if (end_time_checker()):
                    break
                output = ""
                output = subprocess.run(["gcov", "test.c", "-m"], capture_output=True)
                if (str(output).find(BUG_COMMAND) != -1):
                    Total_bugs += 1
                    print("Bug Found")
                print("runned")

                read_gcov(mutate_res[0], mutate_res[1], mutate_res[2], mutate_res[3], location)
                print (p_map["scheme"], p_map["host"], p_map["port"], p_map["path"])

                # Calculate time taken for each iteration
                point_duration = time.time() - start_time
                print ("number of interesting input : " + str(len(total_seed)))
                print(time.time() - start_time)
                if (end_time_checker()):
                    break
                if (time_info_gathering(time_index)):
                    time_index += 1
                    time_per_time_index.append(time_index * time_interval)
                    coverage_per_time.append(len(total_seed))
                    bugs_per_time.append(Total_bugs)
                    tests_per_time.append(number_of_iteration)
                #append everything after time_info_gathering
                plot_duration.append(point_duration)

                number_of_tests.append(number_of_iteration)
                coverage_per_test.append(len(total_seed))
                #will be implemented later
                bugs_per_test.append(Total_bugs)


        else:
            making_seed_start_time = time.time()
            for i in range(100):
                seed.append((new_scheme(), new_host(), new_port(), new_path(), ENERGY))
                if (end_time_checker()):
                    break
            making_seed_end_time = time.time()
            time_for_generating_seeds = making_seed_end_time - making_seed_start_time 
        if (end_time_checker()):
            break

    show_results()
    write_csv()
except KeyboardInterrupt:
    show_results()
    write_csv()
    