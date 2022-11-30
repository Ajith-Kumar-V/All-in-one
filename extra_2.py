def check_duplicates(arr):
    array=arr
    for i in array:
        c=array.count(i)
        if c>1:
            return i
    else:
        return "No duplicates"
fruits=['apple','orange','banana','mango','mango','apple']
print(check_duplicates(fruits))
