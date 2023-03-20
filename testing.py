import subprocess
subprocess.run(["gcc", "-o", "testing", "--coverage", "testing.c"])
subprocess.run(["./testing"])
subprocess.run(["gcov", "testing.c", "-m"])