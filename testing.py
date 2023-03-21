import subprocess
import sys
import time

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

start_time = time.time()
for _ in range(number_of_fuzz):
    print(_)
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

    with open ('testing.txt', 'r') as file:
        key = ""
        for line in file.readlines():
                coverage_list = line.split(':')
                coverage = coverage_list[0].strip()
                line_number = coverage_list[1].strip()
                if int(line_number):
                    if coverage.isnumeric():
                        key += coverage + ","
                    else:
                        key += "#" + ","

        if key not in coverage_dict:
            coverage_dict[key] = 0

        file1.close()
        print("Key length", len(key))
        print("Coverage: ", coverage_dict)
        print("Number of interesting inputs: ", len(coverage_dict))

end_time = time.time()
duration = end_time - start_time
print("Total time taken: ", duration)