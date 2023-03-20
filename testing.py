import subprocess 
subprocess.call(["g++", "testcode.c"]) 
subprocess.run(["gcc", "-o", "testing", "--coverage", "testing.c"])
# subprocess.run(["./testing"])
subprocess.run(["gcov", "testing.c", "-m"])
subprocess.run(["cat", "testing.c.gcov"])