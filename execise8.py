import sys
with open(sys.argv[1]) as data:
    dict_da = {}
    list_da = [x.split(":") for x in data.read().splitlines()]
    for i in list_da: dict_da[i[0]] = str(i[1])
    for j in sys.argv[2].split(","):
        try:
            print(f"{j},University: {dict_da[j]}")
        except:
            print(f"No record '{j}' was found")





