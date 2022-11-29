fruits={'fruit':'apple','color':'red','transport':'boats'}
def longest_value(dicts):
    dictionary=dicts
    lens=[]
    for x in dictionary:
        lens.append(len(dictionary[x]))
    s=lens.index(max(lens))
    h=list(dictionary)[s]
    return (fruits[h])
res=longest_value(fruits)
print(res)
