import subprocess
import sys
import time
# use "pip install plotext" before running
from mutate import *
from mutation_probability import *
from generate_input import *
import plotext as plt
import os
from collections import deque
ENERGY = 50

if len(sys.argv) < 2:
    print("Please provide 1 argument (number of fuzz)")
    sys.exit()
elif len(sys.argv) > 2:
    print("Too much argument is provided")
    sys.exit()

if not str(sys.argv[1]).isnumeric():
    print("Argument must be an integer")
    sys.exit()

# Initialization of global variables
coverage_dict = {}
# overall_coverage_dict = {}
plot_duration = []
number_of_interesting_input = []
number_of_inpute_generated = []
number_of_iteration = 0


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

# Set number of iterations from cmd line
time_for_fuzz = float(sys.argv[1])

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
        for line in file.readlines():
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
                    key += coverage + ","
                else:
                    key += "#" + ","

        p_scheme = p_map["scheme"]
        p_host = p_map["host"]
        p_port = p_map["port"]
        p_path= p_map["path"]
        print(key)
        # Add unique keys to coverage_dict
        if key not in coverage_dict:
            coverage_dict[key] = 0
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
def time_checker():
    return (time.time() - start_time) > time_for_fuzz

def show_results():
    end_time = time.time()
    total_duration = end_time - start_time
    print("Total time taken: ", total_duration)

    #show total seed
    print(total_seed)
    # Plotting total number of inputs vs time
    plt.plot(plot_duration, number_of_inpute_generated)
    plt.xlabel('time')
    plt.ylabel('number of inputs')
    plt.show()

    plt.clear_data()

    plt.plot(plot_duration, number_of_interesting_input)
    plt.xlabel('time')
    plt.ylabel('number of coverage')
    plt.show()
# Main running code
start_time = time.time()
try:
    #infinite loop (loops break when time.time() - start_time > time_for_fuzz)
    while(1):
        print("\nIteration: ", number_of_iteration)

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
                subprocess.run(["gcc", "-o", "test", "--coverage", "test.c"])
                mutate_res = mutate(p_scheme, p_host, p_port, p_path, scheme, host, port, path)
                new_url = mutate_res[0] + mutate_res[1] + mutate_res[2] + mutate_res[3]
                location = mutate_res[4]
                url_len = len(mutate_res[0] + mutate_res[1] + mutate_res[2])
                print(url_len)
                print("compiled")
                #new_url is mutated url, url_len is length of scheme, host, port
                subprocess.run(["./test", f"{new_url}", f"{url_len}"]) 
                print("runned")

                subprocess.run(["gcov", "test.c", "-m"])
                print("runned")
                print (new_url)
                print (location)
                read_gcov(mutate_res[0], mutate_res[1], mutate_res[2], mutate_res[3], location)
                print (p_map["scheme"], p_map["host"], p_map["port"], p_map["path"])
                # Calculate time taken for each iteration
                point_duration = time.time() - start_time
                plot_duration.append(point_duration)

                number_of_inpute_generated.append(number_of_iteration)
                number_of_interesting_input.append(len(total_seed))
                print ("number of interesting input : " + str(len(total_seed)))
                print(time.time() - start_time)
                if (time_checker()):
                    break

        else:
            for i in range(100):
                seed.append((new_scheme(), new_host(), new_port(), new_path(), ENERGY))
                if (time.time() - start_time > time_for_fuzz):
                    break
        if (time_checker()):
            break

    show_results()
except KeyboardInterrupt:
    show_results()
    