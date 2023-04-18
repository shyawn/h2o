import math, random

def update_probability (location_operator_dic, location_operator, incdec):
	if incdec == 0:
		change = math.log10 (101 - location_operator_dic.get(location_operator))
		print (change)
		location_operator_dic[location_operator] += change
		for loc_op in location_operator_dic:
			location_operator_dic [loc_op] *= ((100) / (100 + change))

	else:
		change = math.log10 (location_update_dic.get(location_operator) + 1)
		print (change)
		location_operator_dic[location_operator] -= change
		for loc_op in location_operator_dic:
			location_operator_dic [loc_op] *= ((100) / (100 - change))

	sum_pbbt = 0
	for loc_op in location_operator_dic:
		sum_pbbt += location_operator_dic[loc_op]
	diff_100 = 100 - sum_pbbt
	adjust_location_operator = random.choice (list (location_operator_dic.keys()))
	print (adjust_location_operator)
	#print (diff_100)
	location_operator_dic[adjust_location_operator] += diff_100
	
	return location_operator_dic

'''pbbt_scheme = 48
pbbt_host = 32
pbbt_port = 4
pbbt_path = 16
while (True):
	result = update_probability (pbbt_scheme, pbbt_host, pbbt_port, pbbt_path, "scheme", 0)
	pbbt_scheme = result[0]
	pbbt_host = result[1]
	pbbt_port = result[2]
	pbbt_path = result[3]
	print (str(result[0]), str(result[1]),str(result[2]),str(result[3]))'''

#location_operator_dic = {"pbbt_scheme0" : 1, "pbbt_scheme1" : 1.5, "pbbt_scheme2" : 2, "pbbt_scheme3" : 2.5, "pbbt_scheme4" : 0.5, "pbbt_scheme5" : 3, "pbbt_scheme6" : 3.5, "pbbt_host0" : 4, "pbbt_host1" : 4.5, "pbbt_host2" : 5, "pbbt_host3" : 5.5, "pbbt_host4" : 6, "pbbt_host5" : 6.5, "pbbt_port0" : 7, "pbbt_port1" : 7.5, "pbbt_port2" : 0.8, "pbbt_port3" : 1.6, "pbbt_port4" : 2.4, "pbbt_port5" : 3.2, "pbbt_path0" : 4.8, "pbbt_path1" : 5.6, "pbbt_path2" : 6.4, "pbbt_path3" : 7.2, "pbbt_path4" : 3.9, "pbbt_path5" : 4.1}
#print (update_probability (location_operator_dic, "pbbt_scheme0", 1))
#print(update_probability (1, 1.5, 2, 2.5, 0.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 0.8, 1.6, 2.4, 3.2, 4.8, 5.6, 6.4, 7.2, 3.9, 4.1, "path5", 0))