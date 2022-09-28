dict_a={"卵":100,"パン":150}
dict_b={"トマト":120}

for i,x in dict_a.items():
        if x > dict_b["トマト"]:
            dict_a[i] = dict_b["トマト"]

print(dict_a)
