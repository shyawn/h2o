state_list = ["C", "D", "A"]
state_key ="A"
state_index = 0;
Is_in_sates = False
for states in state_list:
    if state_key in states:
        Is_in_sates = True
        break
    state_index += 1

if Is_in_sates == False:
    state_list.append([state_key, 0, 0])
    print("State Key : " + state_key)
print(state_index)
            