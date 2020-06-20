#Here we implement array in python 

# import array library of python
import array as ar

#------ we create integer array ------# 
# 	'i' - type code
# 	Type Code - Determine type of the array at the time of creation
array = ar.array('i', [1, 4, 5, 6])
print(array)

#------ Read element at nth position ------#
print("Read element at n th position")
print("At 0th position : ", array[0])
print("At 1th position : ", array[1])
print("At 2nd position : ", array[2])
print("At 3rd position : ", array[3])

#------ Modify element at nth position ------#
print("Modify element at n th position")
array[1] = 8
print(array)

#------Insert/store element at nth position------#

# Adding element at tail of the array
print("Adding element at tail")
array.append(9)
print(array)

# Adding multiple element at from tail 
print("Adding multiple elements from the tail")
array.extend([3, 7, 1, 0])
print(array)


#------ Remove element at nth position ------#

print("Remove Element at nth position")
del array[3]
print(array)


