import random

def mutate (location_operator_dic, scheme, host, port, path):
	choose_mutation_location_operator = random.uniform (0, 100)
	print (choose_mutation_location_operator)
	
	temp_sum_ppbt = 0
	for loc_op in location_operator_dic:
		temp_sum_ppbt += location_operator_dic[loc_op]
		if choose_mutation_location_operator < temp_sum_ppbt:
			location_operator = loc_op
			break
	print (location_operator)

	if location_operator == "pbbt_scheme0":
		scheme = change_random_character (scheme)
	elif location_operator == "pbbt_scheme1":
		scheme = havoc_sp (scheme)
	elif location_operator == "pbbt_scheme2":
		scheme = insert_characters (scheme)
	elif location_operator == "pbbt_scheme3":
		scheme = delete_characters (scheme)
	elif location_operator == "pbbt_scheme4":
		scheme = swap_characters (scheme)
	elif location_operator == "pbbt_scheme5":
		scheme = bitflip_random_character (scheme)
	elif location_operator == "pbbt_scheme6":
		scheme = change_scheme (scheme)
	elif location_operator == "pbbt_host0":
		host = change_random_character (host)
	elif location_operator == "pbbt_host1":
		host = havoc_hp (host)
	elif location_operator == "pbbt_host2":
		host = insert_characters (host)
	elif location_operator == "pbbt_host3":
		host = delete_characters (host)
	elif location_operator == "pbbt_host4":
		host = swap_characters (host)
	elif location_operator == "pbbt_host5":
		host = bitflip_random_character (host)
	elif location_operator == "pbbt_port0":
		port = change_random_character (port)
	elif location_operator == "pbbt_port1":
		port = havoc_sp (port)
	elif location_operator == "pbbt_port2":
		port = insert_characters (port)
	elif location_operator == "pbbt_port3":
		port = delete_characters (port)
	elif location_operator == "pbbt_port4":
		port = swap_characters (port)
	elif location_operator == "pbbt_port5":
		port = bitflip_random_character (port)
	elif location_operator == "pbbt_path0":
		path = change_random_character (path)
	elif location_operator == "pbbt_path1":
		path = havoc_hp (path)
	elif location_operator == "pbbt_path2":
		path = insert_characters (path)
	elif location_operator == "pbbt_path3":
		path = delete_characters (path)
	elif location_operator == "pbbt_path4":
		path = swap_characters (path)
	else:
		path = bitflip_random_character (path)
  
	if len(scheme) > 100:
		scheme = scheme[0:100]
	if len(host) > 400:
		host = host[0:400]
	
	if len(port) > 100:
		port = port[0:100]
	if len(host) > 400:
		host = host[0:400]
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
		add_len = random.randint (30, 100)
		for i in range (len(target), add_len):
			target += generate_random_character ()
	return target

def havoc_hp (target):
	choose_havoc = random.randint (0, 1)
	if choose_havoc == 0:
		target = ''
	else:
		add_len = random.randint (200, 400)
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
# location_operator_dic = {"pbbt_scheme0" : 4, "pbbt_scheme1" : 4, "pbbt_scheme2" : 4, "pbbt_scheme3" : 4, "pbbt_scheme4" : 4, "pbbt_scheme5" : 4, "pbbt_scheme6" : 4, "pbbt_host0" : 4, "pbbt_host1" : 4, "pbbt_host2" : 4, "pbbt_host3" : 4, "pbbt_host4" : 4, "pbbt_host5" : 4, "pbbt_port0" : 4, "pbbt_port1" : 4, "pbbt_port2" : 4, "pbbt_port3" : 4, "pbbt_port4" : 4, "pbbt_port5" : 4, "pbbt_path0" : 4, "pbbt_path1" : 4, "pbbt_path2" : 4, "pbbt_path3" : 4, "pbbt_path4" : 4, "pbbt_path5" : 4}
# print (mutate (location_operator_dic, "https://", "google.com", ":8080", "/watch?v=grtqJsO_hb0&t=7771s"))