'''

simple code to write to file


'''


import os
import sys


# method 1
# the directory where the file is
path = os.path.dirname(sys.argv[0])
print(f'the file resides here: {path}')



# method 2
# the directory where the file is
path = os.path.dirname(os.path.realpath(__file__))
print(f'the file resides here: {path}')



# method 3 - this is the best method
# the directory where the file is
path = os.path.dirname(__file__)
print(f'the file resides here: {path}')



# string for file in current working directory
tFile = path + "\\" + 'testfilex.txt'

file = open(tFile, 'w')

file.write('hello world')
file.write('this is our new text file')
file.write('this is another line')

print(file)
print(file.name)


file.close()


print('success: the file was written to')


