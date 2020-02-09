import os,glob

#print(os.getcwd())

# a_list = [1,9,8,4]
# a_list = [elem * 2 for elem in a_list]
# print(a_list)

# print(glob.glob('*.py'))

a_dict = {'a':1, 'b':2, 'c':3}
print({value:key for key, value in a_dict.items()})