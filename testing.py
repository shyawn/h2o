import subprocess
import sys
import time
# import matplotlib.pyplot as plt
# use "pip install plotext" before running
import plotext as plt

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
overall_coverage_dict = {}
plot_duration = []
number_of_interesting_input = []

# Set number of iterations from cmd line
number_of_fuzz = int(sys.argv[1])

start_time = time.time()
for _ in range(number_of_fuzz):
    print("\nIteration: ", _)
    subprocess.run(["gcc", "-o", "testing", "--coverage", "testing.c"])
    subprocess.run(["./testing"])
    subprocess.run(["gcov", "testing.c", "-m"])

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
                if not (int(line_number) in overall_coverage_dict):
                    overall_coverage_dict[int(line_number)] = 0
                # Check if coverage is not ##### or -
                if coverage.isnumeric():
                    # Generate key for each iteration
                    key += coverage + ","
                    # Add coverage for each line from previous coverage
                    if (int(line_number) in overall_coverage_dict):
                        overall_coverage_dict[int(line_number)] += int(coverage)
                else:
                    key += "#" + ","
        # Add unique keys to coverage_dict
        if key not in coverage_dict:
            coverage_dict[key] = 0

    file.close()

    # Calculate time taken for each iteration
    point_duration = time.time() - start_time
    plot_duration.append(point_duration)

    number_of_interesting_input.append(len(coverage_dict))

    # Printing outputs
    # print("Number of inputs generated: ", number_of_input_generated)
    # print("Coverage count: ", plot_coverage)
    print("Duration: ", plot_duration)
    print("Coverage key length: ", len(key))
    print("Coverage: ", coverage_dict)
    print("Number of interesting inputs: ", len(coverage_dict))

end_time = time.time()
total_duration = end_time - start_time
print("Total time taken: ", total_duration)
print("Overall coverage: ", overall_coverage_dict)

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