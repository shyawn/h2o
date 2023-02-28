import requests
import random
import string

def mutate_url(url: str, diff: int) -> str:
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

dir_list = ["index.html", "install.html", "configure.html", "faq.html", "random.html"]

PORT = 5000

headers = {}
h_header = ["accept", "accept-charset", "accept-encoding", "accept-language", "connection", "content-type"]
v_header = ["application/json", "utf-8", "gzip", "deflate", "en-us", "keep-alive", "text/html"]


# Without mutation on url
def fuzz() -> 'None':
    for _ in range(1000):
        for i in h_header:
            headers[i] = random.choice(v_header)
        url = f"http://localhost:{PORT}/{random.choice(dir_list)}"
        res = requests.get(url, headers=headers)
        print(res.status_code)


# With mutation on url
def mutated_fuzz():
    mutated_num = [int(i) for i in range(10)]
    for _ in range(1000):
        for i in h_header:
            headers[i] = random.choice(v_header)
        url = f"http://localhost:{PORT}/{random.choice(dir_list)}"
        url = mutate_url(url, mutated_num)
        res = requests.get(url, headers=headers)
        print(res.status_code)
    pass



# A GET request to the API
# response = requests.get(url, headers=headers)
# print(response.headers)
# fuzz()
url = f"http://localhost:{PORT}/"
print(mutate_url(url, 3))