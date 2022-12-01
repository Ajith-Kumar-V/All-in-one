def register_check(dicty):
    cnt=0
    for i in dicty:
        if (dicty[i]=='yes') | (dicty[i]=='Yes'):
            cnt+=1
    return cnt
register={'John':'yes','Peter':'yes','Daemon':'no','Lucy':'yes','Elena':'Yes','colombus':'yes'}
valu=register_check(register)
print(valu)
