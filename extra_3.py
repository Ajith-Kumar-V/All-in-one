def lower_tuple(names):
    n_lis=[]
    for i in names:
        if i.islower():
            n_lis.append(i)
    n_lis.sort(reverse=True)
    tuples=tuple(n_lis)
    return tuples
name=["kerry","dickson","John","Mary","carol","adam","charlie"]
value=lower_tuple(name)
print(value)
