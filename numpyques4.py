# Write a NumPy program to convert a list and tuple into arrays.

import numpy as np
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_tuple = ([8, 4, 6], [1, 2, 3])
print("List:-\n",my_list)
print("Tuple:-\n",my_tuple)
array_list=np.array(my_list)
array_tuple=np.array(my_tuple)
print("List into array:-\n",array_list)
print("Tuple into array:-\n",array_tuple)