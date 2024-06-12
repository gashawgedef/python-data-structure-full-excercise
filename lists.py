# 1. Write a  Python program to sum all the items in a list.


import random


def sumList(list):
    sum=0
    for item in list:
        sum+=item
        return sum
#. Write a  Python program to multiply all the items in a list.
def multiplyEachList(list):
    product=1
    for item in list:
        product*=item
    return product


#Write a Python program to get the largest number from a list.
def getLargest(list):
    max=list[0]
    for item in list:
        if item>max:
            max=item
    return max
#Write a Python program to get the smallest number from a list.
def getSmallest(list):
    min=list[0]
    for item in list:
        if item<min:
            min=item
    return min
#Write a  Python program to count the number of strings from a given list of strings. 
def countStrings(words):
    count=0
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            count+=1
    return count

#Write a  Python program to remove duplicates from a list.
def removeDuplicates(list):
    uniq_elements=set()
    element_list=[]
    for item in list:
        if item not in uniq_elements:
            element_list.append(item)
            uniq_elements.add(item)
    return element_list
#Write a  Python program to check if a list is empty or not.
def isEmptyList(list):
    if len(list)==0:
        return True
    return False
#Write a Python program to find the list of words that are longer than n from a given list of words.
def longer_than_n(list,n):
    word_list=[]
    for item in list:
        if len(item) > n:
            word_list.append(item)
    return word_list


def convert_list_string(list):
    string=''.join(list)
    return string
#Write a Python program to find the index of an item in a specified list.
def findIndex(list,item):
    return list.index(item)
#Write a Python program to append a list to the second list.
def appendList(list1,list2):
    list3=list1+list2
    return list3
#Write a Python program to select an item randomly from a list.
def selectRandom(list):
    return random.choice(list)
#Write a  Python program to sort (ascending and descending) a dictionary by value.
def sort_dictionary_by_value(dict,ascending=True):
    sorted_dic=sorted(dict.items(),key=lambda item:item[1],reverse=not ascending)
    return dict(sorted_dic) 

#Write a Python script to add a key to a dictionary.
def add_key(dict,key,value):
    dict[key]=value
    return dict
def is_key_exist(dict,key):
    for keys in dict:
        if key in dict:
            return True
    return False


def num_bet_n(n):
    dict={}
    for x in range(1,n+1):
        dict[x]=x**2
    return dict
#Write a Python program to sum all the items in a dictionary.
def sum_dict_values(dict):
    total=0
    for key, value in dict.items():
        total+=value
    return total 


print(add_key({"name":"Gashaw"},"last_name","Gedef"))
print(is_key_exist({"name":"Gashaw","last_name":"Gedef"},"last_name"))
print(num_bet_n(5))
print(sum_dict_values({"Salary":123,"Values":37}))