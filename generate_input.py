import random

def new_scheme ():
    scheme = ""
    choose_scheme = random.randint (0, 2)
    if choose_scheme == 0:
        scheme = "http://"
    elif choose_scheme == 1:
        scheme = "https://"
    else:
        scheme = "masque://"
    return scheme

def new_host ():
    host = ""
    toggle = random.randint (0, 1)
    if toggle == 0:
        host_idx = random.randint (0, 99999)
        host = host_list [host_idx]
    else:
        host_len = random. randint (5, 20)
        after_dot_len = random.randint (2, 3)
        for i in range (host_len - (after_dot_len + 1)):
            host[i] = get_random_character_host ()
        host[host_len - (after_dot_len + 1)] = "."
        for j in range (host_len - after_dot_len, host_len):
            host[j] = get_random_small_alphabet ()
    return host

def new_port ():
    int_port = random.randint (1, 65535)
    str_port = ":" + str(int_port)
    return str_port

def new_path ():
    path = ""
    path_len = random.randint(2, 30)
    path[0] = "/"
    for i in range (1, path_len):
        path[i] = get_random_character_path ()
    return path

def get_random_character_host ():
    toggle = random.randint (0, 1)
    if toggle == 0:
        asciicode = random.randint (45, 57)
        while asciicode == 47:
            asciicode = random.randint (45, 57)
    else:
        asciicode = random.randint (97, 122)
    return chr(asciicode)

def get_random_small_alphabet ():
    asciicode = random.randint (97, 122)
    return chr (asciicode)

def get_random_character_path ():
    asciicode = random.randint (33, 126)
    while asciicode == 34 or asciicode == 42 or asciicode == 47 or asciicode == 58 or asciicode == 60 or asciicode == 62 or asciicode == 63 or asciicode == 92 or asciicode == 124:
        asciicode = random.randint (33, 126)
    return chr (asciicode)