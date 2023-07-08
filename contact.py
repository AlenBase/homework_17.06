flag  = True
dic = {}
while  flag:
    try:
        darget = int(input("1 Add, 2 Search, 3 print_full, 4 Exit: "))
    except ValueError:
        print("Input integer ")
        continue
    if darget == 1:
        name = input("Add_name: ")
        contact = int(input("Add_contact: "))
        dic[name] = contact
    elif darget == 2:
        search_name = input("Input search_name: ")
        print(dic.get(search_name))
    elif darget == 3:
        for name, contact in dic.items():
            print(f"{name} :{contact}")
    elif darget == 4:
        flag = False
    else:
        break