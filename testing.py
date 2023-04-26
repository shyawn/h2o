import subprocess
import sys
import time
import csv
import math
# use "pip install plotext" before running
from mutate import *
from mutation_probability import *
from generate_input import *
import plotext as plt
import os
from collections import deque

#Check argumetns
# first argument time, second argument nth fuzz
if len(sys.argv) < 3:
    print("Please provide 2 argument (time for the fuzz, order of the fuzz)")
    sys.exit()

elif len(sys.argv) > 3:
    print("Too much argument is provided")
    sys.exit()

if not str(sys.argv[1]).isnumeric():
    print("Argument must be an integer")
    sys.exit()

# Set number of iterations from cmd line
time_for_fuzz = float(sys.argv[1])
# Set number of iterations from cmd line
nth_fuzz = int(sys.argv[2])

# Initialization of global variables
coverage_condition_dict = {}
state_list = []
plot_duration = []
coverage_per_test = []
number_of_tests = []
tests_per_time = []
time_per_time_index = []
coverage_per_time = []
bugs_per_time = []
bugs_per_test = []
unique_bugs_per_time = []
unique_bugs_per_tests = []
Total_bugs = 0
bug_inputs = []
unique_bug_returncodes = []

number_of_iteration = 0
num_iteration_assign_energy = 0
time_index = 0
time_interval = 0.0
number_of_coverage = 0

end_time = time.time() 
Time_for_running_Test = 0
# Initialization of Seed
seed = []

seed_index = 0
seed_length = 0

Test_Interval = 40
BUG_COMMAND = "returncode=0"

# Initialization of probability for location x operator
p_map = {}
key_list = ["pbbt_scheme0","pbbt_scheme1","pbbt_scheme2","pbbt_scheme3","pbbt_scheme4","pbbt_scheme5",
"pbbt_scheme6","pbbt_host0","pbbt_host1","pbbt_host2","pbbt_host3","pbbt_host4","pbbt_host5","pbbt_port0","pbbt_port1","pbbt_port2","pbbt_port3","pbbt_port4","pbbt_port5","pbbt_path0",
"pbbt_path1","pbbt_path2","pbbt_path3","pbbt_path4", "pbbt_path5"]

for i,j in enumerate(key_list):
    p_map[j] = 4

#function for read gcov
def read_gcov(scheme, host, port, path, location):
    # global coverage_dict, overall_coverage_dict, seed
    global coverage_condition_dict, seed, p_map

    with open ('testing.c.gcov', 'r') as file:
        key = ""
        state_key = ""
        line_count = 0
        is_interesting = False
        #our target function starts from line 38, so ignore the lines before line 38
        for line in file.readlines():
            if (line_count < 38):
                line_count += 1
                continue
            
            interesintg_list = line.split(':')
            # Get number of times line is run
            coverage = interesintg_list[0].strip()
            # Get line number
            line_number = interesintg_list[1].strip()
            if int(line_number):
                # Check if coverage is not ##### or -
                if coverage.isnumeric():
                    # Generate key for each iteration
                    key += str(coverage) +", "
                    state_key += "1, "
                # Check for * cases also
                elif coverage.find('*') != -1:
                    key += str(coverage) +", "
                    state_key += "1*, "
                else:
                    key += "#, "
                    state_key += "#, "
                line_count += 1


        state_index = 0
        Is_in_sates = False

        # Check if the found state is the new state
        for states in state_list:
            if state_key in states:
                Is_in_sates = True
                break
            state_index += 1
        if Is_in_sates == False:
            # If the state is new state, append to the state_list with s(i) = 0 and f(i) = 0
            # s(i) is number of times state chosen from the seed, f(i) is number of times this seed used for tests
            state_list.append([state_key, 0, 0])

            # store in seed if output is interesting
            print("length of state list : "+ str(len(state_list)))
            print("Seed numbers : " +  str(len(seed)) )

        # Check if the input is interesting or not
        if key not in coverage_condition_dict:
            coverage_condition_dict[key] = 0
            is_interesting = True

        # If interesting append to the seed
        if is_interesting == True:

            print("interesting")
            output_url = scheme + host + port + path
            seed.append([scheme, host, port, path, state_index])


        # Check if the input is mutated or not, if the location is "" the input is not mutated
        if location != "":
            # Update f(i)
            state_list[state_index][2] += 1
            # do updated prob when the mutated input is interesting
            if is_interesting == True:
                p_map = update_probability(p_map, location, 0)
            else:
                p_map = update_probability(p_map, location, 1)

    file.close()    

