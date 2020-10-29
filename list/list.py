# VARIABLES TIPO LIST
#CREATE
var_list_0 = [1,2,3,4]
var_list_1 = ["a","b","c","d"]
var_list_2 = ["a",1,"b",2]
var_list_3 = [[1,2,3,4],["a","b","c","d"]] #nested list
var_list_4 = [var_list_0, var_list_1]      #nested list

print(var_list_3 == var_list_4)

#READ
print(var_list_0)

print(var_list_0[0])

print(var_list_0[0:2])

print(var_list_0[:2])

print(var_list_0[-1])

print(var_list_0[1:3])

print(var_list_3)

print(len(var_list_3))

print(var_list_3[0])

print(var_list_3[1])

print(var_list_3[2]) # intentional error. out of index

print(var_list_3[0][0]) #Two index because there is a nested structure

print(var_list_3[0][0] == var_list_4[0][0])

#UPDATE
var_list_0[0] = 1

var_list_3[0] = [10,11,12,13]

var_list_3[1] = ["w","x","y","z"]

#DELETE
del var_list_2[1]
del var_list_2[-1]

print(var_list_2)
