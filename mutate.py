import random

def mutate (pbbt_scheme0, pbbt_scheme1, pbbt_scheme2, pbbt_scheme3, pbbt_scheme4, pbbt_scheme5, pbbt_scheme6, pbbt_host0, pbbt_host1, pbbt_host2, pbbt_host3, pbbt_host4, pbbt_host5, pbbt_port0, pbbt_port1, pbbt_port2, pbbt_port3, pbbt_port4, pbbt_port5, pbbt_path0, pbbt_path1, pbbt_path2, pbbt_path3, pbbt_path4, pbbt_path5, scheme, host, port, path):
	choose_mutation_location_operator = random.uniform (0, 100)
	print (choose_mutation_location_operator)
	boundary0 = pbbt_scheme0
	boundary1 = pbbt_scheme0 + pbbt_scheme1
	boundary2 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2
	boundary3 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3
	boundary4 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3 + pbbt_scheme4
	boundary5 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3 + pbbt_scheme4 + pbbt_scheme5
	boundary6 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3 + pbbt_scheme4 + pbbt_scheme5 + pbbt_scheme6
	boundary7 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3 + pbbt_scheme4 + pbbt_scheme5 + pbbt_scheme6 + pbbt_host0
	boundary8 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3 + pbbt_scheme4 + pbbt_scheme5 + pbbt_scheme6 + pbbt_host0 + pbbt_host1
	boundary9 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3 + pbbt_scheme4 + pbbt_scheme5 + pbbt_scheme6 + pbbt_host0 + pbbt_host1 + pbbt_host2
	boundary10 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3 + pbbt_scheme4 + pbbt_scheme5 + pbbt_scheme6 + pbbt_host0 + pbbt_host1 + pbbt_host2 + pbbt_host3
	boundary11 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3 + pbbt_scheme4 + pbbt_scheme5 + pbbt_scheme6 + pbbt_host0 + pbbt_host1 + pbbt_host2 + pbbt_host3 + pbbt_host4
	boundary12 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3 + pbbt_scheme4 + pbbt_scheme5 + pbbt_scheme6 + pbbt_host0 + pbbt_host1 + pbbt_host2 + pbbt_host3 + pbbt_host4 + pbbt_host5
	boundary13 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3 + pbbt_scheme4 + pbbt_scheme5 + pbbt_scheme6 + pbbt_host0 + pbbt_host1 + pbbt_host2 + pbbt_host3 + pbbt_host4 + pbbt_host5 + pbbt_port0
	boundary14 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3 + pbbt_scheme4 + pbbt_scheme5 + pbbt_scheme6 + pbbt_host0 + pbbt_host1 + pbbt_host2 + pbbt_host3 + pbbt_host4 + pbbt_host5 + pbbt_port0 + pbbt_port1
	boundary15 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3 + pbbt_scheme4 + pbbt_scheme5 + pbbt_scheme6 + pbbt_host0 + pbbt_host1 + pbbt_host2 + pbbt_host3 + pbbt_host4 + pbbt_host5 + pbbt_port0 + pbbt_port1 + pbbt_port2
	boundary16 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3 + pbbt_scheme4 + pbbt_scheme5 + pbbt_scheme6 + pbbt_host0 + pbbt_host1 + pbbt_host2 + pbbt_host3 + pbbt_host4 + pbbt_host5 + pbbt_port0 + pbbt_port1 + pbbt_port2 + pbbt_port3
	boundary17 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3 + pbbt_scheme4 + pbbt_scheme5 + pbbt_scheme6 + pbbt_host0 + pbbt_host1 + pbbt_host2 + pbbt_host3 + pbbt_host4 + pbbt_host5 + pbbt_port0 + pbbt_port1 + pbbt_port2 + pbbt_port3 + pbbt_port4
	boundary18 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3 + pbbt_scheme4 + pbbt_scheme5 + pbbt_scheme6 + pbbt_host0 + pbbt_host1 + pbbt_host2 + pbbt_host3 + pbbt_host4 + pbbt_host5 + pbbt_port0 + pbbt_port1 + pbbt_port2 + pbbt_port3 + pbbt_port4 + pbbt_port5
	boundary19 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3 + pbbt_scheme4 + pbbt_scheme5 + pbbt_scheme6 + pbbt_host0 + pbbt_host1 + pbbt_host2 + pbbt_host3 + pbbt_host4 + pbbt_host5 + pbbt_port0 + pbbt_port1 + pbbt_port2 + pbbt_port3 + pbbt_port4 + pbbt_port5 + pbbt_path0
	boundary20 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3 + pbbt_scheme4 + pbbt_scheme5 + pbbt_scheme6 + pbbt_host0 + pbbt_host1 + pbbt_host2 + pbbt_host3 + pbbt_host4 + pbbt_host5 + pbbt_port0 + pbbt_port1 + pbbt_port2 + pbbt_port3 + pbbt_port4 + pbbt_port5 + pbbt_path0 + pbbt_path1
	boundary21 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3 + pbbt_scheme4 + pbbt_scheme5 + pbbt_scheme6 + pbbt_host0 + pbbt_host1 + pbbt_host2 + pbbt_host3 + pbbt_host4 + pbbt_host5 + pbbt_port0 + pbbt_port1 + pbbt_port2 + pbbt_port3 + pbbt_port4 + pbbt_port5 + pbbt_path0 + pbbt_path1 + pbbt_path2
	boundary22 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3 + pbbt_scheme4 + pbbt_scheme5 + pbbt_scheme6 + pbbt_host0 + pbbt_host1 + pbbt_host2 + pbbt_host3 + pbbt_host4 + pbbt_host5 + pbbt_port0 + pbbt_port1 + pbbt_port2 + pbbt_port3 + pbbt_port4 + pbbt_port5 + pbbt_path0 + pbbt_path1 + pbbt_path2 + pbbt_path3
	boundary23 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3 + pbbt_scheme4 + pbbt_scheme5 + pbbt_scheme6 + pbbt_host0 + pbbt_host1 + pbbt_host2 + pbbt_host3 + pbbt_host4 + pbbt_host5 + pbbt_port0 + pbbt_port1 + pbbt_port2 + pbbt_port3 + pbbt_port4 + pbbt_port5 + pbbt_path0 + pbbt_path1 + pbbt_path2 + pbbt_path3 + pbbt_path4
	boundary24 = pbbt_scheme0 + pbbt_scheme1 + pbbt_scheme2 + pbbt_scheme3 + pbbt_scheme4 + pbbt_scheme5 + pbbt_scheme6 + pbbt_host0 + pbbt_host1 + pbbt_host2 + pbbt_host3 + pbbt_host4 + pbbt_host5 + pbbt_port0 + pbbt_port1 + pbbt_port2 + pbbt_port3 + pbbt_port4 + pbbt_port5 + pbbt_path0 + pbbt_path1 + pbbt_path2 + pbbt_path3 + pbbt_path4 + pbbt_path5

	if choose_mutation_location_operator < boundary0:
		#print ("Mutation: scheme")
		location_operator = "scheme0"
		scheme = change_random_character (scheme)
		#print ("Mutated scheme: " + scheme)
	elif choose_mutation_location_operator >= boundary0 and choose_mutation_location_operator < boundary1:
		#print ("Mutation: scheme")
		location_operator = "scheme1"
		scheme = havoc_sp (scheme)
		#print ("Mutated scheme: " + scheme)
	elif choose_mutation_location_operator >= boundary1 and choose_mutation_location_operator < boundary2:
		#print ("Mutation: scheme")
		location_operator = "scheme2"
		scheme = insert_characters (scheme)
		#print ("Mutated scheme: " + scheme)
	elif choose_mutation_location_operator >= boundary2 and choose_mutation_location_operator < boundary3:
		#print ("Mutation: scheme")
		location_operator = "scheme3"
		scheme = delete_characters (scheme)
		#print ("Mutated scheme: " + scheme)
	elif choose_mutation_location_operator >= boundary3 and choose_mutation_location_operator < boundary4:
		#print ("Mutation: scheme")
		location_operator = "scheme4"
		scheme = swap_characters (scheme)
		#print ("Mutated scheme: " + scheme)
	elif choose_mutation_location_operator >= boundary4 and choose_mutation_location_operator < boundary5:
		#print ("Mutation: scheme")
		location_operator = "scheme5"
		scheme = bitflip_random_character (scheme)
		#print ("Mutated scheme: " + scheme)
	elif choose_mutation_location_operator >= boundary5 and choose_mutation_location_operator < boundary6:
		#print ("Mutation: scheme")
		location_operator = "scheme6"
		scheme = change_scheme (scheme)
		#print ("Mutated scheme: " + scheme)
	elif choose_mutation_location_operator >= boundary6 and choose_mutation_location_operator < boundary7:
		#print ("Mutation: host")
		location_operator = "host0"
		host = change_random_character (host)
		#print ("Mutated host: " + host)
	elif choose_mutation_location_operator >= boundary7 and choose_mutation_location_operator < boundary8:
		#print ("Mutation: host")
		location_operator = "host1"
		host = havoc_hp (host)
		#print ("Mutated host: " + host)
	elif choose_mutation_location_operator >= boundary8 and choose_mutation_location_operator < boundary9:
		#print ("Mutation: host")
		location_operator = "host2"
		host = insert_characters (host)
		#print ("Mutated host: " + host)
	elif choose_mutation_location_operator >= boundary9 and choose_mutation_location_operator < boundary10:
		#print ("Mutation: host")
		location_operator = "host3"
		host = delete_characters (host)
		#print ("Mutated host: " + host)
	elif choose_mutation_location_operator >= boundary10 and choose_mutation_location_operator < boundary11:
		#print ("Mutation: host")
		location_operator = "host4"
		host = swap_characters (host)
		#print ("Mutated host: " + host)
	elif choose_mutation_location_operator >= boundary11 and choose_mutation_location_operator < boundary12:
		#print ("Mutation: host")
		location_operator = "host5"
		host = bitflip_random_character (host)
		#print ("Mutated host: " + host)
	elif choose_mutation_location_operator >= boundary12 and choose_mutation_location_operator < boundary13:
		#print ("Mutation: port")
		location_operator = "port0"
		port = change_random_character (port)
		#print ("Mutated port: " + port)
	elif choose_mutation_location_operator >= boundary13 and choose_mutation_location_operator < boundary14:
		#print ("Mutation: port")
		location_operator = "port1"
		port = havoc_sp (port)
		#print ("Mutated port: " + port)
	elif choose_mutation_location_operator >= boundary14 and choose_mutation_location_operator < boundary15:
		#print ("Mutation: port")
		location_operator = "port2"
		port = insert_characters (port)
		#print ("Mutated port: " + port)
	elif choose_mutation_location_operator >= boundary15 and choose_mutation_location_operator < boundary16:
		#print ("Mutation: port")
		location_operator = "port3"
		port = delete_characters (port)
		#print ("Mutated port: " + port)
	elif choose_mutation_location_operator >= boundary16 and choose_mutation_location_operator < boundary17:
		#print ("Mutation: port")
		location_operator = "port4"
		port = swap_characters (port)
		#print ("Mutated port: " + port)
	elif choose_mutation_location_operator >= boundary17 and choose_mutation_location_operator < boundary18:
		#print ("Mutation: port")
		location_operator = "port5"
		port = bitflip_random_character (port)
		#print ("Mutated port: " + port)
	elif choose_mutation_location_operator >= boundary18 and choose_mutation_location_operator < boundary19:
		#print ("Mutation: path")
		location_operator = "path0"
		path = change_random_character (path)
		#print ("Mutated path: " + path)
	elif choose_mutation_location_operator >= boundary19 and choose_mutation_location_operator < boundary20:
		#print ("Mutation: path")
		location_operator = "path1"
		path = havoc_hp (path)
		#print ("Mutated path: " + path)
	elif choose_mutation_location_operator >= boundary20 and choose_mutation_location_operator < boundary21:
		#print ("Mutation: path")
		location_operator = "path2"
		path = insert_characters (path)
		#print ("Mutated path: " + path)
	elif choose_mutation_location_operator >= boundary21 and choose_mutation_location_operator < boundary22:
		#print ("Mutation: path")
		location_operator = "path3"
		path = delete_characters (path)
		#print ("Mutated path: " + path)
	elif choose_mutation_location_operator >= boundary22 and choose_mutation_location_operator < boundary23:
		#print ("Mutation: path")
		location_operator = "path4"
		path = swap_characters (path)
		#print ("Mutated path: " + path)
	else:
		#print ("Mutation: path")
		location_operator = "path5"
		path = bitflip_random_character (path)
		#print ("Mutated path: " + path)

	return scheme, host, port, path, location_operator