#function for assign energy
def assign_energy(state_index):
    result = 0
    print("state_index : " + str(state_index))
    print("Length State_List : " + str(len(state_list)))
    mean = num_iteration_assign_energy / len(state_list)
    print( "mean : " + str(mean)  + " f(i) : " + str(state_list[state_index][2]))

    for states in state_list:
        # Cehck and print every states which cannot exceed the mean
        if not (states[2] > mean):
            print("states lower than mean : " + str(state_list.index(states)))
    if state_list[state_index][2] > mean:
        return result
    
    else:
        result = pow(2, state_list[state_index][1])
        if (result > 15000000):
            result = 15000000
        state_list[state_index][1] += 1
    return result

# function for caculating entropy, not using for now
def entropy(map, new_map):
    '''
    args:
        map/new_map: dictionary containing values of all possibility
    return:
        boolean (if true meaning that the current input is making more variety)
    '''
    prev, new = 0, 0
    for i in map:
        prev += map[i] * math.log(map[i],2)
    for i in new_map:
        new += new_map[i] * math.log(new_map[i],2)
    return new < prev


# Set time constant using (time_for_fuzz/600)
# To prevent error, lower time frequency when time_for_fuzz is small
if (time_for_fuzz > 300):
    time_interval = time_for_fuzz/600
else:
    time_interval = time_for_fuzz/100

# Check for endtime
def end_time_checker():
    return (time.time() - start_time) > time_for_fuzz

# calculates time interval
def time_info_gathering(i):
    return (time.time() - start_time) > i * time_interval

