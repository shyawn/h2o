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
	pass

def mutate_host (host):
	pass

def mutate_port (port):
	pass

def mutate_path (path):
	pass