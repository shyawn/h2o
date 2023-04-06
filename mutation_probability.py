import math, random

def update_probability (pbbt_scheme, pbbt_host, pbbt_port, pbbt_path, location, incdec):
	if incdec == 0:
		if location == "scheme":
			change = math.log10 (100 - pbbt_scheme)
			pbbt_scheme += change
			pbbt_scheme *= ((100) / (100 + change))
			pbbt_host *= ((100) / (100 + change))
			pbbt_port *= ((100) / (100 + change))
			pbbt_path *= ((100) / (100 + change))
		elif location == "host":
			change = math.log10 (100 - pbbt_host)
			pbbt_host += change
			pbbt_scheme *= ((100) / (100 + change))
			pbbt_host *= ((100) / (100 + change))
			pbbt_port *= ((100) / (100 + change))
			pbbt_path *= ((100) / (100 + change))
		elif location == "port":
			change = math.log10 (100 - pbbt_port)
			pbbt_port += change
			pbbt_scheme *= ((100) / (100 + change))
			pbbt_host *= ((100) / (100 + change))
			pbbt_port *= ((100) / (100 + change))
			pbbt_path *= ((100) / (100 + change))
		else:
			change = math.log10 (100 - pbbt_path)
			pbbt_path += change
			pbbt_scheme *= ((100) / (100 + change))
			pbbt_host *= ((100) / (100 + change))
			pbbt_port *= ((100) / (100 + change))
			pbbt_path *= ((100) / (100 + change))

	else:
		if location == "scheme":
			change = math.log10 (pbbt_scheme)
			pbbt_scheme -= change
			pbbt_scheme *= ((100) / (100 - change))
			pbbt_host *= ((100) / (100 - change))
			pbbt_port *= ((100) / (100 - change))
			pbbt_path *= ((100) / (100 - change))
		elif location == "host":
			change = math.log10 (pbbt_host)
			pbbt_host -= change
			pbbt_scheme *= ((100) / (100 - change))
			pbbt_host *= ((100) / (100 - change))
			pbbt_port *= ((100) / (100 - change))
			pbbt_path *= ((100) / (100 - change))
		elif location == "port":
			change = math.log10 (pbbt_port)
			pbbt_port -= change
			pbbt_scheme *= ((100) / (100 - change))
			pbbt_host *= ((100) / (100 - change))
			pbbt_port *= ((100) / (100 - change))
			pbbt_path *= ((100) / (100 - change))
		else:
			change = math.log10 (pbbt_path)
			pbbt_path -= change
			pbbt_scheme *= ((100) / (100 - change))
			pbbt_host *= ((100) / (100 - change))
			pbbt_port *= ((100) / (100 - change))
			pbbt_path *= ((100) / (100 - change))
	diff_100 = 100 - (pbbt_scheme + pbbt_host + pbbt_path + pbbt_port)
	#print (diff_100)
	adjust_location = random.randint (0, 3)
	if adjust_location == 0:
		#print ("scheme")
		pbbt_scheme += diff_100
	elif adjust_location == 1:
		#print ("host")
		pbbt_host += diff_100
	elif adjust_location == 2:
		#print ("port")
		pbbt_port += diff_100
	else:
		#print ("path")
		pbbt_path += diff_100
	
	return pbbt_scheme, pbbt_host, pbbt_port, pbbt_path

'''pbbt_scheme = 48
pbbt_host = 32
pbbt_port = 4
pbbt_path = 16
while (True):
	result = update_probability (pbbt_scheme, pbbt_host, pbbt_port, pbbt_path, "scheme", 1)
	pbbt_scheme = result[0]
	pbbt_host = result[1]
	pbbt_port = result[2]
	pbbt_path = result[3]
	print (str(result[0]), str(result[1]),str(result[2]),str(result[3]))'''