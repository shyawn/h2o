import requests
import random
import string
import sys

from collections import defaultdict


PORT = 5000
headers = {}
dir_list = ["index.html", "install.html", "configure.html", "faq.html", "random.html"]
h_header = ["accept", "accept-charset", "accept-encoding", "accept-language", "connection", "content-type"]
v_header = ["application/json", "utf-8", "gzip", "deflate", "en-us", "keep-alive", "text/html"]


def mutate_str(url: str, diff: int) -> str:
    diff = min(diff, len(url))
    random_char = [""] * diff
    idx = [int(i) for i in range(len(url))]
    sample = random.sample(idx, diff)

    l_url = list(url)

    for i in range(diff):
        random_char[i] = random.choice(string.ascii_letters)

    for i in range(diff):
        l_url[sample[i]] = random_char[i]
    return "".join(l_url)


# Without mutation on dir
def fuzz() -> 'None':
    data = defaultdict(int)
    for _ in range(1000):
        for i in h_header:
            headers[i] = random.choice(v_header)
        url = f"http://localhost:{PORT}/{random.choice(dir_list)}"
        res = requests.get(url, headers=headers)
        data[res.status_code] += 1
        print(res.status_code)
    print("Summary of fuzz:")
    print(data)


# With mutation on dir
def mutated_fuzz() -> 'None':
    data = defaultdict(int)
    mutated_num = [int(i) for i in range(10)]
    for _ in range(1000):
        for i in h_header:
            headers[i] = random.choice(v_header)
        dir = random.choice(dir_list)
        m_dir = mutate_str(dir, random.choice(mutated_num))
        url = f"http://localhost:{PORT}/{m_dir}"
        try:
            res = requests.get(url, headers=headers)
            data[res.status_code] += 1
            print(res.status_code)
        except Exception:
            pass
    print("Summary of mutated fuzz:")
    print(data)


arg_list = list(sys.argv)
for i in arg_list[1:]:
    if i == "1":
        fuzz()
    elif i == "2":
        mutated_fuzz()