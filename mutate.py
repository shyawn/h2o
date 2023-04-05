import random

def choose_mutation_location (pbbt_scheme, pbbt_host, pbbt_port, pbbt_path, scheme, host, port, path):
	choose_mutation_location = random.uniform (0, 100)

	if choose_mutation_location < pbbt_scheme:
		print ("Mutation: scheme")
		scheme = mutate_scheme (scheme)
		print ("Mutated scheme: " + scheme)

	elif choose_mutation_location >= pbbt_scheme and choose_mutation_location < (pbbt_scheme + pbbt_host):
		print ("Mutation: host")
		host = mutate_host (host)
		print ("Mutated host: " + host)
	elif choose_mutation_location >= (pbbt_scheme + pbbt_host) and choose_mutation_location < (pbbt_scheme + pbbt_host + pbbt_port):
		print ("Mutation: port")
		port = mutate_port (port)
		print ("Mutated port: " + port)
	else:
		print ("Mutation: path")
		path = mutate_path (path)
		print ("Mutated path: " + path)



def mutate_scheme (scheme):
	scheme_list = ["http://", "https://", "masque://", "ftp://", "file-", "mailto:", "tel:", "sms:", "skype:"]
	choose_mutation = random.randint (0, 6)
	if choose_mutation == 0:
		scheme = change_random_character (scheme)
	elif choose_mutation == 1:
		scheme = havoc_sp (scheme)
	elif choose_mutation == 2:
		scheme = insert_characters (scheme)
	elif choose_mutation == 3:
		scheme = delete_characters (scheme)
	elif choose_mutation == 4:
		scheme = swap_characters (scheme)
	elif choose_mutation == 5:
		scheme = bitflip_random_character (scheme)
	else:
		list_idx = random.randint (0, 8)
		scheme = scheme_list [list_idx]

def mutate_host (host):
	choose_mutation = random.randint (0, 5)
	if choose_mutation == 0:
		host = change_random_character (host)
	elif choose_mutation == 1:
		host = havoc_hp (host)
	elif choose_mutation == 2:
		host = insert_characters (host)
	elif choose_mutation == 3:
		host = delete_characters (host)
	elif choose_mutation == 4:
		host = swap_characters (host)
	else:
		host = bitflip_random_character (host)

def mutate_port (port):
	choose_mutation = random.randint (0, 5)
	if choose_mutation == 0:
		port = change_random_character (port)
	elif choose_mutation == 1:
		port = havoc_sp (port)
	elif choose_mutation == 2:
		port = insert_characters (port)
	elif choose_mutation == 3:
		port = delete_characters (port)
	elif choose_mutation == 4:
		port = swap_characters (port)
	else:
		port = bitflip_random_character (port)

def mutate_path (path):
	choose_mutation = random.randint (0, 5)
	if choose_mutation == 0:
		path = change_random_character (path)
	elif choose_mutation == 1:
		path = havoc_hp (path)
	elif choose_mutation == 2:
		path = insert_characters (path)
	elif choose_mutation == 3:
		path = delete_characters (path)
	elif choose_mutation == 4:
		path = swap_characters (path)
	else:
		path = bitflip_random_character (path)

def generate_random_character ():
	asciicode = random.randint (32, 126)
	return chr (asciicode)

def change_random_character (target):
	if target == "":
		return target
	target_len = len (target)
	idx = random.randint (0, target_len - 1)
	front = target [0:idx]
	back = target [idx + 1: target_len]
	target = front + generate_random_character () + back
	return target

def havoc_sp (target):
	choose_havoc = random.randint (0, 1)
	if choose_havoc == 0:
		target = ''
	else:
		add_len = random.randint (30, 80)
		for i in range (len(target), add_len):
			target += generate_random_character ()
	return target

def havoc_hp (target):
	choose_havoc = random.randint (0, 1)
	if choose_havoc == 0:
		target = ''
	else:
		add_len = random.randint (200, 900)
		for i in range (len(target), add_len):
			target += generate_random_character ()
	return target

def insert_characters (target):
	insert_len = random.randint (1, 5)
	inserted = ""
	for i in range (insert_len):
		inserted += generate_random_character ()
	if target == "":
		target += inserted
		return target
	idx_insert = random.randint (0, len(target))
	front = target [:idx_insert]
	if idx_insert != len(target):
		back = target[idx_insert:len(target)]
		target = front + inserted + back
	else:
		target += inserted
	return target

def delete_characters (target):
	if target == "":
		return target
	delete_len = random.randint (1, len(target))
	delete_from = random.randint (0, len(target) - delete_len)
	if delete_from != 0:
		front = target[0:delete_from]
		back = target[delete_from + delete_len: len(target)]
		target = front + back
	else:
		back = target [delete_len:len(target)]
		target = back
	return target

def swap_characters (target):
	if target == "":
		return target
	idx = random.randint (0, len(target) - 2)
	new_chr = target[idx + 1]
	new_chr2 = target[idx]
	front = target [0:idx]
	back = target [idx +2:len(target)]
	target = front + new_chr + new_chr2 + back
	return target

def bitflip_random_character (target):
	if target == "":
		target += inserted
	idx = random.randint(0, len(target) - 1)
	c = target [idx]
	bit = 1 << random.randint(0, 6)
	new_c = chr(ord(c) ^ bit)
	target =  target[:idx] + new_c + target[idx + 1:]
	return target


print ("1" + change_random_character ("google.com"))
print ("2" + havoc_hp ("google.com"))
print ("3" + havoc_sp("google.com"))
print ("4" + insert_characters ("google.com"))
print ("5" + delete_characters ("google.com"))
print ("6" + swap_characters ("google.com"))
print ("7" + bitflip_random_character ("google.com"))