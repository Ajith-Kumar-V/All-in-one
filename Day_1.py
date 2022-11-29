def divide_or_square():
    n=int(input())
    if n%5==0:
        print('%0.2f'%(n**0.5))
    else:
        print('%0.2f'%(n/5))
divide_or_square()
