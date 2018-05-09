st = [{"Dinesh":"Dinesh","id":8},{"Kumar":"Kumar","id":9},{"Howgwarts":"Howgwarts","id":7},{"Harry":"Harry","id":5},{"Potter":"Potter","id":3}]

for i in st:
    try:
        if "Dinesh" in i:
            print("Found")
        else:
            print(i["id"])
    except Exception as e:
        print (e)