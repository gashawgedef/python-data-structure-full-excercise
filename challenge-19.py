

def concate_string(value):
    if len(value) >=2 and value[:2]=="ls":
        return value
    else:
        return "ls"+value
    

print(concate_string("lsgashaw"))
# Write a  Python program to count the number 4 in a given list.

def count4(values):
    count = 0
    for value in values:
        if value ==4:
            count += 1
    return count


print(count4([4,4,4,5,78,89,67]))
        
