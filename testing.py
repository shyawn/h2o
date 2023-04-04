import subprocess
import sys
import time
# import matplotlib.pyplot as plt
# use "pip install plotext" before running
import plotext as plt
from collections import deque

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

# Initialization of Seed
seed = deque()

# Initialization of probability for scheme, host, port and path
# Note: 0 -> scheme, 1 -> host, 2 -> port, 3 -> path
p_map = {0: 25, 1: 25, 2: 25, 3: 25}

# Total seed
# Note: Some of the seed might not be executed because of either time constraint or exception
total_seed = set()

ENERGY = 50

# TODO: Complete the assign energy function
def assign_energy(url):
    return ENERGY

# Set number of iterations from cmd line
number_of_fuzz = int(sys.argv[1])

# Helper functions
def read_gcov(scheme, host, port, path):
    # global coverage_dict, overall_coverage_dict, seed
    global coverage_dict, seed
    with open('testing.txt', 'w') as file1:
        with open ('testing.c.gcov', 'r') as file2:
            line = file2.read()
            file1.write(line)
    file2.close()
    file1.close()

    with open ('testing.txt', 'r') as file:
        key = ""
        for line in file.readlines():
            coverage_list = line.split(':')
            # Get number of times line is run
            coverage = coverage_list[0].strip()
            # Get line number
            line_number = coverage_list[1].strip()
            # Exclude code from line 183 onwards
            if int(line_number) >= 183:
                break
            # Ignore line 0s
            if int(line_number):
                # Initialize line number & line coverage in overall_coverage_dict
                # if not (int(line_number) in overall_coverage_dict):
                    # overall_coverage_dict[int(line_number)] = 0
                # Check if coverage is not ##### or -
                if coverage.isnumeric():
                    # Generate key for each iteration
                    key += coverage + ","
                    # Add coverage for each line from previous coverage
                    # if (int(line_number) in overall_coverage_dict):
                        # overall_coverage_dict[int(line_number)] += int(coverage)
                else:
                    key += "#" + ","
        # Add unique keys to coverage_dict
        if key not in coverage_dict:
            coverage_dict[key] = 0
            # store in seed if output is interesting
            output_url = scheme + host + port + path
            energy = assign_energy(output_url)
            seed.append((scheme, host, port, path, energy))
            total_seed.add(output_url)

    file.close()


# Main running code
start_time = time.time()
for _ in range(number_of_fuzz):
    print("\nIteration: ", _)
    subprocess.run(["gcc", "-o", "testing", "--coverage", "testing.c"])
    # subprocess.run(["./testing"])

    # Getting output from testing.c
    if seed:
        data = seed.popleft()
        url = data[0]
        energy = data[1]
        # Run testing for n number of times, where n is the assigned energy
        for i in range(energy):
            subprocess.run(["./testing", f"{url}"]) # add arguments later
            scheme, host, port, path = None, None, None, None # read from random input generator

            subprocess.run(["gcov", "testing.c", "-m"])

            read_gcov(scheme, host, port, path)
        # deque.popleft() -> for url argument
    else:
        output_url = subprocess.check_output(["./testing"])
        output_url = output_url.decode("utf-8")

        subprocess.run(["gcov", "testing.c", "-m"])

        read_gcov(output_url)

    # # Calculate time taken for each iteration
    # point_duration = time.time() - start_time
    # plot_duration.append(point_duration)

    # number_of_interesting_input.append(len(coverage_dict))

    # # Printing outputs
    # # print("Number of inputs generated: ", number_of_input_generated)
    # # print("Coverage count: ", plot_coverage)
    # print("Duration: ", plot_duration)
    # print("Coverage key length: ", len(key))
    # print("Coverage: ", coverage_dict)
    # print("Number of interesting inputs: ", len(coverage_dict))

end_time = time.time()
total_duration = end_time - start_time
print("Total time taken: ", total_duration)
# print("Overall coverage: ", overall_coverage_dict)

# Plotting number of interesting input vs total number of input
total_number_of_input = [i for i in range(1, number_of_fuzz+1)]
# plt.plot(total_number_of_input, number_of_interesting_input)
# plt.xlabel('total number of inputs')
# plt.ylabel('interesting inputs')
# plt.show()

# Plotting number of interesting inputs vs time
# plt.plot(plot_duration, number_of_interesting_input)
# plt.xlabel('time')
# plt.ylabel('number of interesting inputs')
# plt.show()

# Plotting total number of inputs vs time
plt.plot(plot_duration, total_number_of_input)
plt.xlabel('time')
plt.ylabel('number of inputs')
plt.show()