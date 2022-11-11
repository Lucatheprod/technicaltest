#Luca Scardaccione - + 54 9 11 2161 8490

#                 E X E R C I S E     O N E :  Name: Simple


from random import randint, random, uniform




#Item One

list = []

for n in range(0,9):
    list.append({"Id" : random(), "Age": randint(1,100)})
print("The list is:" , list)


#Item Two
sorted_list = (sorted(list, key = lambda i: (i["Age"])))
#Sorted list by Age

print("•The youngest person is:" , sorted_list[0].get("Id")) 
print("•The oldest person is:" , sorted_list[-1].get("Id"))
print("•The sorted list is:" , sorted_list)




    


