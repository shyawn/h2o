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


number_of_fuzz = int(sys.argv[1])

coverage_dict = {}
inputs = []
duration = []
plot_coverage = []

start_time = time.time()
for _ in range(number_of_fuzz):
    print("Iteration: ", _)
    subprocess.run(["gcc", "-o", "testing", "--coverage", "testing.c"])
    subprocess.run(["./testing"])
    subprocess.run(["gcov", "testing.c", "-m"])

    # subprocess.run(["cat", "testing.c.gcov"])

    ### using lcov to generate html report
    # subprocess.run(["lcov", "--capture", "--directory", ".", "--output-file", "testing.info"])
    # # subprocess.run(["geninfo", ".", "-o", "./testing.info"])
    # subprocess.run(["genhtml", "testing.info", "--output-directory", "out"])
    # subprocess.run(["google-chrome", "out/index.html"]) # not working??

    # subprocess.run(["gcovr", "-v", "-gk", "--html", "--html-details", "-o", "coverage.html", "-s"])

    with open('testing.txt', 'w') as file1:
        with open ('testing.c.gcov', 'r') as file2:
            line = file2.read()
            file1.write(line)
    file2.close()
    file1.close()

    with open ('testing.txt', 'r') as file:
        key = ""
        coverage_cnt = 0
        for line in file.readlines():
                coverage_list = line.split(':')
                coverage = coverage_list[0].strip()
                line_number = coverage_list[1].strip()
                if int(line_number):
                    if coverage.isnumeric():
                        coverage_cnt += int(coverage)
                        key += coverage + ","
                    else:
                        key += "#" + ","

        if key not in coverage_dict:
            coverage_dict[key] = 0

    file2.close()

    point_duration = time.time() - start_time
    duration.append(point_duration)
    if len(plot_coverage) != 0:
        plot_coverage.append(coverage_cnt + plot_coverage[-1])
    else:
        plot_coverage.append(coverage_cnt)

    print("Coverage count: ", plot_coverage)
    print("Duration: ", duration)
    print("Key length", len(key))
    print("Coverage: ", coverage_dict)
    print("Number of interesting inputs: ", len(coverage_dict))

end_time = time.time()
total_duration = end_time - start_time
print("Total time taken: ", total_duration)

plt.plot(duration, plot_coverage)
plt.xlabel('time')
plt.ylabel('coverage')
plt.show()