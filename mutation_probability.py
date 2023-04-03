import math

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
			change = math.log10 (100 - pbbt_scheme)
			pbbt_scheme -= change
			pbbt_scheme *= ((100) / (100 - change))
			pbbt_host *= ((100) / (100 - change))
			pbbt_port *= ((100) / (100 - change))
			pbbt_path *= ((100) / (100 - change))
		elif location == "host":
			change = math.log10 (100 - pbbt_host)
			pbbt_host -= change
			pbbt_scheme *= ((100) / (100 - change))
			pbbt_host *= ((100) / (100 - change))
			pbbt_port *= ((100) / (100 - change))
			pbbt_path *= ((100) / (100 - change))
		elif location == "port":
			change = math.log10 (100 - pbbt_port)
			pbbt_port -= change
			pbbt_scheme *= ((100) / (100 - change))
			pbbt_host *= ((100) / (100 - change))
			pbbt_port *= ((100) / (100 - change))
			pbbt_path *= ((100) / (100 - change))
		else:
			change = math.log10 (100 - pbbt_path)
			pbbt_path -= change
			pbbt_scheme *= ((100) / (100 - change))
			pbbt_host *= ((100) / (100 - change))
			pbbt_port *= ((100) / (100 - change))
			pbbt_path *= ((100) / (100 - change))
			
	return pbbt_scheme, pbbt_host, pbbt_port, pbbt_path