# function for drawing graphs
def show_results():
    total_duration = end_time - start_time
    print("Total time taken: ", total_duration)

    #show total seed
    print(seed)
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
    path = os.getcwd()
    print (str(nth_fuzz) + "th fuzz")
    
    # create csv file contating data per time
    with open(path + "/data_per_time" + str(nth_fuzz) + ".csv", 'w') as f:
        writer = csv.writer(f)
        # firstly write down datas per time
        writer.writerow(["time", "coverage", "bug", "tests", "unique bugs"])
        for i in range(len(time_per_time_index)):
            writer.writerow([time_per_time_index[i], coverage_per_time[i], bugs_per_time[i], tests_per_time[i], unique_bugs_per_time[i]])
            
    # create csv file contating data per tests
    with open(path + "/data_per_test" + str(nth_fuzz) + ".csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["test", "coverage", "bug", "unique bugs"])
        for i in range((len(number_of_tests)//Test_Interval)):
            writer.writerow([number_of_tests[i * Test_Interval ], coverage_per_test[i * Test_Interval], bugs_per_test[i * Test_Interval], unique_bugs_per_tests[i * Test_Interval]])
            
    # write down found bugs   
    with open(path + "/bugs" + str(nth_fuzz) + ".csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["unique bugs"])
        for i in range(len(unique_bug_returncodes)):
            writer.writerow([unique_bug_returncodes[i]])
        writer.writerow(["bugs"])
        for i in range(len(bug_inputs)):
            writer.writerow([bug_inputs[i][0], bug_inputs[i][1]])
            
    # write down runtime and time for generating inputs
    with open(path + "/timeinfo" + str(nth_fuzz) + ".csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["average time taken for running tests", "average time taken for generate inputs"])
        writer.writerow([Time_for_running_Test / number_of_iteration, ( end_time - start_time - Time_for_running_Test)  / number_of_iteration])
    return



# Start to count time from this point
start_time = time.time() 
try:
    #infinite loop (loops break when time.time() - start_time > time_for_fuzz)
    while(1):
        
        # subprocess.run(["./testing"])
        # Getting output from testing.c
        if seed:
            while(seed_index < seed_length):
                data = seed[seed_index]

                scheme = data[0]
                host = data[1]
                port = data[2]
                path = data[3]
                state_num = data[4]
                # Assigning Energy before testing

                energy = assign_energy(state_num)
                
                # print input, assigned energy, and state
                print (scheme + host + port + path)
                print ("energy :" + str(energy))
                print (state_list[state_num])
                # Run testing for n number of times, where n is the assigned energy
                print("seed_index : " + str(seed_index))
                for i in range(energy):
                    number_of_iteration += 1
                    num_iteration_assign_energy += 1
                    print("\nIteration: ", number_of_iteration)
                    # compile run gcov the target function and read gcov result
                    
                    subprocess.run(["gcc", "-o", "testing", "--coverage", "testing.c"])
                    print("compiled")
                    mutate_res = mutate(p_map, scheme, host, port, path)
                    new_url = mutate_res[0] + mutate_res[1] + mutate_res[2] + mutate_res[3]
                    location = mutate_res[4]
                    url_len = len(mutate_res[0] + mutate_res[1] + mutate_res[2] + mutate_res[3])
                    
                    # input for target function and location 
                    print (url_len)
                    print (new_url)
                    print (location)
                    
                    #new_url is mutated url, url_len is length of scheme, host, port
                    output = ""
                    run_start_time = time.time()
                    #run the test
                    output = subprocess.run(["./testing", str(new_url), str(url_len)])
                    #calculating runtime for target function
                    run_end_time = time.time()
                    #count time for running the test
                    Time_for_running_Test += run_end_time - run_start_time
                    if (str(output).find(BUG_COMMAND) == -1):
                        Total_bugs += 1
                        x = str(output).split("returncode=")
                        retruncode = x[1][:-1]
                        print("bug returncode = " + str(retruncode))
                        print(type(retruncode))
                        if retruncode not in unique_bug_returncodes:
                            unique_bug_returncodes.append(retruncode)
                        bug_inputs.append([new_url, retruncode])
                        print("Bug Found")
                    if (end_time_checker()):
                        break
                    subprocess.run(["gcov", "testing.c", "-m"], capture_output=True)
                    read_gcov(mutate_res[0], mutate_res[1], mutate_res[2], mutate_res[3], location)

                    # Calculate time taken for each iteration
                    point_duration = time.time() - start_time
                    
                    #print probabilities
                    for i,j in p_map.items():
                        print("Key: " + str(i) + " Value : " +str(j))
                        
                    #print number of inputs
                    print ("number of interesting input : " + str(len(seed)))
                    
                    #print running time
                    print(time.time() - start_time)
                    
                    #check whether time end
                    if (end_time_checker()):
                        break
                    
                    #append data for ith time index
                    if (time_info_gathering(time_index)):
                        time_index += 1
                        time_per_time_index.append(time_index * time_interval)
                        coverage_per_time.append(len(seed))
                        bugs_per_time.append(Total_bugs)
                        tests_per_time.append(number_of_iteration)
                        unique_bugs_per_time.append(len(unique_bug_returncodes))
                        
                    # append datas per tests
                    plot_duration.append(point_duration)
                    number_of_tests.append(number_of_iteration)
                    coverage_per_test.append(len(seed))
                    bugs_per_test.append(Total_bugs)
                    unique_bugs_per_tests.append(len(unique_bug_returncodes))
                #update seed index and seedlength
                seed_index += 1
                seed_length = len(seed)
                
                #check whether time end
                if (end_time_checker()):
                    break
            seed_index = 0
            
        # fill in the seed only at the beginning
        else:
            for i in range(1200):
                number_of_iteration += 1
                print("\nMaking Seed Iteration: ", number_of_iteration)
                scheme = new_scheme()
                host = new_host()
                port = new_port()
                path = new_path()
                #mutate_res = mutate(25, 25, 25, 25, scheme, host, port, path)

                # compile run gcov the target function and read gcov result
                new_url = scheme + host + port + path
                url_len = len(new_url)
                subprocess.run(["gcc", "-o", "testing", "--coverage", "testing.c"])
                run_start_time = time.time()
                subprocess.run(["./testing", str(new_url), str(url_len)])
                run_end_time = time.time()
                Time_for_running_Test += run_end_time - run_start_time
                output = subprocess.run(["gcov", "testing.c", "-m"], capture_output=True)
                # read gcov
                read_gcov(scheme, host, port, path, "")
                
                # calculate runtime for target function
                point_duration = time.time() - start_time
                print ("number of interesting input : " + str(len(seed)))
                print(time.time() - start_time)
                if (end_time_checker()):
                    break
                # append datas per timeinterval
                if (time_info_gathering(time_index)):
                    time_index += 1
                    time_per_time_index.append(time_index * time_interval)
                    coverage_per_time.append(len(seed))
                    bugs_per_time.append(Total_bugs)
                    tests_per_time.append(number_of_iteration)
                    unique_bugs_per_time.append(len(unique_bug_returncodes))
                    
                # append datas per tests
                plot_duration.append(point_duration)
                number_of_tests.append(number_of_iteration)
                coverage_per_test.append(len(seed))
                bugs_per_test.append(Total_bugs)
                unique_bugs_per_tests.append(len(unique_bug_returncodes))

                if (end_time_checker()):
                    break
            seed_length = len(seed)
        if (end_time_checker()):
            break
        
# show results and write csv file when time limit ended
    end_time = time.time()
    show_results()
    write_csv()

# show results and write csv file when Ctrl+c pressed
except KeyboardInterrupt:
    end_time = time.time()
    show_results()
    write_csv()
