H2O - an optimized HTTP server with support for HTTP/1.x, HTTP/2 and HTTP/3 (experimental)
===

To run the Fuzzer X, run "python combined_testing.py {seconds} {runs}" in the command line, where seconds = amount of time the code should run in seconds, and runs = number of iterations the code should run for.
ex) python combined_testing.py 3600 3 (run the test 3600sec 3 times)

As a result of the each test "time vs coverage", "time vs number of inputs" garph and csv files will be generated

As a final result of the each test "time vs coverage", "time vs number", "tests vs coverage" graphs and csv files will be generated

For testing baseline, use "python combined_baseline_fuzzing.py {seconds} {runs}"

If "python" does not work, use the "python3" argument instead.
Plotext is required to run the test. Use "pip install plotext" to download the library.