'''def mutate_scheme (scheme):
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
	return scheme

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
	return host

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
	return port

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
	return path'''

def generate_random_character ():
	asciicode = random.randint (32, 126)
	return chr (asciicode)

def change_scheme (scheme):
	scheme_list = ["http://", "https://", "masque://", "ftp://", "file-", "mailto:", "tel:", "sms:", "skype:"]
	list_idx = random.randint (0, 8)
	scheme = scheme_list [list_idx]
	return scheme

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
	if len(target) == 0 or len(target) == 1:
		return target
	idx = random.randint (0, len(target) - 2)
	new_chr = target[idx + 1]
	new_chr2 = target[idx]
	front = target [0:idx]
	back = target [idx +2:len(target)]
	target = front + new_chr + new_chr2 + back
	return target

def bitflip_random_character (target):
	inserted = ""
	if target == "":
		return target
	idx = random.randint(0, len(target) - 1)
	c = target [idx]
	bit = 1 << random.randint(0, 6)
	new_c = chr(ord(c) ^ bit)
	if(new_c == '\0'):
		return target
	target =  target[:idx] + new_c + target[idx + 1:]
	return target


'''print ("1" + change_random_character ("google.com"))
print ("2" + havoc_hp ("google.com"))
print ("3" + havoc_sp("google.com"))
print ("4" + insert_characters ("google.com"))
print ("5" + delete_characters ("google.com"))
print ("6" + swap_characters ("google.com"))
print ("7" + bitflip_random_character ("google.com"))

print (mutate (25, 25, 25, 25, "https://", "google.com", ":5300", "/watch?v=grtqJsO_hb0&t=7771s"))'''

print (mutate (4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, "https://", "google.com", ":8080", "/watch?v=grtqJsO_hb0&t=7771s"))